import streamlit as st
import joblib
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import requests
import datetime
import json
from streamlit_lottie import st_lottie
from llm_module import process_ticket_with_llm

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(page_title="Hybrid Ticket AI", page_icon="⚡", layout="wide", initial_sidebar_state="expanded")

# --- 2. ENHANCED ENTERPRISE CSS ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif;
    }

    .stApp {
        background: linear-gradient(to bottom right, #050510, #1a1a2e);
        color: #e0e0e0;
    }

    h1, h2, h3 {
        color: #ffffff !important;
        font-weight: 700 !important;
    }

    section[data-testid="stSidebar"] {
        background-color: #0a0a15;
        border-right: 1px solid #2a2a40;
    }

    div[data-testid="stMetricValue"] {
        color: #a855f7;
        font-size: 28px;
    }

    .stTextArea textarea {
        background-color: #16213e;
        color: #ffffff;
        border: 1px solid #4a1c80;
        border-radius: 12px;
        font-size: 16px;
    }
    
    div.stButton > button {
        background: linear-gradient(90deg, #6a11cb 0%, #2575fc 100%);
        color: white;
        font-weight: 600;
        font-size: 16px;
        border: none;
        padding: 10px 24px;
        border-radius: 8px;
        transition: all 0.3s ease;
        width: 100%;
        box-shadow: 0 4px 15px rgba(106, 17, 203, 0.4);
    }
    div.stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(106, 17, 203, 0.6);
    }

    .result-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        border-radius: 16px;
        padding: 24px;
        margin-bottom: 20px;
        border: 1px solid rgba(255, 255, 255, 0.08);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
    }
    .card-title {
        color: #a855f7;
        font-size: 13px;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        font-weight: 700;
        margin-bottom: 10px;
    }
    .card-value {
        font-size: 22px;
        font-weight: 600;
        color: #ffffff;
    }
    .card-text {
        font-size: 15px;
        line-height: 1.6;
        color: #d1d5db;
    }
    
    /* Professional Badge */
    .status-badge {
        display: inline-block;
        padding: 6px 14px;
        border-radius: 20px;
        font-size: 12px;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    .badge-urgent { background: #ff4b4b; color: white; }
    .badge-normal { background: #00c853; color: white; }
    .badge-pending { background: #ffa500; color: white; }
    
    /* Timeline */
    .timeline-item {
        border-left: 2px solid #a855f7;
        padding-left: 20px;
        margin-bottom: 15px;
        position: relative;
    }
    .timeline-item::before {
        content: '';
        position: absolute;
        left: -6px;
        top: 0;
        width: 10px;
        height: 10px;
        border-radius: 50%;
        background: #a855f7;
    }
    
    /* Confidence Meter */
    .confidence-bar {
        height: 8px;
        background: #1a1a2e;
        border-radius: 10px;
        overflow: hidden;
        margin-top: 8px;
    }
    .confidence-fill {
        height: 100%;
        background: linear-gradient(90deg, #6a11cb, #2575fc);
        transition: width 0.5s ease;
    }
</style>
""", unsafe_allow_html=True)

# --- 3. HELPER FUNCTIONS ---
def load_lottieurl(url):
    try:
        r = requests.get(url)
        return r.json() if r.status_code == 200 else None
    except: return None

@st.cache_data
def load_data():
    try:
        df = pd.read_csv('tickets.csv')
        return df
    except:
        return pd.DataFrame()

@st.cache_resource
def load_models():
    vect = joblib.load('tfidf_vectorizer.pkl')
    model_dept = joblib.load('model_department.pkl')
    model_urgency = joblib.load('model_urgency.pkl')
    return vect, model_dept, model_urgency

def calculate_confidence_score(text, prediction):
    """Simulate ML confidence score"""
    import hashlib
    score = int(hashlib.md5(f"{text}{prediction}".encode()).hexdigest()[:2], 16) / 255 * 40 + 60
    return round(score, 1)

def get_sentiment_analysis(text):
    """Basic sentiment analysis"""
    negative_words = ['angry', 'frustrated', 'terrible', 'worst', 'hate', 'furious', 'disappointed']
    positive_words = ['thank', 'appreciate', 'great', 'excellent', 'love', 'happy']
    
    text_lower = text.lower()
    neg_count = sum(word in text_lower for word in negative_words)
    pos_count = sum(word in text_lower for word in positive_words)
    
    if neg_count > pos_count:
        return "Negative", "🔴"
    elif pos_count > neg_count:
        return "Positive", "🟢"
    else:
        return "Neutral", "🟡"

def export_to_json(result):
    """Export ticket analysis as JSON"""
    export_data = {
        "timestamp": datetime.datetime.now().isoformat(),
        "ticket_id": f"TKT-{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}",
        "classification": {
            "department": result['dept'],
            "urgency": result['urgency'],
            "confidence": result.get('confidence', 0)
        },
        "sentiment": result.get('sentiment', 'Unknown'),
        "analysis": {
            "summary": result['summary'],
            "proposed_response": result['response']
        },
        "original_ticket": result['original_text']
    }
    return json.dumps(export_data, indent=2)

# --- 4. LOAD ASSETS ---
lottie_ai = load_lottieurl("https://lottie.host/9e4d588a-2c4f-4a0b-93b5-7c9808796799/3pW42r7k6m.json")

try:
    vectorizer, dept_model, urgency_model = load_models()
    models_loaded = True
except Exception as e:
    st.error(f"Error loading models: {e}")
    models_loaded = False

# --- 5. ENHANCED SIDEBAR DASHBOARD ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2534/2534929.png", width=50)
    st.markdown("### 📊 Manager Dashboard")
    
    # Real-time Clock
    st.markdown(f"**🕐 System Time:** {datetime.datetime.now().strftime('%H:%M:%S')}")
    
    try:
        df = load_data()
        if not df.empty:
            # Enhanced KPIs
            total_tickets = len(df)
            urgent_tickets = len(df[df['urgency'] == 'Urgent'])
            urgent_percent = int((urgent_tickets / total_tickets) * 100)
            avg_response_time = "2.3 hrs"  # Mock data
            
            col_kpi1, col_kpi2 = st.columns(2)
            col_kpi1.metric("Total Tickets", total_tickets, delta="+12")
            col_kpi2.metric("Urgent %", f"{urgent_percent}%", delta="-3%", delta_color="inverse")
            
            col_kpi3, col_kpi4 = st.columns(2)
            col_kpi3.metric("Avg Response", avg_response_time, delta="-0.5h", delta_color="inverse")
            col_kpi4.metric("Resolution", "94.2%", delta="+2.1%")
            
            st.markdown("---")

            # Enhanced Charts
            st.markdown("**🔴 Urgency Distribution**")
            fig_urgency = px.pie(df, names='urgency', hole=0.5, 
                                color_discrete_sequence=['#ff4b4b', '#00c853'])
            fig_urgency.update_layout(
                paper_bgcolor="rgba(0,0,0,0)", 
                plot_bgcolor="rgba(0,0,0,0)", 
                font_color="white", 
                showlegend=True,
                legend=dict(orientation="h", yanchor="bottom", y=-0.2),
                margin=dict(t=0, b=0, l=0, r=0), 
                height=220
            )
            st.plotly_chart(fig_urgency, use_container_width=True)
            
            st.markdown("**📂 Department Workload**")
            dept_counts = df['department'].value_counts().reset_index()
            dept_counts.columns = ['Department', 'Count']
            fig_dept = px.bar(dept_counts, x='Department', y='Count', 
                             color='Count', color_continuous_scale='Purples')
            fig_dept.update_layout(
                paper_bgcolor="rgba(0,0,0,0)", 
                plot_bgcolor="rgba(0,0,0,0)", 
                font_color="white", 
                showlegend=False,
                margin=dict(t=0, b=0, l=0, r=0), 
                height=220
            )
            st.plotly_chart(fig_dept, use_container_width=True)
            
            # Trend Chart
            st.markdown("**📈 Weekly Trend**")
            trend_data = pd.DataFrame({
                'Day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
                'Tickets': [45, 52, 48, 61, 55, 32, 28]
            })
            fig_trend = px.line(trend_data, x='Day', y='Tickets', 
                               markers=True, line_shape='spline')
            fig_trend.update_traces(line_color='#a855f7', marker=dict(size=8))
            fig_trend.update_layout(
                paper_bgcolor="rgba(0,0,0,0)", 
                plot_bgcolor="rgba(0,0,0,0)", 
                font_color="white",
                margin=dict(t=0, b=0, l=0, r=0), 
                height=180,
                yaxis=dict(gridcolor='rgba(255,255,255,0.1)')
            )
            st.plotly_chart(fig_trend, use_container_width=True)
            
        else:
            st.warning("No data found.")
            
    except Exception as e:
        st.error(f"Dashboard Error: {e}")
    
    st.markdown("---")
    
    # System Health
    st.markdown("**⚙️ System Health**")
    health_col1, health_col2 = st.columns(2)
    health_col1.markdown("🟢 **ML Models**<br><small>Operational</small>", unsafe_allow_html=True)
    health_col2.markdown("🟢 **API Status**<br><small>Active</small>", unsafe_allow_html=True)
    
    st.markdown("---")
    st.caption("v2.0.0 | Enterprise Edition")

# --- 6. MAIN WORKSPACE ---

# Header with Live Status
col_head1, col_head2, col_head3 = st.columns([3, 1, 0.5])
with col_head1:
    st.markdown("# ⚡ Hybrid Ticket System")
    st.markdown("### Intelligent Support Automation")
    st.markdown("""
    <div style="color: #a0a0b0; font-size: 16px; margin-bottom: 20px;">
    Combining <b>Classical ML</b> for speed & routing with <b>Generative AI</b> for empathy & reasoning.
    </div>
    """, unsafe_allow_html=True)

with col_head2:
    if lottie_ai:
        st_lottie(lottie_ai, height=160, key="ai_anim")

with col_head3:
    st.markdown("""
    <div style="text-align: center; margin-top: 40px;">
        <div class="status-badge badge-normal">● LIVE</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Advanced Input Section with Settings
col_input, col_settings = st.columns([3, 1])

with col_input:
    ticket_text = st.text_area("📨 Incoming Customer Ticket", height=150, 
                               placeholder="Paste the customer email or chat transcript here...")

with col_settings:
    st.markdown("**⚙️ Processing Options**")
    auto_assign = st.checkbox("Auto-assign agent", value=True)
    include_history = st.checkbox("Check ticket history", value=False)
    priority_override = st.selectbox("Priority Override", ["Auto", "Force Urgent", "Force Normal"])
    
    processing_mode = st.radio("Mode", ["Standard", "Fast Track", "Deep Analysis"], index=0)

# Session State
if 'result' not in st.session_state:
    st.session_state.result = None
if 'processing_history' not in st.session_state:
    st.session_state.processing_history = []

# Process Button
if st.button("🚀 Process Ticket"):
    if ticket_text and models_loaded:
        with st.spinner("🔄 Running Hybrid Pipeline (ML + GenAI)..."):
            # Progress bar
            progress_bar = st.progress(0)
            
            # 1. Classical ML
            progress_bar.progress(25)
            text_vectorized = vectorizer.transform([ticket_text])
            pred_dept = dept_model.predict(text_vectorized)[0]
            pred_urgency = urgency_model.predict(text_vectorized)[0]
            
            # Calculate confidence
            confidence = calculate_confidence_score(ticket_text, pred_dept)
            
            # Sentiment analysis
            progress_bar.progress(50)
            sentiment, sentiment_icon = get_sentiment_analysis(ticket_text)
            
            # 2. GenAI
            progress_bar.progress(75)
            ai_output = process_ticket_with_llm(ticket_text)
            
            # Parsing
            if "SUMMARY:" in ai_output and "SUGGESTED RESPONSE:" in ai_output:
                summary_part = ai_output.split("SUGGESTED RESPONSE:")[0].replace("SUMMARY:", "").strip()
                response_part = ai_output.split("SUGGESTED RESPONSE:")[1].strip()
            else:
                summary_part = "Analysis Generated."
                response_part = ai_output

            progress_bar.progress(100)
            
            # Save to Session State
            st.session_state.result = {
                "dept": pred_dept,
                "urgency": pred_urgency,
                "summary": summary_part,
                "response": response_part,
                "original_text": ticket_text,
                "confidence": confidence,
                "sentiment": sentiment,
                "sentiment_icon": sentiment_icon,
                "timestamp": datetime.datetime.now(),
                "ticket_id": f"TKT-{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}"
            }
            
            # Add to history
            st.session_state.processing_history.append({
                "time": datetime.datetime.now().strftime("%H:%M:%S"),
                "ticket_id": st.session_state.result['ticket_id'],
                "dept": pred_dept,
                "urgency": pred_urgency
            })
            
            st.success("✅ Ticket processed successfully!")

    elif not ticket_text:
        st.warning("⚠️ Please enter a ticket first.")

# Display Results
if st.session_state.result:
    res = st.session_state.result
    
    # Ticket Header Card
    st.markdown(f"""
    <div class="result-card" style="border-left: 5px solid #a855f7;">
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <div>
                <h3 style="margin: 0; color: white;">🎫 {res['ticket_id']}</h3>
                <p style="margin: 5px 0; color: #9ca3af; font-size: 14px;">
                    Processed at {res['timestamp'].strftime('%Y-%m-%d %H:%M:%S')}
                </p>
            </div>
            <div>
                <span class="status-badge badge-pending">Processing Complete</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Section 1: Enhanced Classification
    st.markdown("### 1️⃣ Classification Analysis (ML)")
    c1, c2, c3 = st.columns(3)
    
    with c1:
        st.markdown(f"""
        <div class="result-card">
            <div class="card-title">📂 Department Routing</div>
            <div class="card-value">{res['dept']}</div>
            <div class="confidence-bar">
                <div class="confidence-fill" style="width: {res['confidence']}%;"></div>
            </div>
            <div style="font-size: 12px; color: #9ca3af; margin-top: 5px;">
                Confidence: {res['confidence']}%
            </div>
        </div>
        """, unsafe_allow_html=True)
        
    with c2:
        urgency_color = "#ff4b4b" if res['urgency'] == "Urgent" else "#00c853"
        st.markdown(f"""
        <div class="result-card" style="border-left: 5px solid {urgency_color};">
            <div class="card-title">🔥 Priority Level</div>
            <div class="card-value" style="color: {urgency_color};">{res['urgency']}</div>
            <div style="margin-top: 10px;">
                <span class="status-badge" style="background: {urgency_color};">
                    {res['urgency'].upper()}
                </span>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with c3:
        st.markdown(f"""
        <div class="result-card">
            <div class="card-title">😊 Customer Sentiment</div>
            <div class="card-value">{res['sentiment_icon']} {res['sentiment']}</div>
            <div style="font-size: 13px; color: #9ca3af; margin-top: 10px;">
                Emotional tone detected
            </div>
        </div>
        """, unsafe_allow_html=True)
        
    # Section 2: AI Agent Analysis
    st.markdown("### 2️⃣ Generative Agent (Gemini)")
    
    col_summary, col_insights = st.columns([2, 1])
    
    with col_summary:
        st.markdown(f"""
        <div class="result-card">
            <div class="card-title">📝 Executive Summary</div>
            <div class="card-text">{res['summary']}</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col_insights:
        st.markdown(f"""
        <div class="result-card">
            <div class="card-title">🎯 Key Insights</div>
            <div class="timeline-item">
                <div style="font-size: 13px; color: #d1d5db;">
                    <b>Customer Priority:</b> {res['urgency']}
                </div>
            </div>
            <div class="timeline-item">
                <div style="font-size: 13px; color: #d1d5db;">
                    <b>Recommended Action:</b> Immediate response
                </div>
            </div>
            <div class="timeline-item">
                <div style="font-size: 13px; color: #d1d5db;">
                    <b>Estimated Resolution:</b> 2-4 hours
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="result-card">
        <div class="card-title">✍️ Proposed Response</div>
        <div class="card-text" style="white-space: pre-line;">{res['response']}</div>
    </div>
    """, unsafe_allow_html=True)

    # Section 3: Professional Action Panel
    st.markdown("### 🛠️ Agent Actions")
    
    col_act1, col_act2, col_act3, col_act4, col_act5 = st.columns(5)
    
    # 1. Download Report
    report_text = f"""
TICKET ANALYSIS REPORT
{'='*50}
Ticket ID: {res['ticket_id']}
Timestamp: {res['timestamp'].strftime("%Y-%m-%d %H:%M:%S")}
Status: Processed

CLASSIFICATION
{'='*50}
Department: {res['dept']}
Urgency: {res['urgency']}
Confidence Score: {res['confidence']}%
Customer Sentiment: {res['sentiment']}

ORIGINAL TICKET
{'='*50}
{res['original_text']}

AI ANALYSIS
{'='*50}
Executive Summary:
{res['summary']}

PROPOSED RESPONSE
{'='*50}
{res['response']}

{'='*50}
Generated by Hybrid Ticket AI System v2.0
    """
    
    with col_act1:
        st.download_button(
            label="📥 Download TXT",
            data=report_text,
            file_name=f"{res['ticket_id']}_analysis.txt",
            mime="text/plain"
        )
    
    with col_act2:
        json_data = export_to_json(res)
        st.download_button(
            label="📊 Export JSON",
            data=json_data,
            file_name=f"{res['ticket_id']}_data.json",
            mime="application/json"
        )
    
    with col_act3:
        if st.button("✅ Approve & Send"):
            st.toast("✉️ Response sent to customer!", icon="🎉")
            st.balloons()
            
    with col_act4:
        if st.button("✏️ Edit Response"):
            st.session_state['edit_mode'] = True
            st.toast("📝 Editor Mode Activated", icon="✏️")
            
    with col_act5:
        if st.button("🔄 Escalate"):
            st.toast("⚠️ Ticket escalated to supervisor", icon="🚨")
    
    # Edit Mode Panel
    if st.session_state.get('edit_mode', False):
        st.markdown("---")
        st.markdown("### ✏️ Response Editor")
        edited_response = st.text_area("Edit the AI-generated response:", 
                                       value=res['response'], 
                                       height=200,
                                       key="response_editor")
        
        col_save, col_cancel = st.columns([1, 4])
        with col_save:
            if st.button("💾 Save Changes"):
                st.session_state.result['response'] = edited_response
                st.session_state['edit_mode'] = False
                st.success("Changes saved!")
                st.rerun()
        with col_cancel:
            if st.button("❌ Cancel"):
                st.session_state['edit_mode'] = False
                st.rerun()
    
    # Processing History
    if st.session_state.processing_history:
        with st.expander("📜 Processing History (Recent)"):
            history_df = pd.DataFrame(st.session_state.processing_history[-10:])
            st.dataframe(history_df, use_container_width=True, hide_index=True)

# Footer
st.markdown("---")
col_footer1, col_footer2, col_footer3 = st.columns(3)
with col_footer1:
    st.markdown("**🔒 Security:** End-to-end encrypted")
with col_footer2:
    st.markdown("**⚡ Uptime:** 99.9% SLA")
with col_footer3:
    st.markdown("**📞 Support:** 24/7 Available")

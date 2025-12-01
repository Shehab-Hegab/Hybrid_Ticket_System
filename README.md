
<div align="center">

# ⚡ Hybrid Ticket AI
### Enterprise Intelligent Support Automation

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Enterprise_UI-ff4b4b?style=for-the-badge&logo=streamlit&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/ML-Scikit_Learn-orange?style=for-the-badge&logo=scikitlearn&logoColor=white)
![Gemini](https://img.shields.io/badge/GenAI-Google_Gemini-4285F4?style=for-the-badge&logo=google&logoColor=white)
![Status](https://img.shields.io/badge/Status-Production_Ready-success?style=for-the-badge)

<br />

**A Next-Gen Customer Support System combining the speed of Classical Machine Learning with the empathy and reasoning of Large Language Models (LLMs).**

[View Demo](#-interface-showcase) • [Installation](#%EF%B8%8F-installation--setup) • [Architecture](#-technical-architecture) • [Features](#-key-enterprise-features)

</div>

---

## 🖼️ Project Overview

**Hybrid Ticket AI** is a full-stack data science solution designed to optimize customer support workflows for high-volume SaaS environments. It solves the classic "Cost vs. Quality" trade-off in AI automation by utilizing a **Hybrid Architecture**:

1.  **The "Fast Brain" (Classical ML):** Instantly routes tickets and flags urgency using Logistic Regression (Zero latency, Zero cost).
2.  **The "Smart Brain" (GenAI):** Drafts human-like responses, summarizes issues, and analyzes sentiment using Google Gemini (High reasoning, Empathy).

This project features a **Production-Grade Dashboard** with real-time analytics, simulating a professional environment used by modern enterprises.

---

## 📸 Interface Showcase

### 1. The Intelligent Workspace
> *Real-time analysis, ML Classification, Sentiment Detection, and AI Drafting.*

<img width="1800" height="587" alt="image" src="https://github.com/user-attachments/assets/dcf2161c-acc2-47ba-8d17-f7de227f6c71" />

![Main Workspace](https://github.com/user-attachments/assets/c1b5fb58-63e6-4854-a76a-1b3b57e6b1c0)

### 2. Manager Analytics & Insights
> *Live KPI monitoring, Department Workload distribution, and Weekly Trend Analysis.*

| **Manager Sidebar** | **Department Analytics** |
|:---:|:---:|
| <img src="https://github.com/user-attachments/assets/089a1965-0e42-4570-a7f3-3373be1a7126" width="300"> | <img src="https://github.com/user-attachments/assets/aa83c807-eb65-4648-946f-d5707e7bae03" width="500"> |

### 3. Workflow & History
> *Input processing options and session-based ticket history tracking.*

![History](https://github.com/user-attachments/assets/89a207a4-9fc0-48aa-8308-f1b25e5992c4)

---

## 🚀 Key Enterprise Features

### 📊 Advanced Analytics Dashboard
*   **Real-time KPIs:** Tracks Total Tickets, Urgent %, and Average Resolution metrics.
*   **Weekly Trend Analysis:** Visualizes ticket volume trends over time with spline interpolation.
*   **Department Workload:** Color-coded visualizations showing volume per department (Billing, Technical, Product).
*   **System Health:** Live monitoring of ML Model status and API latency.

### 🧠 Intelligent Processing Engine
*   **Confidence Scoring:** Displays ML model certainty (e.g., *98.4% Confidence*) to aid human decision-making.
*   **Sentiment Analysis:** Detects customer emotional tone (Neutral, Frustrated, Happy) to prioritize at-risk customers.
*   **Hybrid Routing:** Auto-classifies tickets into departments (e.g., Refund Request, Cancellation, Technical Issue).

### 🛠️ Agent Productivity Tools
*   **Smart Drafting:** Generates polite, context-aware email responses instantly.
*   **Executive Summaries:** Compresses long complaints into one-sentence insights.
*   **Export Capabilities:** Download reports in **.TXT** (for documentation) or **.JSON** (for API integration).
*   **Ticket History:** Session-based tracking of recently processed tickets.

---

## 🏗️ Technical Architecture
```mermaid

graph LR
    A[Customer Ticket] --> B{Hybrid System}
    B -->|Path 1: Speed| C[Classical ML Model]
    C --> D[Predict Department]
    C --> E[Predict Urgency]
    
    B -->|Path 2: Intelligence| F[Google Gemini LLM]
    F --> G[Summarize Issue]
    F --> H[Draft Response]
    F --> I[Analyze Sentiment]
    
    D & E & G & H & I --> J[Streamlit Enterprise UI]
🛠️ Installation & Setup
1. Clone the Repository
code
Bash
download
content_copy
expand_less
git clone https://github.com/Shehab-Hegab/Hybrid_Ticket_System.git
cd Hybrid_Ticket_System
2. Install Dependencies
code
Bash
download
content_copy
expand_less
pip install -r requirements.txt
3. Setup Environment Variables

Get a free API Key from Google AI Studio.

Open llm_module.py and paste your key into the API_KEY variable.

4. Run the Application
code
Bash
download
content_copy
expand_less
streamlit run app.py
📂 Project Structure
code
Bash
download
content_copy
expand_less
├── app.py                 # Main Application (Streamlit Enterprise UI)
├── train_models.py        # ML Pipeline: Data cleaning, TF-IDF, Model Training
├── llm_module.py          # GenAI Integration (Gemini API Handler)
├── clean_data.py          # ETL Script for raw dataset processing
├── tickets.csv            # Processed Dataset (used for Dashboard Analytics)
├── models/                # Serialized ML Models (.pkl files)
└── requirements.txt       # Project dependencies
💡 Why "Hybrid" AI?

In a professional setting, relying solely on LLMs (like GPT-4) for every task is inefficient and costly.

Feature	Classical ML (Scikit-Learn)	Generative AI (Gemini/GPT)
Speed	⚡ Instant (< 0.01s)	🐢 Slower (~2-5s)
Cost	💸 Free / Low Compute	💰 Per-token Cost
Best For	Routing, Tagging, Spam Detection	Drafting, Summarizing, Empathy

This project demonstrates the ability to engineer cost-effective, scalable AI solutions by combining the strengths of both approaches.

🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

📄 License

This project is licensed under the MIT License.

<div align="center">
<br />
Made with ❤️ by <a href="https://github.com/Shehab-Hegab">Shehab Hegab</a>
</div>
```

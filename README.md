
# ⚡ Hybrid Ticket AI | Enterprise Support Automation

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Enterprise%20UI-ff4b4b)
![ML](https://img.shields.io/badge/ML-Scikit--Learn-orange)
![GenAI](https://img.shields.io/badge/GenAI-Google%20Gemini-4285F4)
![Status](https://img.shields.io/badge/Status-Production%20Ready-success)

> **A Next-Gen Customer Support System combining the speed of Classical Machine Learning with the empathy and reasoning of Large Language Models (LLMs).**

---

## 🖼️ Project Overview

**Hybrid Ticket AI** is a full-stack data science solution designed to optimize customer support workflows. It solves the "Cost vs. Quality" trade-off by using a **Hybrid Architecture**:

1.  **The "Fast Brain" (Classical ML):** Instantly routes tickets and flags urgency using Logistic Regression (Zero latency, Zero cost).
2.  **The "Smart Brain" (GenAI):** Drafts human-like responses, summarizes issues, and analyzes sentiment using Google Gemini (High reasoning, Empathy).

This project features a **Production-Grade Dashboard** with real-time analytics, mimicking a real SaaS environment used by Fortune 500 companies.

---

## 🚀 Key Enterprise Features

### 📊 1. Advanced Analytics Dashboard
*   **Real-time KPIs:** Tracks Total Tickets, Urgent %, Average Response Time, and Resolution Rate.
*   **Weekly Trend Analysis:** Visualizes ticket volume trends over time.
*   **Department Workload:** Color-coded bar charts showing volume per department (Billing, Technical, Product).
*   **System Health:** Live monitoring of ML Model status and API latency.

### 🧠 2. Intelligent Processing Engine
*   **Confidence Scoring:** Displays the ML model's certainty (e.g., *98.4% Confidence*) to aid human decision-making.
*   **Sentiment Analysis:** Detects customer emotional tone (Neutral, Frustrated, Happy) to prioritize angry customers.
*   **Hybrid Routing:** Auto-classifies tickets into departments (e.g., Refund Request, Cancellation, Technical Issue).

### 🛠️ 3. Agent Productivity Tools
*   **Smart Drafting:** Generates polite, context-aware email responses instantly.
*   **Executive Summaries:** Compresses long complaints into one-sentence insights.
*   **Export Capabilities:** Download reports in **.TXT** (for logs) or **.JSON** (for API integration).
*   **Ticket History:** Session-based tracking of the last 10 processed tickets.

---

## 📸 Interface Screenshots

### **1. The Agent Workspace**
*Real-time analysis, sentiment detection, and AI drafting.*
![Agent Workspace](insert_your_screenshot_1_here.png)

### **2. The Analytics Dashboard**
*Manager view with KPIs, trend lines, and dark-mode visualizations.*
![Dashboard View](insert_your_screenshot_2_here.png)

*(Note: Replace the text above with your actual screenshots after uploading them to GitHub)*

---

## 🏗️ Technical Architecture


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

Clone the Repository

code
Bash
download
content_copy
expand_less
git clone https://github.com/yourusername/hybrid-ticket-ai.git
cd hybrid-ticket-ai

Install Dependencies

code
Bash
download
content_copy
expand_less
pip install -r requirements.txt

Setup Environment Variables

Get a free API Key from Google AI Studio.

Add it to llm_module.py or create a .env file.

Run the Application

code
Bash
download
content_copy
expand_less
streamlit run app.py
📂 Project Structure
code
Code
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

In a professional setting, using GPT-4 for everything is too slow and expensive.

Classical ML (Scikit-Learn) handles the "Routing" task in 0.01 seconds for free.

LLMs (Gemini) handle the "Writing" task where human nuance is needed.

This project demonstrates the ability to engineer cost-effective, scalable AI solutions.

🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

📄 License

This project is licensed under the MIT License.

code
Code
download
content_copy
expand_less
### **How to add your Screenshots:**
1.  Take screenshots of your App (The Dashboard view and the Analysis view).
2.  Save them as images (e.g., `dashboard.png`, `workspace.png`).
3.  Upload your project to GitHub.
4.  Upload the images to your GitHub repository (you can drag and drop them into the file list on the website).
5.  Click on the image on GitHub to get its **URL**.
6.  Edit the `README.md` and replace `insert_your_screenshot_1_here.png` with that URL.


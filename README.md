# 🛡️ Log-Sentinel

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://nomaanos-log-sentinel.streamlit.app/)

An **AI-Powered Security Log & SIEM Anomaly Threat Analyzer** engineered to parse server access, authentication, and firewall logs to detect active cyber threats and generate automated incident response reports.

Developed by **[NomaanOS-Dev](https://github.com/NomaanOS-Dev)**.

---

## 🚀 Key Features

* **Log Pattern Analyzer:** Automated detection for SSH brute-force attempts, SQL Injection payloads, HTTP errors, and unauthorized shell commands.
* **Metric Summarization:** Extracts threat indicators and unique malicious IPs from raw log data.
* **AI Incident Responder:** Leverages OpenAI `gpt-4o-mini` to evaluate incident severity and generate actionable SOC mitigation strategies.
* **Flexible Input:** Supports live paste or direct log file uploads (`.log`, `.txt`).

---

## 🛠️ Tech Stack

* **Language:** Python 3.x
* **AI Engine:** OpenAI `gpt-4o-mini` & LangChain Core
* **UI Framework:** Streamlit
* **Parsing Engine:** Regex Security Heuristics

---

## 📦 Local Installation & Setup

1. **Clone Repository:**
   ```bash
   git clone [https://github.com/NomaanOS-Dev/Log-Sentinel.git](https://github.com/NomaanOS-Dev/Log-Sentinel.git)
   cd Log-Sentinel
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run Application:**
   ```bash
   streamlit run app.py
   ```

---

## 🛡️ License
Open-source SIEM log analysis utility built for security research and demonstration.

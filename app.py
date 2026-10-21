import os
import streamlit as st
from analyzer import LogAnalyzer
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

st.set_page_config(page_title="Log Sentinel", page_icon="🛡️", layout="wide")

st.title("🛡️ Log Sentinel - AI SIEM & Threat Analyzer")
st.caption("Automated Log Parsing & AI-Driven Security Incident Response | Built by NomaanOS-Dev")

openai_api_key = st.sidebar.text_input("OpenAI API Key", type="password")

st.sidebar.markdown("---")
st.sidebar.info("Upload server authentication, firewall, or web server logs for automated threat detection.")

uploaded_file = st.file_uploader("Upload Log File (log, txt)", type=["log", "txt"])

log_data = ""
if uploaded_file:
    log_data = uploaded_file.getvalue().decode("utf-8", errors="ignore")
else:
    log_data = st.text_area("Or Paste Security Logs Directly Here:", height=200, placeholder="Paste auth.log, access.log or syslog content...")

if log_data:
    st.subheader("📄 Log Data Preview")
    st.code(log_data[:1000] + ("..." if len(log_data) > 1000 else ""), language="text")
    
    analyzer = LogAnalyzer()
    findings = analyzer.scan_log(log_data)
    
    st.markdown("---")
    st.markdown("### 🔍 Threat Detection Findings")
    
    if findings:
        cols = st.columns(len(findings))
        for idx, (cat, val) in enumerate(findings.items()):
            cols[idx % len(cols)].metric(label=cat, value=val["count"])
            
        for cat, val in findings.items():
            with st.expander(f"View Details: {cat}"):
                st.write(val["samples"])
    else:
        st.success("No known malicious threat signatures found in the provided log snippet.")

    if openai_api_key:
        st.markdown("---")
        st.markdown("### 🤖 AI Incident Response Generator")
        if st.button("Generate Incident Analysis Report"):
            with st.spinner("Analyzing threat patterns and log anomalies using GPT-4o-mini..."):
                os.environ["OPENAI_API_KEY"] = openai_api_key
                
                prompt_template = (
                    "You are a Lead SOC Analyst & Incident Responder.\n"
                    "Analyze the following security log findings and raw log context.\n"
                    "Provide an Executive Incident Summary, Assess Threat Severity (Low/Medium/High/Critical), and detail Actionable Mitigation Steps.\n\n"
                    "Findings: {findings}\n\n"
                    "Log Excerpt:\n{log_excerpt}"
                )
                
                prompt = ChatPromptTemplate.from_template(prompt_template)
                llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
                chain = prompt | llm | StrOutputParser()
                
                report = chain.invoke({"findings": str(findings), "log_excerpt": log_data[:2000]})
                st.write(report)
    else:
        st.info("💡 Enter your OpenAI API Key in the sidebar to generate AI Incident Response Reports.")
else:
    st.info("👈 Upload a log file or paste text above to begin SIEM log analysis.")

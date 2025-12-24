import streamlit as st
import requests
import pandas as pd

st.set_page_config(page_title="AI Agent Dashboard", layout="wide")
st.title("🤖 Multi-Agent Chatbot Dashboard")

# Chat Section
st.header("💬 Chat with the Multi-Agent System")
user_input = st.text_input("Enter your question:")

if st.button("Send"):
    try:
        response = requests.post("http://127.0.0.1:5000/chat", json={"message": user_input}).json()
        st.success("**Bot:** " + response["response"])
        st.subheader("Agent Metrics (latest interaction)")
        st.json(response["metrics"])
    except Exception as e:
        st.error(f"Error connecting to backend: {e}")

# Metrics Dashboard
st.header("📊 Agent Performance Metrics")

if st.button("Refresh Metrics"):
    try:
        data = requests.get("http://127.0.0.1:5000/metrics").json()
        if isinstance(data, list) and len(data) > 0:
            df = pd.DataFrame(data, columns=["id", "agent_name", "time_taken", "cost", "accuracy", "efficiency", "created_at"])
            st.dataframe(df)
        else:
            st.warning("No metrics found in database.")
    except Exception as e:
        st.error(f"Error fetching metrics: {e}")

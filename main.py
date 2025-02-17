import streamlit as st
import os
from dotenv import load_dotenv
from utils.advisor import FinancialAdvisor

# Load environment variables
load_dotenv()

# Initialize session state
if 'messages' not in st.session_state:
    st.session_state.messages = []

def initialize_advisor():
    """Initialize the FinancialAdvisor instance"""
    return FinancialAdvisor(openai_api_key=os.getenv('OPENAI_API_KEY'))

def main():
    st.title("🤖 AI Financial Advisor")
    
    # Initialize advisor
    advisor = initialize_advisor()

    # Sidebar for user information
    with st.sidebar:
        st.header("Your Financial Profile")
        income = st.number_input("Monthly Income ($)", min_value=0)
        expenses = st.number_input("Monthly Expenses ($)", min_value=0)
        risk_tolerance = st.select_slider(
            "Risk Tolerance",
            options=["Low", "Medium", "High"]
        )

    # Chat interface
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Ask me about your finances..."):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Get AI response
        with st.chat_message("assistant"):
            response = advisor.get_advice(prompt)
            st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})

if __name__ == "__main__":
    main()
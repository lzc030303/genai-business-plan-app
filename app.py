import streamlit as st
from genai_core import generate_business_plan

st.set_page_config(page_title="Startup Co-Founder AI")

st.title("💡 Startup Co-Founder Assistant")
st.write("Generate startup insights using GenAI!")

idea = st.text_input("Enter your startup idea:")

mode = st.selectbox("What do you want to generate?", [
    "💼 Full Business Plan",
    "📛 Startup Name Ideas",
    "📊 Competitor Analysis",
    "💡 Feature Suggestions",
    "💰 Monetization Strategy"
])

def build_prompt(idea, mode):
    if mode == "💼 Full Business Plan":
        return f"""You are a startup consultant. Based on the idea: "{idea}", write a full business plan including:
- Problem
- Target Market
- Unique Value
- Monetization
- Go-to-Market"""
    elif mode == "📛 Startup Name Ideas":
        return f"Suggest 5 creative and relevant startup names for this idea: \"{idea}\"."
    elif mode == "📊 Competitor Analysis":
        return f"What companies already exist in this space: \"{idea}\"? Give a brief analysis."
    elif mode == "💡 Feature Suggestions":
        return f"List 5 MVP features for a product based on: \"{idea}\"."
    elif mode == "💰 Monetization Strategy":
        return f"Suggest 3 ways to make money from thi

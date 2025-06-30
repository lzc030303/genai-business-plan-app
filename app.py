import streamlit as st
from genai_core import generate_business_plan

st.title("🚀 Startup Idea Generator")

idea = st.text_input("Enter your startup idea")

mode = st.selectbox(
    "Choose what you want to generate:",
    [
        "💼 Full Business Plan",
        "📛 Startup Name Ideas",
        "📊 Competitor Analysis",
        "💡 Feature Suggestions",
        "💰 Monetization Strategy"
    ]
)

if st.button("Generate"):
    if idea:
        with st.spinner("Generating..."):
            prompt = ""

            if "Full Business Plan" in mode:
                prompt = f"Write a detailed business plan for this idea: {idea}"
            elif "Startup Name" in mode:
                prompt = f"Suggest 10 creative startup names for this idea: {idea}"
            elif "Competitor Analysis" in mode:
                prompt = f"Give a competitor analysis for this idea: {idea}"
            elif "Feature Suggestions" in mode:
                prompt = f"List the most important features to include for: {idea}"
            elif "Monetization Strategy" in mode:
                prompt = f"Suggest 3 ways to make money from this idea: {idea}"

            result = generate_business_plan(prompt)
            st.markdown("### Result")
            st.write(result)
    else:
        st.warning("Please enter your startup idea above.")


import streamlit as st 
import time
import google.generativeai as genai

# Animated text function
def animated_text(text, speed=0.05):
    placeholder = st.empty()
    displayed_text = ""
    for letter in text:
        displayed_text += letter
        placeholder.markdown(f"""
            <h1 style="text-align:center; color: #FF4500;">🚀{displayed_text}</h1>
        """, unsafe_allow_html=True)
        time.sleep(speed)

# Display animated text
animated_text("Welcome to GenAI Code Reviewer!", speed=0.1)

# Set up Google Gemini API Key
genai.configure(api_key="AIzaSyBm0GOvYox4OyRG1WFOK7FT5fnNCHfubns")

# Streamlit App Title
st.title("🤖 AI-Powered Code Debugging")

# Text Area for User Input (Buggy Code)
buggy_code = st.text_area("🐞 Enter your buggy code here:", height=200)

# Function to Debug Code Using Gemini AI
def debug_code_with_gemini(code):
    prompt = f"Debug the following code and provide the corrected version:\n\n{code}"
    model = genai.GenerativeModel("models/gemini-2.0-flash")
    response = model.generate_content(prompt)
    return response.text if response.text else "⚠️ Error in AI response."

# Function to Generate Code Improvement Suggestions
def get_suggestions_with_gemini(code):
    prompt = f"Suggest improvements for the following code, focusing on best practices, performance optimization, and readability:\n\n{code}"
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)
    return response.text if response.text else "⚠️ No suggestions available."

# Generate Button
if st.button("🚀 Analyze & Optimize Code"):
    if buggy_code:
        with st.spinner("🛠️ Debugging your code..."):
            fixed_code = debug_code_with_gemini(buggy_code)
        
        with st.spinner("🔍 Generating suggestions..."):
            suggestions = get_suggestions_with_gemini(fixed_code)
        
        # Display Fixed Code
        st.subheader("✅ Fixed Code:")
        st.code(fixed_code, language="python")
        
        # Copy Button for Fixed Code
        st.download_button(
            label="📋 Copy Fixed Code",
            data=fixed_code,
            file_name="fixed_code.py",
            mime="text/plain"
        )
        
        # Display AI-Generated Suggestions
        st.subheader("💡 Suggestions for Improvement:")
        st.write(suggestions)
    else:
        st.warning("⚠️ Please enter some code before generating fixes and suggestions!")

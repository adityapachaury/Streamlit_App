import streamlit as st #UI design
import os
from dotenv import load_dotenv # package to get the env variables load into the application
load_dotenv()

import google.generativeai as genai


#genai configuration of API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

#intalling the model
model = genai.GenerativeModel('gemini-pro')

#define a function to generate the response from llm
def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text

#setting up Streamlit app
st.set_page_config(
    page_title="gemini-pro",
    layout="wide",
    initial_sidebar_state="expanded"
)

#setting up header
st.header("Gemini Q & A App")

# Initialize session state for history
if 'history' not in st.session_state:
    st.session_state.history = []

# Sidebar for history
with st.sidebar:
    st.header("Conversation History")
    for i, (question, response) in enumerate(st.session_state.history):
        st.write(f"**You:** {question}")
        st.write(f"**Gemini:** {response}")

#input
question = st.text_input("Ask your Question")

#submit
if st.button("Submit your Question"):
    response = get_gemini_response(question)
    st.write("**You:**", question)
    st.write("**Gemini:**", response)

    # Append to history
    st.session_state.history.append((question, response))

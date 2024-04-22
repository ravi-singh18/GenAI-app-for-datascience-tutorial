import streamlit as st

import google.generativeai as genai




f = open(r"C:\Users\errav\genai\gemini_api\gem_api_key.txt")
gem_api_key = f.read()
genai.configure(api_key=gem_api_key)

st.title("Data Science and Python Tutorial AI")
st.subheader("Learn Data Science and also you can ask for python code")

model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                               system_instruction="""You are a friendly and helpful AI Teaching Assistant and python code generator related to Data Science.
                         Given an answer for the user query when it is related datascience topic or python for data science otherwise tell I don't know if user and say Hi then say Hi, How can I assist you.""")

# Check for messages in session 
if "messages" not in st.session_state.keys():
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello,AI bot here how can I help you today?"}
    ]
    

# Display all messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])
# Receive user input
user_input = st.chat_input()

# Store user input in session
if user_input is not None:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)
# Generate AI response and display
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Loading..."):
            ai_response = model.generate_content(user_input)
            st.write(ai_response.text)
    new_ai_message = {"role": "assistant", "content": ai_response.text}
    st.session_state.messages.append(new_ai_message)
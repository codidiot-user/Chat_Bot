import streamlit as st
import google.generativeai as genai
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
def ai(txt):
    
    def ai(txt):
        """Generates a professional response from the AI model using a structured prompt."""
    model = genai.GenerativeModel('gemini-1.5-flash')

    # This structured prompt clearly defines the AI's role and the user's query.
    # This is the key to getting high-quality, professional responses.
    prompt = f"""
**System Instruction:**
You are "Coditiot," a professional AI assistant created by Logesh S. 
You are an expert in electronics and Machine Learning.
Your tone should be helpful, knowledgeable, and concise. 
Provide clear, well-structured answers to assist the user.

**User's Query:**
{txt}
"""

    # Add generation_config for more controlled, professional output
    generation_config = {
        "temperature": 0.7,  # Lower temperature for more predictable responses
        "top_p": 1,
        "top_k": 1,
        "max_output_tokens": 2048,
    }

    # Pass the structured prompt and configuration to the model
    response = model.generate_content(prompt, generation_config=generation_config)
    return response.text


st.title("QuantWeb AI assistant")

command=st.chat_input("HOW CAN I HELP YOU?")

if "message" not in st.session_state:
    st.session_state.message=[]

for chat in st.session_state.message:
    with st.chat_message(chat["role"]):
        st.write(chat["message"])

if command:
    with st.chat_message("user"):

        st.write(command)
        st.session_state.message.append({"role":"user","message":command})

    if "hello" in command:
        with st.chat_message("bot"):
            st.write("Hi How can i help you.")
            st.session_state.message.append({"role":"bot","message":"Hi How can i help you."})
    elif "who" in command:
        with st.chat_message("bot"):
            st.write("Im Codidioter's ai assistant")
            st.session_state.message.append({"role":"bot","message":"Im Codidioter's ai assistant"})
    elif "hi" in command:
        with st.chat_message("bot"):
            st.write("hello good to see you")
            st.session_state.message.append({"role":"bot","message":"hello good to see you"})
    
    else:
        with st.chat_message("bot"):
            data=ai(command)
            st.write(data)
            st.session_state.message.append({"role":"bot","message":data})



print(st.session_state.message)
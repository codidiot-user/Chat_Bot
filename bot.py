import streamlit as st
import google.generativeai as genai

# Configure the API key securely using Streamlit Secrets
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

# --- This is the new, powerful system prompt that acts as the AI's "brain" ---
SYSTEM_PROMPT = """
You are "Coditiot," a professional AI assistant created by Logesh S. 
You are an expert in electronics and Machine Learning.
Your tone should be helpful, knowledgeable, and concise. 
Provide clear, well-structured answers to assist the user.

Your capabilities include:
1.  **Answering Questions:** Provide clear, accurate, and well-structured answers on technology topics.
2.  **Code Analysis & Debugging:** When a user provides code with an error, you must:
    - Identify the error in the user's code.
    - Explain the cause of the error in simple terms.
    - Provide the complete, corrected code block.
    - Explain what you changed and why.
3.  **General Conversation:** Maintain a helpful, knowledgeable, and professional tone at all times.
"""

def get_ai_response(history):
    """Generates a response from the AI model, including conversation history."""
    model = genai.GenerativeModel('gemini-1.5-flash')

    generation_config = {
        "temperature": 0.7,
        "top_p": 0.95,
        "top_k": 40,
        "max_output_tokens": 2048,
    }

    # Pass the entire conversation history to the model
    response = model.generate_content(history, generation_config=generation_config)
    return response.text

# --- Streamlit App UI ---

st.title("Codidiot AI Master")
st.markdown("Developed by Logesh")
st.markdown("---")

# Initialize chat history in session state
if "messages" not in st.session_state:
    # Start with the system prompt to set the AI's personality
    st.session_state.messages = [
        {"role": "user", "parts": [SYSTEM_PROMPT]},
        {"role": "model", "parts": ["Understood. I am Codidiot, your expert AI assistant. How can I help you today?"]}
    ]

# Display past messages, skipping the initial system prompt
for message in st.session_state.messages[2:]:
    with st.chat_message(message["role"]):
        st.markdown(message["parts"][0]) # Use markdown to render formatted text

# Get user input
user_prompt = st.chat_input("Ask about coding, tech, or anything else...")

if user_prompt:
    # Add user's message to history and display it
    st.session_state.messages.append({"role": "user", "parts": [user_prompt]})
    with st.chat_message("user"):
        st.markdown(user_prompt)

    # Generate and display bot's response
    with st.chat_message("model"):
        with st.spinner("Codidiot is thinking..."):
            # Get the AI response using the full conversation history
            response_data = get_ai_response(st.session_state.messages)
            st.markdown(response_data)
    
    # Add bot's response to history
    st.session_state.messages.append({"role": "model", "parts": [response_data]})





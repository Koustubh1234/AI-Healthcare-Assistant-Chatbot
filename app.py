import streamlit as st
import re
from transformers import AutoModelForCausalLM, AutoTokenizer
from streamlit_chat import message  # For chat UI

# Set page configuration (MUST be the first Streamlit command)
st.set_page_config(page_title="Healthcare AI Chatbot", page_icon="🩺", layout="wide")

# Load BioGPT Model and Tokenizer
@st.cache_resource
def load_model():
    model_name = "microsoft/biogpt"  # Using BioGPT instead of BioGPT-Large
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
    return tokenizer, model

tokenizer, model = load_model()

# Define Chatbot Function with Predefined Responses
def healthcare_chatbot(user_input):
    user_input = user_input.lower()

    # Predefined Responses
    if "hi" in user_input or "hello" in user_input:
        return "Hello! How can I assist you today? 😊"
    elif "bye" in user_input:
        return "Goodbye! Take care and stay healthy. 👋"
    elif "symptoms of cold" in user_input:
        return "Common symptoms of cold include sneezing, runny nose, sore throat, and mild fever. 🤧"
    elif "symptoms of covid" in user_input:
        return "COVID-19 symptoms include fever, cough, difficulty breathing, and loss of taste or smell. Please consult a doctor if needed. 🏥"
    elif "appointment" in user_input:
        return "Would you like to schedule an appointment with the doctor? 📅"
    elif "medication for cold" in user_input:
        return "For a common cold, take rest, drink warm fluids, and consider over-the-counter medicines like paracetamol. Always consult a doctor. 💊"
    elif "medication for fever" in user_input:
        return "For fever, you may take paracetamol and stay hydrated. If fever persists, consult a doctor. 🔥"
    
    # Improved Prompting for AI Response
    prompt = f"answer for given inpt from AI health care assistant is: {user_input}"
    inputs = tokenizer(prompt, return_tensors="pt")
    output = model.generate(**inputs, max_length=200, num_return_sequences=1)
    response = tokenizer.decode(output[0], skip_special_tokens=True)

    # Remove any extra unwanted symbols or tags
    response = re.sub(r"<[^>]+>", "", response)  # Removes XML-like tags
    response = response.strip()  # Clean up any extra spaces

    return response

# Streamlit UI Setup
st.title("💬 Healthcare Assistant Chatbot")
st.markdown("""
    <h3 style='color: #2b8a3e;'>Your AI-powered health assistant. 🌿</h3>
    <p style='font-size:18px;'>Ask me anything about symptoms, medications, and appointments.</p>
""", unsafe_allow_html=True)

# Custom Styling
st.markdown("""
    <style>
        .chat-container {
            background-color: #e3f2fd;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 5px 5px 15px rgba(0,0,0,0.2);
        }
        .user-message {
            background-color: #0078ff;
            color: white;
            padding: 10px;
            border-radius: 10px;
            max-width: 70%;
        }
        .bot-message {
            background-color: #81c784;
            padding: 10px;
            border-radius: 10px;
            max-width: 70%;
        }
        .stButton > button {
            background-color: #2b8a3e;
            color: white;
            font-size: 16px;
            padding: 10px 20px;
            border-radius: 8px;
        }
    </style>
""", unsafe_allow_html=True)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Chat Interface
user_input = st.text_input("💬 Type your query here...", key="user_input")
if st.button("Submit", key="submit_button"):
    if user_input:
        st.session_state["messages"].append(("user", user_input))
        response = healthcare_chatbot(user_input)
        st.session_state["messages"].append(("bot", response))

# Display Chat History
st.subheader("📜 Chat History")
for idx, (sender, msg) in enumerate(st.session_state["messages"]):
    if sender == "user":
        message(msg, is_user=True, avatar_style="thumbs", key=f"user_{idx}")
    else:
        message(msg, is_user=False, avatar_style="bottts", key=f"bot_{idx}")

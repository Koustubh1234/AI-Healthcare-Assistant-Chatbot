# AI-Healthcare-Assistant-Chatbot
# 🏥 AI Healthcare Assistant Chatbot

## 📌 Project Overview
The **AI Healthcare Assistant Chatbot** is an interactive web-based AI system designed to provide **basic medical guidance, symptom checking, and medication suggestions** using **BioGPT**. The chatbot is built with **Streamlit** for an easy-to-use interface and supports **custom styling, chat history, and predefined responses** for quick assistance.

## ✨ Features
✅ **AI-Powered Responses:** Uses BioGPT to generate medical answers.  
✅ **Predefined Responses:** Quick answers for common questions like cold, fever, and COVID-19 symptoms.  
✅ **Appointment Scheduling Prompt:** Guides users on scheduling a doctor’s appointment.  
✅ **Interactive UI:** Beautiful design with colors, images, and chatbot-style messaging.  
✅ **Chat History:** Displays previous queries for easy reference.  

## 🛠️ Installation & Setup
### 1️⃣ **Clone the Repository**
```bash
git clone https://github.com/your-username/healthcare-chatbot.git
cd healthcare-chatbot
```

### 2️⃣ **Create Virtual Environment & Install Dependencies**
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install -r requirements.txt
```

### 3️⃣ **Run the Application**
```bash
streamlit run app.py
```

## 📂 Project Structure
```
healthcare-chatbot/
│── app.py          # Main Streamlit application
│── requirements.txt  # List of dependencies
│── README.md       # Documentation
```

## 📚 Technologies Used
- **Python** 🐍
- **Streamlit** 🎨 (For Web UI)
- **Hugging Face Transformers** 🤗 (BioGPT model)
- **PyTorch** 🔥 (For AI inference)
- **Regular Expressions (re)** ✨ (To clean AI responses)

## 🤖 How It Works
1️⃣ **User enters a medical query.**  
2️⃣ **Predefined responses** handle common symptoms & medications.  
3️⃣ **BioGPT processes other queries** and generates AI-based answers.  
4️⃣ The chatbot **removes unwanted formatting** from AI-generated text.  
5️⃣ **Styled chat messages** provide a modern user experience.  

## 📌 Example Queries
| User Query | Chatbot Response |
|------------|-----------------|
| "Hi" | "Hello! How can I assist you today? 😊" |
| "Symptoms of COVID" | "COVID-19 symptoms include fever, cough, difficulty breathing..." |
| "Medication for fever" | "For fever, take paracetamol and stay hydrated..." |
| "Schedule appointment" | "Would you like to schedule an appointment with the doctor? 📅" |

## 📝 Notes
⚠️ **This chatbot does not replace professional medical advice.** It only provides general health guidance. Always consult a doctor for serious conditions.

## 🤝 Contributing
Pull requests are welcome! If you’d like to contribute, please fork the repository and submit a PR.

## 📜 License
MIT License © 2025 Your Name

## ⭐ Acknowledgements
- [Streamlit](https://streamlit.io/)
- [Hugging Face](https://huggingface.co/microsoft/biogpt)

🚀 **Happy Coding & Stay Healthy!**

# 🧠 AI-Powered Study Buddy 🎓

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)
![Gemini API](https://img.shields.io/badge/Google_Gemini-8E75B2?style=for-the-badge&logo=google&logoColor=white)

An intelligent, interactive web application designed to transform passive reading into active learning. Built as a Capstone Project for the IBM/Edunet AI/ML Internship, this tool leverages Large Language Models (LLMs) to break down complex topics, summarize dense notes, and automatically generate interactive assessments.

🔗 **[Live Demo: Try the App Here!](https://hridayesh-ai-study-buddy.streamlit.app/)**

---

## ✨ Core Features
* **📚 Topic Explainer:** Explains any complex concept using a dual-layered approach—providing both a simple "Explain Like I'm 5" analogy and a comprehensive technical breakdown.
* **📝 Smart Summarizer:** Instantly condenses long paragraphs, textbook chapters, or lecture notes into easily digestible key takeaways.
* **🎯 Interactive Quizzes:** Automatically extracts context from pasted notes or topics to generate a custom multiple-choice quiz. Features real-time answer validation and session-state memory.
* **🎨 Premium UI/UX:** Fully responsive design featuring custom CSS, hover animations, and a seamless Light/Dark mode toggle.

---

## 🛠️ Technology Stack
* **Frontend:** Streamlit (Python) + Custom CSS
* **Backend:** Python 3.11
* **AI & Orchestration:** LangChain Core 
* **LLM Provider:** Google Gemini API (`gemini-2.5-flash`)

---

## 💻 Local Installation & Setup

If you want to run this project locally on your own machine, follow these steps:

**1. Clone the repository**

```bash
git clone [https://github.com/Hridayesh007/AI-Study-Buddy.git](https://github.com/Hridayesh007/AI-Study-Buddy.git)
cd AI-Study-Buddy
```

**2. Create a virtual environment**

```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate
```

**3. Install the required dependencies**

```bash
pip install -r requirements.txt
```

**4. Set up your API Key**

Create a `.env` file in the root directory and add your Google Gemini API key:

```env
GEMINI_API_KEY="your_api_key_here"
```

**5. Run the application**

```bash
python -m streamlit run app.py
```

---

## 👨‍💻 Author

**Puttamraju Krishna Hridayesh Kumar**
*Undergraduate Student (B.Tech ECE) @ Koneru Lakshmaiah Education Foundation*
*AI/ML Virtual Intern @ IBM / Edunet*

[![GitHub](https://img.shields.io/badge/GitHub-Profile-black?style=for-the-badge&logo=github)](https://github.com/Hridayesh007)

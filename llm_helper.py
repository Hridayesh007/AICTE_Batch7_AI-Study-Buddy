import os
import json
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate

# Load the Gemini key from the .env file
load_dotenv()

def get_llm():
    # Initialize the Gemini model
    return ChatGoogleGenerativeAI(
        model="gemini-2.5-flash", 
        google_api_key=os.environ.get("GEMINI_API_KEY"),
        temperature=0.3
    )

def get_summary(text):
    llm = get_llm()
    prompt = PromptTemplate(
        input_variables=["text"],
        template="Summarize the following text into 3-5 key bullet points. Only return the bullet points.\n\nText: {text}"
    )
    chain = prompt | llm
    response = chain.invoke({"text": text})
    return response.content

def get_topic_explanation(text):
    llm = get_llm()
    # We use a structured prompt to force the AI to return two distinct markdown sections
    prompt = PromptTemplate(
        input_variables=["text"],
        template='''You are an expert AI tutor. The user wants to learn about the following concept: "{text}"

Please provide your explanation structured exactly like this:

### 🧒 Simple Explanation (Explain Like I'm 5)
[Provide a simple, engaging explanation using an everyday analogy.]

### 🧠 In-Depth Explanation
[Provide a comprehensive, detailed explanation covering the core mechanics, importance, and technical details.]'''
    )
    chain = prompt | llm
    response = chain.invoke({"text": text})
    return response.content

def get_interactive_quiz(text):
    llm = get_llm()
    # Notice the DOUBLE curly braces {{ }} around the JSON format example below
    prompt = PromptTemplate(
        input_variables=["text"],
        template='''You are an expert AI tutor. The user has provided the following topic or study notes: 
"{text}"

Generate a 3-question multiple-choice quiz about this subject. 
Return the result STRICTLY as a valid JSON list of dictionaries. Do not include markdown formatting like ```json.
Format:
[
  {{
    "question": "Question text here?",
    "options": ["Option A", "Option B", "Option C", "Option D"],
    "answer": "Option B"
  }}
]'''
    )
    chain = prompt | llm
    response = chain.invoke({"text": text})
    
    import json
    try:
        cleaned = response.content.strip().replace('```json', '').replace('```', '')
        return json.loads(cleaned)
    except Exception as e:
        return []

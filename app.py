import streamlit as st
import llm_helper

# 1. PAGE SETUP
st.set_page_config(page_title="AI Study Buddy", page_icon="🎓", layout="wide")

# 2. LIGHT / DARK MODE TOGGLE & CSS INJECTION
with st.sidebar:
    st.title("🎓 Study Buddy")
    st.markdown("Your AI-powered learning assistant.")
    
    # The toggle switch
    dark_mode = st.toggle("🌙 Enable Dark Mode", value=False)
    st.divider()

# Set colors based on the toggle state
if dark_mode:
    bg_color = "#1E1E2E"       
    sidebar_bg = "#11111B"     
    text_color = "#CDD6F4"     
    container_bg = "#313244"   
    border_color = "#45475A"   
    input_bg = "#181825"       
else:
    bg_color = "#F4F7FE"       
    sidebar_bg = "#FFFFFF"     
    text_color = "#2B3674"     
    container_bg = "#FFFFFF"   
    border_color = "#E2E8F0"   
    input_bg = "#F8FAFC"       

# Injecting the Custom CSS
st.markdown(f"""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap');
        
        html, body, [class*="css"] {{
            font-family: 'Plus Jakarta Sans', sans-serif !important;
        }}
        
        .stApp {{ background-color: {bg_color}; color: {text_color}; }}
        [data-testid="stSidebar"] {{ background-color: {sidebar_bg} !important; border-right: 1px solid {border_color} !important; }}
        h1, h2, h3, h4, h5, h6, p, span, div, label {{ color: {text_color} !important; }}
        
        [data-testid="stVerticalBlockBorderWrapper"] {{
            border-radius: 16px !important; background-color: {container_bg} !important;
            border: 1px solid {border_color} !important; box-shadow: 0 4px 20px rgba(0, 0, 0, 0.05) !important;
            transition: all 0.3s ease-in-out; padding: 10px;
        }}
        [data-testid="stVerticalBlockBorderWrapper"]:hover {{
            box-shadow: 0 8px 30px rgba(0, 0, 0, 0.08) !important; transform: translateY(-2px);
        }}
        
        .stTextInput>div>div>input, .stTextArea>div>div>textarea {{
            border-radius: 12px !important; border: 1px solid {border_color} !important;
            background-color: {input_bg} !important; color: {text_color} !important; padding: 12px !important;
        }}
        .stTextInput>div>div>input:focus, .stTextArea>div>div>textarea:focus {{
            border: 2px solid #4318FF !important; box-shadow: none !important;
        }}
        
        .stButton>button {{
            border-radius: 12px !important; font-weight: 600 !important;
            transition: all 0.3s ease !important; border: none !important;
        }}
        .stButton>button[kind="primary"] {{
            background: linear-gradient(135deg, #4318FF 0%, #868CFF 100%) !important; color: white !important;
        }}
        .stButton>button:hover {{
            transform: translateY(-3px) !important; box-shadow: 0 10px 20px rgba(67, 24, 255, 0.3) !important;
        }}
    </style>
""", unsafe_allow_html=True)
# 3. SIDEBAR NAVIGATION CONTINUED
with st.sidebar:
    feature = st.radio(
        "Choose a Learning Tool:",
        ("📚 Explain a Topic", "📝 Summarize Notes", "🎯 Interactive Quiz"),
        label_visibility="collapsed"
    )
    st.divider()
    
    # Developer Credit
    st.caption("Built by Puttamraju Krishna Hridayesh Kumar")
    
    # Social Links using Markdown Badges
    st.markdown(
        """
        <div style="display: flex; gap: 10px; margin-bottom: 15px;">
            <a href="https://https://www.linkedin.com/in/krishna-hridayesh-kumar-puttamraju-2b3681295/" target="_blank">
                <img src="https://img.shields.io/badge/LinkedIn-Profile-blue?style=for-the-badge&logo=linkedin" alt="LinkedIn"/>
            </a>
            <a href="https://https://github.com/Hridayesh007" target="_blank">
                <img src="https://img.shields.io/badge/GitHub-Profile-black?style=for-the-badge&logo=github" alt="GitHub"/>
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    st.caption("Results powered by Gemini API")

# 4. MAIN APP HEADER
st.title("🧠 AI-Powered Study Buddy")
st.markdown("*Master complex concepts, condense long lectures, and test your knowledge.*")
st.divider()

# --- FEATURE 1: EXPLAIN A TOPIC ---
if feature == "📚 Explain a Topic":
    st.header("Topic Explainer")
    st.markdown("Get a simple analogy and a deep technical dive into any concept.")
    
    with st.container(border=True):
        topic = st.text_input("What do you want to learn today?", placeholder="e.g., Dynamic Programming, Neural Networks, Cloud Networking...")
        
        col1, col2 = st.columns([1, 4])
        with col1:
            if st.button("🚀 Explain it", type="primary"): 
                if topic:
                    with st.spinner(f"Breaking down '{topic}'..."):
                        # SAVE TO MEMORY
                        st.session_state.explanation_data = llm_helper.get_topic_explanation(topic)
                else:
                    st.warning("Please enter a topic to get started.")
        with col2:
            if "explanation_data" in st.session_state:
                if st.button("🔄 Clear"):
                    del st.session_state.explanation_data
                    st.rerun()

    # DISPLAY FROM MEMORY
    if "explanation_data" in st.session_state:
        st.success("Explanation Ready!")
        st.markdown(st.session_state.explanation_data)


# --- FEATURE 2: SUMMARIZE NOTES ---
elif feature == "📝 Summarize Notes":
    st.header("Smart Summarizer")
    st.markdown("Paste your dense lecture notes or textbook chapters to extract the key takeaways.")
    
    with st.container(border=True):
        notes = st.text_area("Source Material:", height=250, placeholder="Paste your study notes here...")
        
        col1, col2 = st.columns([1, 4])
        with col1:
            if st.button("✨ Generate Summary", type="primary"):
                if notes:
                    with st.spinner("Extracting key information..."):
                        # SAVE TO MEMORY
                        st.session_state.summary_data = llm_helper.get_summary(notes)
                else:
                    st.warning("Please paste some notes first.")
        with col2:
             if "summary_data" in st.session_state:
                if st.button("🔄 Clear"):
                    del st.session_state.summary_data
                    st.rerun()

    # DISPLAY FROM MEMORY
    if "summary_data" in st.session_state:
        st.success("Summary Generated!")
        with st.container(border=True):
            st.markdown("### Key Takeaways")
            st.markdown(st.session_state.summary_data)


# --- FEATURE 3: INTERACTIVE QUIZ ---
elif feature == "🎯 Interactive Quiz":
    st.header("Knowledge Assessment")
    st.markdown("Generate a custom multiple-choice quiz based on any topic or pasted notes.")
    
    with st.container(border=True):
        study_material = st.text_area("What should the quiz be about?", height=100, placeholder="e.g., Azure AI Principles, Data Structures, or paste your notes...")
        
        col1, col2 = st.columns([1, 4])
        with col1:
            if st.button("🎯 Generate Quiz", type="primary"):
                if study_material:
                    with st.spinner("Crafting your custom quiz..."):
                        # SAVE TO MEMORY
                        st.session_state.quiz_data = llm_helper.get_interactive_quiz(study_material)
                else:
                    st.warning("Please provide a topic or notes first.")
        
        with col2:
            if "quiz_data" in st.session_state and st.session_state.quiz_data:
                if st.button("🔄 Clear Quiz"):
                    del st.session_state.quiz_data
                    st.rerun()

    # DISPLAY FROM MEMORY
    if "quiz_data" in st.session_state and st.session_state.quiz_data:
        st.subheader("Test Your Knowledge")
        for i, q in enumerate(st.session_state.quiz_data):
            with st.container(border=True): 
                st.markdown(f"**Question {i+1}: {q.get('question', 'Error loading question')}**")
                
                user_choice = st.radio("Select your answer:", q.get("options", []), key=f"q_{i}", index=None)
                
                if user_choice:
                    if user_choice == q.get("answer"):
                        st.success("✅ Correct!")
                    else:
                        st.error(f"❌ Incorrect. The correct answer is: **{q.get('answer')}**")
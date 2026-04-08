import streamlit as st
import os
import google.generativeai as genai
from dotenv import load_dotenv

# 1. Initialize & Configuration
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

if api_key:
    genai.configure(api_key=api_key)
else:
    st.error("API Key not found. Please ensure your .env file contains GOOGLE_API_KEY.")

# 2. Enhanced Translation Logic (Supports Project Flow: Process -> Refine)
def process_translation(text, source_lang, target_lang, context):
    """
    Translates and refines text based on specific user personas:
    Business (Scenario 1), Academic (Scenario 2), or Travel (Scenario 3).
    """
    model = genai.GenerativeModel("gemini-2.5-flash") # Using latest flash for speed/latency goals
    
    # System prompt to ensure contextual relevance and clarity [cite: 29]
    context_prompts = {
        "Professional Business": "Focus on consistent brand voice, professional tone, and localized marketing nuance.",
        "Academic Research": "Maintain technical integrity, use precise scientific jargon, and ensure formal scholarly tone.",
        "General/Casual": "Focus on ease of understanding and natural conversational flow."
    }
    
    prompt = f"""
    Task: Translate the following text from {source_lang} to {target_lang}.
    Context Profile: {context_prompts.get(context, "General")}
    
    Step 1: Translate the text accurately.
    Step 2: Refine the translation for clarity, coherence, and professional formatting.
    
    Original Text: {text}
    """
    
    response = model.generate_content(prompt)
    return response.text

# 3. Travel Itinerary Feature (Scenario 3)
def generate_travel_itinerary(destination, duration, interests):
    model = genai.GenerativeModel("gemini-2.5-flash")
    prompt = f"Create a detailed travel itinerary for {destination} for {duration} days. Focus on {interests}. Ensure local landmarks are translated correctly."
    response = model.generate_content(prompt)
    return response.text

# 4. Streamlit UI (Refined for User-Centric Design)
def main():
    st.set_page_config(page_title="TransLingua AI", page_icon="🌐", layout="wide")
    
    # Sidebar for project branding
    st.sidebar.title("TransLingua")
    st.sidebar.info("AI-Powered Multi-Language Bridge [cite: 17]")
    
    st.title("🌐 TransLingua: AI-Powered Multi-Language Translator")
    st.markdown("---")

    # Implementing Tabs for different project scenarios 
    tab1, tab2 = st.tabs(["🔠 Contextual Translator", "✈️ Travel Explorer"])

    with tab1:
        col1, col2 = st.columns(2)
        with col1:
            source_lang = st.selectbox("From:", ["English", "French", "Spanish", "German", "Chinese", "Hindi", "Telugu"])
            context = st.radio("Translation Context Profile:", ["General/Casual", "Professional Business", "Academic Research"])
        with col2:
            target_lang = st.selectbox("To:", ["Spanish", "English", "French", "German", "Chinese", "Hindi", "Telugu"])
            
        input_text = st.text_area("Enter text to translate (Supports technical jargon & business docs):", height=200)

        if st.button("🔄 Process & Refine"):
            if input_text:
                with st.spinner("AI is refining your translation..."):
                    result = process_translation(input_text, source_lang, target_lang, context)
                    st.subheader("Refined Translation:")
                    st.success(result)
                    
                    # Ability to save/modify
                    st.download_button("💾 Download Translation", result, file_name="translingua_output.txt")
            else:
                st.warning("Please enter text to begin.")

    with tab2:
        st.subheader("Scenario 3: Travel & Tourism Assistance ")
        dest = st.text_input("Where are you traveling?")
        days = st.slider("Duration (Days)", 1, 14, 3)
        focus = st.multiselect("Interests:", ["Culture", "Food", "History", "Nature", "Adventure"])
        
        if st.button("🗺️ Generate Local Itinerary"):
            if dest:
                with st.spinner("Creating your AI-powered itinerary..."):
                    itinerary = generate_travel_itinerary(dest, days, ", ".join(focus))
                    st.markdown(itinerary)
            else:
                st.error("Please enter a destination.")

if __name__ == "__main__":
    main()
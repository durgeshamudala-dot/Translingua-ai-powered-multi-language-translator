# TransLingua: AI-Powered Multi-Language Translator
TransLingua is a cutting-edge web application designed to harness the power of advanced AI to provide seamless language translation services. Built using Streamlit and Google's Generative AI (Gemini Pro), the platform offers an intuitive interface for accurate, context-aware translations between multiple languages.  
Whether for professional business localization, precise academic collaboration, or real-time travel assistance, TransLingua ensures that meaning is never lost in translation.

## 🚀 Key Features
->Context-Aware Translation: Utilizes Gemini Pro to provide translations that are not just literal but contextually relevant for specific domains.<br>
->AI-Driven Refinement: Automatically formats and refines translated text to ensure clarity and coherence in the target language.<br>
->Domain Profiles: Optimized workflows for Global Business, Academic Research, and Travel & Tourism.<br>
->Interactive UI: A clean, responsive Streamlit-based frontend for real-time user interaction.<br>
->Travel Itinerary Generation: A specialized feature that generates localized travel plans based on user interests.<br>

## 🛠️ Technology Stack
>Frontend: Streamlit (Python-based web framework)<br>
>AI Engine: Google Gemini Pro (Large Language Model)<br>
>Language: Python 3.x<br>
>Environment Management: Python-Dotenv <br>

## 📐 Project Architecture & Flow
The application follows a structured data flow to ensure high performance and accuracy:<br>
->User Input: Users input text and select source/target languages via the Streamlit UI.<br>
->Backend Processing: Input data is sent to the translation backend utilizing the Gemini Pro LLM.<br>
->AI Translation: The model translates the text from the source to the target language with high contextual relevance.<br>
->Refinement: The AI formats and refines the output for maximum clarity.<br>
->Display: The final translated text is sent back to the frontend for user review and modification.<br>

## 🧠 Design Thinking & Ideation
->TransLingua was developed using a human-centric approach to problem-solving:<br>
->Empathy Mapping: We utilized an Empathy Map Canvas to capture user behaviors and attitudes, ensuring the solution addresses the actual goals and challenges of our personas.<br>

### Problem Statements:
We defined clear customer problem statements to focus on what matters most to our users, such as avoiding the high cost of manual translation and overcoming language barriers during travel.<br>

->Brainstorming: Our team used a structured template to prioritize high-volume, out-of-the-box ideas, moving from a free and open environment to a feasible project roadmap.<br>

## 📖 Use Cases
### 1. Global Business Expansion
Enables companies to quickly translate promotional content and technical documents, ensuring consistency and accuracy across different regional markets.<br>

### 2. Academic Research & Collaboration
Assists researchers in translating complex academic articles and facilitating cross-border collaborations by maintaining the integrity of scholarly documents.<br>

### 3. Travel & Tourism
Serves as a real-time tool for tourists to translate signs and menus, while generating personalized itineraries to enhance the travel experience.

## 🔧 Installation & Setup

Clone the Repository:
```bash
# Clone the repository
git clone https://github.com/your-username/TransLingua.git

# Install the required libraries
pip install -r requirements.txt
```

Configure API Key:
Create a .env file in the root directory and add your Google API Key:
```python
import google.generativeai as genai

# Configure the model
genai.configure(api_key="YOUR_API_KEY")
model = genai.GenerativeModel("gemini-2.5-flash")
```

Environment Variables
For your .env file instructions:
```env
GOOGLE_API_KEY="your_api_key_here"
```

Run the Application:
```bash
streamlit run app.py
```

## 🔮 Future Scope
->Offline Mode: Integration of lightweight local LLMs for translation without internet connectivity.
->OCR Integration: Real-time camera-based translation for street signs and physical documents.
->Voice-to-Speech: Enabling spoken translations for natural, real-time conversations.

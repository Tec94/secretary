import google.generativeai as genai, os
from load_keys import load_env
from speech_recorder import record
from speech_converter import speech_to_text

load_env()
genai.configure(model_api_key=os.getenv('MODEL_API_KEY'))

model = genai.GenerativeModel(model_name='gemini-1.5-pro')
response = model.generate_content('Teach me about how an LLM works')

print(response.text)

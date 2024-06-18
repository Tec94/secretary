import google.generativeai as genai, os
from load_keys import load_env
from speech_recorder import record
from speech_converter import speech_to_text
from get_calendar_events import get_calendar_events

load_env()
record()

genai.configure(api_key=os.getenv('MODEL_API_KEY'))

# 15 requests per min
model = genai.GenerativeModel(model_name='gemini-1.5-flash')
response = model.generate_content(speech_to_text())

print(response.text)

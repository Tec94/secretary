import google.generativeai as genai, os
from load_keys import load_env
from speech_recorder import record
from speech_converter import speech_to_text
from get_calendar_events import get_calendar_events

load_env()
record()

genai.configure(model_api_key=os.getenv('MODEL_API_KEY'))

model = genai.GenerativeModel(model_name='gemini-1.5-pro')
response = model.generate_content(speech_to_text())

print(response.text)

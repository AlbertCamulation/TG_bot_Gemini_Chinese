import pathlib
import textwrap
import google.generativeai as genai
from  variable import Globals as global_var

genai.configure(api_key=global_var.TOKEN_Gemini)

for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
    print(m.name)

# model = genai.GenerativeModel('gemini-1.0-pro')
# model = genai.GenerativeModel('gemini-1.0-pro-001')
# model = genai.GenerativeModel('gemini-1.0-pro-latest')
# model = genai.GenerativeModel('gemini-1.0-pro-vision-latest')
model = genai.GenerativeModel('gemini-pro')
# model = genai.GenerativeModel('gemini-pro-vision')

def tg_gemini(prompt):
  first_off_prompt='使用繁體中文回答'
  response = model.generate_content(first_off_prompt+prompt)
  output=response.text
  print(output)
  result=f"{output}"
  return  result
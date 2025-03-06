import google.generativeai as genai

def get_gemini_response(question, prompt):
  model = genai.GenerativeModel('gemini-2.0-flash')
  response = model.generate_content([prompt[0], question])
  return response.text
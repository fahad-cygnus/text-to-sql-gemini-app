from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import os

# Load the model and tokenizer
# Adjust the model name as necessary
# model_name = "meta-llama/Llama-2-7b-chat-hf"
# tokenizer = AutoTokenizer.from_pretrained(model_name, use_auth_token=os.getenv("HUGGINGFACE_API_KEY"))
# model = AutoModelForCausalLM.from_pretrained(model_name, use_auth_token=os.getenv("HUGGINGFACE_API_KEY"))

def get_llama_response(question, prompt):
  # # Prepare the input
  # input_text = prompt[0] + question
  # inputs = tokenizer(input_text, return_tensors="pt")

  # # Generate response
  # with torch.no_grad():
  #   outputs = model.generate(**inputs, max_length=150)  # Adjust max_length as needed

  # response = tokenizer.decode(outputs[0], skip_special_tokens=True)
  # return response
  return "Llama model is currently unavailable"
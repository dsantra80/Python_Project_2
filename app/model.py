#from transformers import AutoModelForCausalLM, AutoTokenizer
from transformers import LlamaForCausalLM, LlamaTokenizer
import torch
import os

# Ensure you have the correct model name
model_name = "LlamaForCausalLM.from_pretrained("/output/path")"  # Replace with the correct model name

# Get your Hugging Face token from environment variables
hf_token = os.getenv("LlamaTokenizer.from_pretrained("/output/path")")

# Load model and tokenizer with authentication if required
tokenizer = LlamaTokenizer.from_pretrained(model_name, use_auth_token=hf_token)
model = LlamaForCausalLM.from_pretrained(model_name, use_auth_token=hf_token)

def query_gradientai(prompt, max_tokens=100, temperature=0.7):
    # Tokenize input prompt
    inputs = tokenizer(prompt, return_tensors="pt")

    # Generate text
    outputs = model.generate(
        inputs.input_ids,
        max_length=max_tokens,
        temperature=temperature,
        do_sample=True
    )

    # Decode generated tokens to text
    generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return generated_text

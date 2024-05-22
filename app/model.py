from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Load model and tokenizer globally to avoid re-loading on each request
model_name = "meta-llama/LLaMA-3b"  # Replace with the actual model name
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

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

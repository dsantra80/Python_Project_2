from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Load the model and tokenizer
model_name = "gradientai/llama-3-8b-instruct-gradient-1048k"
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

def query_gradientai(prompt, max_tokens, temperature):
    # Tokenize input text
    input_ids = tokenizer.encode(prompt, return_tensors='pt')

    # Generate text using the model
    output = model.generate(input_ids, max_length=max_tokens, temperature=temperature)

    # Decode generated output
    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)

    return generated_text

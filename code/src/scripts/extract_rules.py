import os
from huggingface_hub import login
from transformers import pipeline

# Function to authenticate with Hugging Face using an API token
def authenticate_huggingface():
    # Check if the token is available in environment variable
    hf_token = "token"

    if not hf_token:
        raise ValueError("Hugging Face token is missing! Please set the 'HF_AUTH_TOKEN' environment variable.")

    # Log in with the Hugging Face token
    try:
        login(token=hf_token)
        print("Successfully authenticated with Hugging Face!")
    except Exception as e:
        print(f"Error authenticating with Hugging Face: {e}")
        raise

# Function to extract validation rules using the GPT-2 model
def extract_validation_rules(instructions_text):
    # Authenticate with Hugging Face before using the model
    authenticate_huggingface()

    # Load the GPT-2 model using Hugging Face's pipeline
    model = pipeline('text-generation', model='gpt2')  # Use 'gpt2' or 'gpt3' for Hugging Face

    # Generate rules based on the instructions
    rules = model(instructions_text, max_length=200)
    return rules

if __name__ == "__main__":
    # Example instructions for validation rules
    instructions = """
    The data should be validated for the following constraints:
    - Validate cross-border transaction limits (for simplicity, assuming a cross-border flag is set)
    - Validate Account Balance - should never be negative unless marked as overdraft (OD)
    - Check for cross-currency transactions (allow up to 1% deviation)
    - Validate that Transaction Amount matches the Reported Amount (with 1% deviation for cross-currency transactions).
    """

    # Extract validation rules
    validation_rules = extract_validation_rules(instructions)

    # Print the generated rules
    print(validation_rules)

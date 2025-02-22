from openai import OpenAI

# Set OpenAI's API key and API base to use vLLM's API server.
openai_api_key = "EMPTY"
openai_api_base = "http://0.0.0.0:21554/v1"

client = OpenAI(
    api_key=openai_api_key,
    base_url=openai_api_base,
)

# Capture user input from the terminal
user_input = input("Please enter your prompt: ")

chat_response = client.chat.completions.create(
    model="/usr/local/models/Meta-Llama-3.1-8B-Instruct-AWQ-INT4",
    messages=[
        {"role": "system", "content": "You are my Phison aiDaptiv expert"},
        {"role": "user", "content": user_input},
    ]
)

print("Chat response:", chat_response)

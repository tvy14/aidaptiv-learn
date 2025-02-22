from openai import OpenAI

# Set OpenAI's API key and API base
openai_api_key = "EMPTY"
openai_api_base = "http://0.0.0.0:21554/v1"

client = OpenAI(
    api_key=openai_api_key,
    base_url=openai_api_base,
)

def get_user_input():
    """Captures user input from the terminal."""
    return input("Please enter your prompt (type 'exit' to stop): ")

def send_to_ai(user_input):
    """Sends user input to AI model and prints response."""
    chat_response = client.chat.completions.create(
        model="/usr/local/models/Meta-Llama-3.1-8B-Instruct-AWQ-INT4",
        max_tokens=50, # Lowered max tokens for faster response
        messages=[
            {"role": "system", "content": "You are my Phison aiDaptiv expert"},
            {"role": "user", "content": user_input},
        ]
    )
    
    print("Chat response:", chat_response.choices[0].message.content)

def main():
    while True:
        user_input = get_user_input()
        
        if user_input.lower() == 'exit':
            break
        
        send_to_ai(user_input)

if __name__ == "__main__":
    main()

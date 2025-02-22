from openai import OpenAI

# Set OpenAI's API key and API base
openai_api_key = "EMPTY"
openai_api_base = "http://0.0.0.0:21554/v1"

client = OpenAI(
    api_key=openai_api_key,
    base_url=openai_api_base,
)

def get_system_input():
    """Captures system role input from the user."""
    return input("Please enter the system role (or press Enter to skip): ")

def get_user_input():
    """Captures user input for the conversation."""
    return input("Enter your message (type 'exit' to stop): ")

def send_to_ai(system_content, user_input):
    """Sends user input to AI model and prints response."""
    messages = []
    if system_content:
        messages.append({"role": "system", "content": system_content})
    messages.append({"role": "user", "content": user_input})

    chat_response = client.chat.completions.create(
        model="/usr/local/models/Meta-Llama-3.1-8B-Instruct-AWQ-INT4",
        max_tokens=50,  # Lowered max tokens for faster response
        messages=messages
    )
    
    print("AI response:", chat_response.choices[0].message.content)

def main():
    system_content = get_system_input()
    print("System role set. You can now start the conversation.")
    
    while True:
        user_input = get_user_input()
        
        if user_input.lower() == 'exit':
            break
        
        send_to_ai(system_content, user_input)

if __name__ == "__main__":
    main()

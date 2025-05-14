import requests
import json
import tkinter as tk
from tkinter import scrolledtext
import threading
import sys # To exit the script

def get_model_response(model, prompt):
    url = "http://localhost:11434/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        |}
    data = {
        "model": model,
        "prompt": prompt,
        "stream": False,
        "temperature": 0.7,
        "top_p": 1.0,
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None
    
def build_convo(models, initial_idea_prompt, filename):
    convo = []
    current_prompt = initial_idea_prompt
    exchange_counter = 1
    model_index = 0
    num_models = len(models)

    while True:
        current_model = models[model_index]
        next_model = models[(model_index + 1) % num_models]
        response = get_model_response(current_model, current_prompt) #get the response from the model
        if response:
            conversation.append(f"{current_model}(Part{exchange_counter}):{current_prompt}\n")
            conversation.append(f"next_model(Part{exchange_counter}):{response['choices'][0]['text']}\n")
            break
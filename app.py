# app.py

import requests
from config import API_URL, HF_TOKEN
import json

print("\n🌿 Welcome to the PLLaMa-7B CLI (API Edition)")
print("Ask a plant science question (type 'exit' to quit):\n")

while True:
    user_input = input("🧑‍🌾 You: ").strip()
    if user_input.lower() in ["exit", "quit"]:
        print("👋 Exiting. See you again!")
        break

    payload = {
        "inputs": f"You are a helpful plant science assistant. Answer this simply:\n{user_input}\nAnswer:",
        "parameters": {
            "temperature": 0.7,
            "max_new_tokens": 256,
            "top_p": 0.9
        }
    }

    headers = {
        "Authorization": f"Bearer {HF_TOKEN}",
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        response.raise_for_status()
        data = response.json()
        text = data[0]["generated_text"] if isinstance(data, list) else data.get("generated_text", "")
        print(f"\n🌱 PLLaMa: {text.split('Answer:')[-1].strip()}\n")
    except Exception as e:
        print("❌ Error:", e)

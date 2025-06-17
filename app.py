"""Command line interface for the PLLaMa assistant."""

from datetime import datetime
import sys
import requests

from config import API_URL, HF_TOKEN


def query_model(question: str) -> str:
    """Send the question to the inference endpoint and return the answer."""
    payload = {
        "inputs": (
            "You are a helpful plant science assistant. Answer this simply:\n"
            f"{question}\nAnswer:"
        ),
        "parameters": {
            "temperature": 0.7,
            "max_new_tokens": 256,
            "top_p": 0.9,
        },
    }

    headers = {
        "Authorization": f"Bearer {HF_TOKEN}",
        "Content-Type": "application/json",
    }

    response = requests.post(API_URL, headers=headers, json=payload)
    response.raise_for_status()
    data = response.json()
    text = data[0]["generated_text"] if isinstance(data, list) else data.get(
        "generated_text", ""
    )
    return text.split("Answer:")[-1].strip()


def main() -> None:
    """Run the interactive chat loop."""
    print("\n🌿 Welcome to the PLLaMa-7B CLI (API Edition)")
    print("Ask a plant science question (type 'exit' to quit):\n")

    while True:
        try:
            user_input = input("🧑‍🌾 You: ").strip()
        except EOFError:
            print("\n👋 Exiting. See you again!")
            break

        if not user_input:
            continue
        if user_input.lower() in {"exit", "quit"}:
            print("👋 Exiting. See you again!")
            break

        try:
            answer = query_model(user_input)
            print(f"\n🌱 PLLaMa: {answer}\n")
            with open("log.txt", "a", encoding="utf-8") as log:
                timestamp = datetime.utcnow().isoformat()
                log.write(f"{timestamp}\nQ: {user_input}\nA: {answer}\n\n")
        except Exception as exc:
            print("❌ Error:", exc, file=sys.stderr)


if __name__ == "__main__":
    main()

# PLLaMa CLI Assistant

This project provides a simple command line interface for interacting with a
PLLaMa model hosted on a Hugging Face Inference Endpoint.

## Setup
1. Create a `.env` file in the project directory containing `API_URL` and
   `HF_TOKEN`.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the assistant:
   ```bash
   python app.py
   ```

## Usage
Type your plant science question and press `Enter`. Use `exit` or `quit` to
leave the program. Every question and answer pair is appended to `log.txt` for
reference.


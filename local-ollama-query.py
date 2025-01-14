# imports

import requests

# Constants
OLLAMA_API = "http://localhost:11434/api/chat"
HEADERS = {"Content-Type": "application/json"}
MODEL = "llama3.2"

# Define prompts
system_prompt = "You provide technical answers to IT realted questions"
user_prompt = """
    How many bits are in a byte?
"""


# Create a messages list using the same format that we used for OpenAI
messages = [
    {"role": "system", "content": system_prompt },
    {"role": "user", "content": user_prompt }
]


# Step 3: Set payload and call Ollama
payload = {
        "model": MODEL,
        "messages": messages,
        "stream": False
    }
response = requests.post(OLLAMA_API, json=payload, headers=HEADERS)


# Step 4: print the result
print(response.json()['message']['content'])

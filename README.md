# Ollama Python Script

This is a basic Python script that demonstrates how to integrate the Ollama AI tool into your project. The script interacts with the Ollama API to utilize its AI-powered features.

## Features

- Sends a prompt to the Ollama API.
- Receives and displays the AI-generated response.
- Easy-to-extend script for custom use cases.

## Prerequisites

Before running the script, make sure you have the following:

1. Python installed (version 3.7 or later).
2. Access to the Ollama AI tool and its API.
3. A valid API link for the Ollama service.
4. Ollama is running.

## Installation

1. Clone this repository or download the script file:
   ```bash
   git clone https://github.com/whiskyneat/ai-ollama-basic.git
   ```

2. Install the required Python packages:
   ```bash
   pip install requests
   ```

## Configuration

Before running the script, you need to set your Ollama API key. Create a `.env` file in the project directory and add your API key like this:

```
OLLAMA_API = "http://localhost:11434/api/chat"
```

Alternatively, you can set the API key as an environment variable.

## Usage

1. Open the script file (e.g., `ollama_script.py`) and modify the `prompt` variable with the desired input for the AI.

2. Run the script:
   ```bash
   python local-ollama-query.py
   ```

3. View the AI-generated response in the console.

## Example Code

Here's a simplified version of the script:

```python
# imports

import requests

# Constants
OLLAMA_API = "http://localhost:11434/api/chat"
HEADERS = {"Content-Type": "application/json"}
MODEL = "llama3.2"

# Define prompts
system_prompt = "You love dark humor and jokes."
user_prompt = input("What's your question? ")


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
```

## Contributing

Feel free to fork this repository and submit pull requests for improvements or additional features.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


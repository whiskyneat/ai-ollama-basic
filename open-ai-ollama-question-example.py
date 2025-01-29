# imports
import os
from openai import OpenAI
from dotenv import load_dotenv
import ollama

# constants

MODEL_GPT = 'gpt-4o-mini'
MODEL_LLAMA = 'llama3.2'

# set up environment
load_dotenv(override=True)
api_key = os.getenv('OPENAI_API_KEY')
openai = OpenAI()

# here is the question; type over this to ask something new
question = """
Why don't skeletons fight each other?
"""

# Get gpt-4o-mini to answer, with streaming

response = openai.chat.completions.create(
    model=MODEL_GPT,
    messages=[{"role":"user", "content":question}],
    stream=True #enables streaming
    )

# Stream and print the response
for chunk in response:
    content = chunk.choices[0].delta.content  # Directly access `content`
    if content:  # Ensure content is not None
        print(content, end="", flush=True)


# Get Llama 3.2 to answer
response = ollama.chat(model=MODEL_LLAMA, messages=[{"role": "user", "content": question}], stream=True)

# Stream and print the response in real-time
for chunk in response:
    if "message" in chunk and "content" in chunk["message"]:
        print(chunk["message"]["content"], end="", flush=True)

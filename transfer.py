import gradio as gr
import openai
import os

# Set OpenAI API Key
openai.api_key = os.getenv("OPENAI_API_KEY")

def chat_with_gpt(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        return str(e)

# Create a simple Gradio interface
iface = gr.Interface(
    fn=chat_with_gpt,
    inputs="text",
    outputs="text",
    title="OpenAI Chatbot",
    description="Ask anything, and GPT-3.5 will respond!"
)

if __name__ == "__main__":
    iface.launch(server_name="0.0.0.0", server_port=7860)


#################
import openai
import requests
from bs4 import BeautifulSoup

# Set up OpenAI API key
openai.api_key = "your_openai_api_key"

def summarize_webpage(url):
    """
    Fetches and summarizes the content of a webpage using OpenAI's LLM.
    
    Args:
        url (str): The URL of the webpage to summarize.
    
    Returns:
        str: A summarized version of the webpage content.
    """
    try:
        # Fetch webpage content
        response = requests.get(url)
        if response.status_code != 200:
            return f"Error: Unable to fetch the webpage (Status Code: {response.status_code})"

        # Parse the webpage
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Extract main content (ignoring scripts, styles, and navigation)
        for script in soup(["script", "style", "nav", "footer", "header"]):
            script.extract()
        
        text = soup.get_text()
        text = " ".join(text.split())  # Remove excessive whitespace
        
        # Truncate text if it's too long
        max_chars = 4000  # Token limit handling
        text = text[:max_chars]

        # Generate a summary using OpenAI's GPT
        prompt = f"Summarize the following webpage content in a concise and clear manner:\n\n{text}"
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "system", "content": "You are an expert at summarizing webpage content clearly and concisely."},
                      {"role": "user", "content": prompt}]
        )

        summary = response["choices"][0]["message"]["content"]
        return summary

    except Exception as e:
        return f"An error occurred: {str(e)}"

# Example usage
# print(summarize_webpage("https://example.com"))

############

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

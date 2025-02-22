import gradio as gr
from openai import OpenAI

client = OpenAI(base_url="http://127.0.0.1:1337/v1")

def chatbot_response(input_text):
    completion = client.chat.completions.create(
        model="llama3.2-1b-instruct",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": input_text}
        ],
        max_tokens=50
    )
    return completion.choices[0].message.content

iface = gr.Interface(
    fn=chatbot_response,
    inputs="text",
    outputs="text",
    title="Chatbot LLM Local",
    description="Um chatbot simples conectado a um LLM local."
)

if __name__ == "__main__":
    iface.launch()

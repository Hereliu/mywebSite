from flask import Flask, render_template, request, jsonify
import openai
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()  # take environment variables from .env.

openai.api_type = "azure"
openai.api_base = "https://openai-et-na-lab.openai.azure.com/"
openai.api_version = "2023-03-15-preview"
openai.api_key = ""#os.environ.get("AZURE_OPENAI_KEY")

def ask_gpt3(question):
    response = openai.ChatCompletion.create(
        engine="gpt-4-8K",
            messages=[
                {
                    "role": "system",
                    "content": "You are an AI assistant that helps people find information.",
                #"content": name,
                },
                {
                    "role": "user",
                    "content": question,
                },
            ],
            #prompt="Translate the following English text to French: '{}'".format(name),
            temperature=0.7,
            max_tokens=800,
            top_p=0.95,
            frequency_penalty=0,
            presence_penalty=0,
            stop=None,
        )
    return "{}".format(response.choices[0].message.content)




@app.route("/")
def index():
    return render_template("chat.html")

@app.route("/send_message", methods=["POST"])
def send_message():
    message = request.form["message"]
    response = ask_gpt3(message)# 这里可以放你的消息处理逻辑
    return jsonify(response=response)





if __name__ == "__main__":
    app.run(port=5000)
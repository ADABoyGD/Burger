import os
import openai
from flask import Flask, request, jsonify

openai.api_key = os.getenv("OPENAI_API_KEY")

def chat_with_agent(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat_endpoint():
    data = request.get_json()
    prompt = data.get("prompt", "")
    try:
        answer = chat_with_agent(prompt)
        return jsonify({"answer": answer})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/")
def index():
    return """<html>
      <head><title>My AI Agent</title></head>
      <body>
        <h1>Ask the AI!</h1>
        <form action="/chat" method="post" onsubmit="sendPrompt(event)">
          <input id="prompt" type="text" name="prompt" placeholder="Enter prompt" />
          <button type="submit">Send</button>
        </form>
        <div id="response"></div>
        <script>
          async function sendPrompt(e) {
            e.preventDefault();
            const promptText = document.getElementById('prompt').value;
            const response = await fetch('/chat', {
              method: 'POST',
              headers: { 'Content-Type': 'application/json' },
              body: JSON.stringify({ prompt: promptText })
            });
            const data = await response.json();
            document.getElementById('response').textContent = data.answer || data.error || "No response";
          }
        </script>
      </body>
    </html>"""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

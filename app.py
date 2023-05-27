from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import openai
import os

app = Flask(__name__)
CORS(app)

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/", methods=("GET", "POST"))
def index():
    return render_template("index.html")

@app.route('/generate', methods=['POST'])
def generate():
    data = request.form
    prompt = data.get('prompt', '')
    model = data.get('model', 'gpt-3.5-turbo') 

    response = openai.ChatCompletion.create(
      model=model,
      messages=[{"role": "user","content": f"{prompt}"}],
      n=1
    )

    return jsonify({'output': response['choices'][0]['message']['content']})


if __name__ == '__main__':
    app.run(debug=True)
    

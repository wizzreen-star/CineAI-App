from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import os

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    print("❌ GEMINI_API_KEY not found!")
else:
    print("✅ GEMINI_API_KEY loaded successfully.")

genai.configure(api_key=GEMINI_API_KEY)

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()
    prompt = data.get("prompt")

    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(f"Create a YouTube Shorts video script for: {prompt}")
        return jsonify({"response": response.text})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

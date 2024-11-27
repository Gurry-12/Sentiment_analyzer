from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

from transformers import pipeline

sent_pipeline = pipeline("sentiment-analysis")

# Load models
with open("models/tfidf_vectorizer.pkl", "rb") as vec_file:
    tfidf_vectorizer = pickle.load(vec_file)

with open("models/sentiment_model.pkl", "rb") as model_file:
    svm_model = pickle.load(model_file)

@app.route("/", methods=["GET", "POST"])
def index():
    
    return render_template("index.html")

@app.route("/result", methods=["POST"])
def result():
    user_input = request.form.get("user_input", "")
    if user_input.strip():
        try:
            # Predict sentiment using Hugging Face pipeline
            result = sent_pipeline(user_input)
            sentiment = result[0]['label']
            score = result[0]['score']

            return render_template(
                "result.html",
                text=user_input,
                sentiment=sentiment,
                score=round(score * 100, 2)  # Convert to percentage
            )
        except Exception as e:
            return f"Error in sentiment prediction: {e}", 500
    else:
        return render_template("index.html", error="Please enter valid text.")


if __name__ == "__main__":
    app.run(debug=True)

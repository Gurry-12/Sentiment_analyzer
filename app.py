from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load models
with open("models/tfidf_vectorizer.pkl", "rb") as vec_file:
    tfidf_vectorizer = pickle.load(vec_file)

with open("models/svm_model.pkl", "rb") as model_file:
    svm_model = pickle.load(model_file)

# Label mapping
label_mapping = {0: "Neutral", 1: "Positive", 2: "Negative"}

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/result", methods=["POST"])
def result():
    user_input = request.form.get("user_input", "")
    
    if user_input.strip():
        try:
            # Preprocess input text and vectorize
            input_tfidf = tfidf_vectorizer.transform([user_input])
            
            # Predict sentiment
            prediction = svm_model.predict(input_tfidf)[0]  # Numeric label (0, 1, or 2)
            
            # Dummy scores for demonstration (update with actual probability scores if available)
            scores = svm_model.decision_function(input_tfidf).tolist()[0]
            neutral_score = round((scores[0] if prediction == 0 else 0) * 10, 2)
            positive_score = round((scores[1] if prediction == 1 else 0) * 10, 2)
            negative_score = round((scores[2] if prediction == 2 else 0) * 10, 2)
            
            return render_template(
                "result.html",
                text=user_input,
                sentiment=prediction,  # Numeric sentiment
                neutral_score=neutral_score,
                positive_score=positive_score,
                negative_score=negative_score
            )
        except Exception as e:
            return f"Error in sentiment prediction: {e}", 500
    else:
        return render_template("index.html", error="Please enter valid text.")

if __name__ == "__main__":
    app.run(debug=True)

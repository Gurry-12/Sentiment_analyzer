
# Sentiment Analyzer

A Flask-based web application for sentiment analysis. This project uses a pre-trained Support Vector Machine (SVM) model and TF-IDF vectorizer to classify text as positive, negative, or neutral.

## Table of Contents

- [Features](#features)
- [Setup](#setup)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Screenshots](#screenshots)
- [License](#license)

---

## Features

- Predicts sentiment of text input (positive, negative, neutral).
- User-friendly web interface built with Flask.
- Deployed on Replit for quick access.
- Uses SVM for accurate predictions.

---

## Setup

### Prerequisites

- Python 3.8 or higher
- Flask 3.1.0
- Scikit-learn 1.5.2
- Gunicorn (for production deployment)

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/YourUsername/sentiment-analyzer.git
   cd sentiment-analyzer


2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Ensure the required models and vectorizer files are in the project folder:
   - `tfidf_vectorizer.pkl`
   - `svm_model.pkl`

---

## Usage

### Local Development

1. Run the Flask app:
   ```bash
   flask run --host=0.0.0.0 --port=8080
   ```

2. Open your browser and go to:
   ```
   http://localhost:8080
   ```

### Deployment on Replit

1. Upload your project files to Replit.
2. Use the following run command:
   ```bash
   flask run --host=0.0.0.0 --port=8080
   ```

3. Access the Replit deployment URL.

---

## Technologies Used

- **Python**: Backend programming
- **Flask**: Web framework
- **Scikit-learn**: Machine learning library for sentiment analysis
- **Gunicorn**: WSGI HTTP server for production

---

## Project Structure

```plaintext
sentiment-analyzer/
│
├── static/
│   └── style.css           # CSS for the web interface
├── templates/
│   └── index.html          # HTML template
├── app.py                  # Flask application
├── tfidf_vectorizer.pkl    # Pre-trained TF-IDF vectorizer
├── svm_model.pkl           # Trained SVM model
├── requirements.txt        # Dependencies
└── README.md               # Project documentation
```

---

## Screenshots

### Home Page
![Home Page](https://via.placeholder.com/800x400.png?text=Add+Screenshot)

### Sentiment Result
![Result Page](https://via.placeholder.com/800x400.png?text=Add+Screenshot)

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Author

**Gurpreet Singh**  
- [GitHub](https://github.com/Gurry-12)
- [LinkedIn](https://www.linkedin.com/in/gurpreet-singh57/)
```


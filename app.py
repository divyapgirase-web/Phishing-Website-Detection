from flask import Flask, request, render_template
import joblib
from feature_extraction import extract_features

app = Flask(__name__)

# Load trained model
model = joblib.load("phishing_model.pkl")


@app.route("/", methods=["GET", "POST"])
def home():
    result = ""

    if request.method == "POST":
        url = request.form["url"].strip()

        if not url:
            result = "Please enter a website URL."

        elif not (url.startswith("http://") or url.startswith("https://")):
            result = "Please enter a valid URL starting with http:// or https://"

        else:
            features = extract_features(url)

            prediction = model.predict([features])[0]

            if prediction == 1:
                result = "⚠️ Phishing Website"
            else:
                result = "✅ Legitimate Website"

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)
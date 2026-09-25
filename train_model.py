import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib

# Load dataset
data = pd.read_csv("Dataset_small.csv")

# Select only the features we can extract from a URL
from urllib.parse import urlparse
import re

def extract_features(url):
    features = []

    # URL length
    features.append(len(url))

    # Number of dots
    features.append(url.count("."))

    # Number of hyphens
    features.append(url.count("-"))

    # @ symbol
    features.append(url.count("@"))

    # Number of digits
    features.append(sum(c.isdigit() for c in url))

    # HTTPS
    features.append(1 if url.startswith("https://") else 0)

    # Number of subdomains
    try:
        hostname = urlparse(url).hostname or ""
        subdomains = hostname.count(".")
    except:
        subdomains = 0

    features.append(subdomains)

    # Suspicious words
    suspicious_words = [
        "login",
        "verify",
        "account",
        "update",
        "secure",
        "bank",
        "signin",
        "password"
    ]

    suspicious_count = sum(
        1 for word in suspicious_words
        if word in url.lower()
    )

    features.append(suspicious_count)

    # Special characters
    special_chars = len(
        re.findall(r"[^a-zA-Z0-9]", url)
    )

    features.append(special_chars)

    return features

# Create features from dataset URLs
# This requires a URL column in the dataset.
print("Dataset loaded!")
print("Columns available:")
print(data.columns.tolist())
feature_columns = [
    "length_url",
    "qty_dot_url",
    "qty_hyphen_url",
    "qty_at_url",
    "qty_slash_url",
    "qty_questionmark_url",
    "qty_equal_url",
    "qty_percent_url",
    "qty_underline_url"
]
X = data[feature_columns]
y = data["phishing"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("\nModel trained successfully!")
print("Accuracy:", accuracy)

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

joblib.dump(model, "phishing_model.pkl")

print("\nModel saved as phishing_model.pkl")
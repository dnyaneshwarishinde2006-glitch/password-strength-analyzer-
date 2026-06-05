import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, confusion_matrix

# Sample dataset
data = {
    "email": [
        "Click here to claim your free prize now",
        "Your account has been suspended verify immediately",
        "Meeting scheduled for tomorrow at 10 AM",
        "Project report attached for review",
        "Congratulations you won a lottery",
        "Please update your banking details"
    ],
    "label": [
        "Phishing",
        "Phishing",
        "Safe",
        "Safe",
        "Phishing",
        "Phishing"
    ]
}

df = pd.DataFrame(data)

# Features and labels
X = df["email"]
y = df["label"]

# Convert text into numerical features
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(X)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Train model
model = MultinomialNB()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Confusion Matrix
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# Test custom email
email = ["Verify your account immediately by clicking this link"]
email_features = vectorizer.transform(email)

prediction = model.predict(email_features)
print("\nPrediction:", prediction[0])
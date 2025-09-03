import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
import pickle
import os

# -------------------------------
# Load dataset
# -------------------------------
df = pd.read_csv("heart.csv")   # make sure heart.csv is in the same folder
df = df.drop_duplicates()

X = df.drop("target", axis=1)
y = df["target"]

# -------------------------------
# Train/test split
# -------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -------------------------------
# Scale features
# -------------------------------
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# -------------------------------
# Train Logistic Regression
# -------------------------------
model = LogisticRegression(max_iter=1000)  # add max_iter to avoid warnings
model.fit(X_train_scaled, y_train)

# -------------------------------
# Evaluate
# -------------------------------
y_pred = model.predict(X_test_scaled)
accuracy = accuracy_score(y_test, y_pred)
print(f"✅ Model accuracy: {accuracy:.2f}")

# -------------------------------
# Save model and scaler
# -------------------------------
save_dir = "predictor_collection"
os.makedirs(save_dir, exist_ok=True)

with open(os.path.join(save_dir, "model.pkl"), "wb") as f:
    pickle.dump(model, f)

with open(os.path.join(save_dir, "scaler.pkl"), "wb") as f:
    pickle.dump(scaler, f)

print(f"✅ model.pkl and scaler.pkl saved inside {save_dir}/")

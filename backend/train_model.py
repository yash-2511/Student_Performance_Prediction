
import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OrdinalEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import joblib

# Define paths
base_dir = os.path.dirname(__file__)
data_path = os.path.join(base_dir, '../data/student_data.csv')
model_dir = os.path.join(base_dir, '../models')

# Create models directory if it doesn't exist
os.makedirs(model_dir, exist_ok=True)

# Load dataset
df = pd.read_csv(data_path)

# Encode categorical features
encoder = OrdinalEncoder()
df[["internet", "parent_education"]] = encoder.fit_transform(df[["internet", "parent_education"]])

# Features and target
X = df.drop("performance", axis=1)
y = df["performance"]

# Scale numeric features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save model and preprocessors
joblib.dump(model, os.path.join(model_dir, "model.pkl"))
joblib.dump(scaler, os.path.join(model_dir, "scaler.pkl"))
joblib.dump(encoder, os.path.join(model_dir, "encoder.pkl"))

# Evaluation
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))

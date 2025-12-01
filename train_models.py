import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# 1. Load the clean data
print("⏳ Loading data...")
try:
    df = pd.read_csv('tickets.csv')
except FileNotFoundError:
    print("❌ Error: tickets.csv not found. Run clean_data.py first.")
    exit()

# --- FIX: HANDLE MISSING VALUES ---
print(f"   Original rows: {len(df)}")
# Drop rows where urgency or department is empty (NaN)
df = df.dropna(subset=['urgency', 'department', 'ticket_text'])
print(f"   Rows after cleaning NaNs: {len(df)}")
# ----------------------------------

# 2. Convert Text to Numbers (Vectorization)
print("⏳ Vectorizing text...")
vectorizer = TfidfVectorizer(max_features=5000, stop_words='english')
X = vectorizer.fit_transform(df['ticket_text'])

# 3. Train Model 1: Department Classifier
print("⏳ Training Department Model...")
y_dept = df['department']
X_train_d, X_test_d, y_train_d, y_test_d = train_test_split(X, y_dept, test_size=0.2, random_state=42)

model_dept = LogisticRegression(max_iter=1000)
model_dept.fit(X_train_d, y_train_d)

pred_dept = model_dept.predict(X_test_d)
print(f"✅ Department Model Accuracy: {accuracy_score(y_test_d, pred_dept):.2f}")

# 4. Train Model 2: Urgency Classifier
print("⏳ Training Urgency Model...")
y_urgency = df['urgency']
X_train_u, X_test_u, y_train_u, y_test_u = train_test_split(X, y_urgency, test_size=0.2, random_state=42)

model_urgency = LogisticRegression(max_iter=1000)
model_urgency.fit(X_train_u, y_train_u)

pred_urgency = model_urgency.predict(X_test_u)
print(f"✅ Urgency Model Accuracy: {accuracy_score(y_test_u, pred_urgency):.2f}")

# 5. Save the Models
print("⏳ Saving models...")
joblib.dump(vectorizer, 'tfidf_vectorizer.pkl')
joblib.dump(model_dept, 'model_department.pkl')
joblib.dump(model_urgency, 'model_urgency.pkl')

print("\n🎉 Success! Models saved successfully.")

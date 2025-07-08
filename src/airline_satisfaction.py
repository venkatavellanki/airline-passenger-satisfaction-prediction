# airline_satisfaction.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, f1_score, classification_report
import os

# Load dataset
data_path = os.path.join('..', 'data', 'Airline_Passenger_Satisfaction.csv')
df = pd.read_csv(data_path)

# Data preprocessing
df.dropna(inplace=True)
df['Gender'] = df['Gender'].map({'Male': 1, 'Female': 0})
df['Customer Type'] = df['Customer Type'].map({'Loyal Customer': 1, 'Disloyal Customer': 0})
df['Type of Travel'] = df['Type of Travel'].map({'Business travel': 1, 'Personal Travel': 0})
df['Class'] = df['Class'].map({'Business': 2, 'Economy Plus': 1, 'Economy': 0})
df['satisfaction'] = df['satisfaction'].map({'satisfied': 1, 'neutral or dissatisfied': 0})

X = df.drop(['satisfaction'], axis=1)
y = df['satisfaction']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Decision Tree Classifier
dt_model = DecisionTreeClassifier()
dt_model.fit(X_train, y_train)
dt_preds = dt_model.predict(X_test)

# Naive Bayes Classifier
nb_model = GaussianNB()
nb_model.fit(X_train, y_train)
nb_preds = nb_model.predict(X_test)

# Evaluation
dt_accuracy = accuracy_score(y_test, dt_preds)
dt_f1 = f1_score(y_test, dt_preds)

nb_accuracy = accuracy_score(y_test, nb_preds)
nb_f1 = f1_score(y_test, nb_preds)

# Save outputs
os.makedirs('../output', exist_ok=True)

with open('../output/decision_tree_results.txt', 'w') as f:
    f.write("Decision Tree Classifier Results:\n")
    f.write(f"Accuracy: {dt_accuracy:.2f}\n")
    f.write(f"F1 Score: {dt_f1:.2f}\n")
    f.write("\nClassification Report:\n")
    f.write(classification_report(y_test, dt_preds))

with open('../output/naive_bayes_results.txt', 'w') as f:
    f.write("Naive Bayes Classifier Results:\n")
    f.write(f"Accuracy: {nb_accuracy:.2f}\n")
    f.write(f"F1 Score: {nb_f1:.2f}\n")
    f.write("\nClassification Report:\n")
    f.write(classification_report(y_test, nb_preds))

print("✅ Model results saved to output folder.")

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Sample dataset
data = {
    'Sore Throat': ['Yes', 'No', 'Yes', 'Yes', 'No', 'Yes', 'No', 'No'],
    'Congestion': ['No', 'No', 'Yes', 'Yes', 'No', 'Yes', 'No', 'No'],
    'Headache': ['Yes', 'No', 'Yes', 'Yes', 'No', 'Yes', 'No', 'No'],
    'Diagnosis': ['Flu', 'Healthy', 'Flu', 'Flu', 'Healthy', 'Flu', 'Healthy', 'Healthy']
}

# Create DataFrame
df = pd.DataFrame(data)
print("Original Dataset:\n", df)

# Label Encoding
le = LabelEncoder()
for col in df.columns:
    df[col] = le.fit_transform(df[col])

print("\nData after encoding:\n", df)

# Plotting category-wise counts
features = ['Sore Throat', 'Congestion', 'Headache']
for feature in features:
    plt.figure(figsize=(6, 4))
    sns.countplot(x=df[feature])
    plt.title(f"Category-wise count of '{feature}'")
    plt.xlabel("Category")
    plt.ylabel("Count")
    plt.show()

# Splitting features and target
X = df.drop('Diagnosis', axis=1)
y = df['Diagnosis']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# Train KNN model
knn = KNeighborsClassifier()
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)



# Evaluation
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

# Hyperparameter tuning
param_grid = {'n_neighbors': np.arange(1, 11)}  # Smaller range due to small dataset
grid_search = GridSearchCV(KNeighborsClassifier(), param_grid, cv=3)
grid_search.fit(X, y)

print("Best Parameters:", grid_search.best_params_)
print("Best Score:", grid_search.best_score_)

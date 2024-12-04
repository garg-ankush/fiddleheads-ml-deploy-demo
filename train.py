# Import necessary libraries
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pickle
import numpy as np

# Load the iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the model
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

with open('model.pkl', 'wb') as model_file:
    pickle.dump(model, model_file)


test_record = {
    "inputs": [6.1, 2.8, 4.7, 1.2]
}
r = np.array([test_record['inputs']])
print(r)

# Make predictions
predictions = model.predict(r)
print(predictions)


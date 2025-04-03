import numpy as np
from sklearn.linear_model import LinearRegression

# Create a sample dataset
X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)  # Input features (in this case, just one feature)
y = np.array([2, 4, 5, 4, 5])  # Target values

# Initialize the linear regression model
model = LinearRegression()

# Fit the model to the data
model.fit(X, y)

# Create a function to make predictions
def predict_value(input_feature):
    input_feature = np.array(input_feature).reshape(-1, 1)  # Ensure input is a 2D array
    prediction = model.predict(input_feature)
    return prediction[0]  # Return the predicted value

# Example usage:
input_feature = 6
prediction = predict_value(input_feature)
print(f"Predicted value for input {input_feature}: {prediction}")

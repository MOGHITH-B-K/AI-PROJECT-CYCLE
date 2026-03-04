# Sample dataset
x = [1, 2, 3, 4, 5]
y = [2, 4, 5, 4, 5]

n = len(x)

# Initialize parameters
m = 0
b = 0

learning_rate = 0.01
epochs = 1000

# Gradient Descent Loop
for epoch in range(epochs):
    
    dm = 0
    db = 0
    
    # Calculate gradients
    for i in range(n):
        y_pred = m * x[i] + b
        error = y_pred - y[i]
        
        dm += error * x[i]
        db += error
    
    # Average gradients
    dm = (2/n) * dm
    db = (2/n) * db
    
    # Update parameters
    m = m - learning_rate * dm
    b = b - learning_rate * db

# Final model
print("Slope (m):", m)
print("Intercept (b):", b)

# Prediction
x_test = 6
y_pred = m * x_test + b
print("Predicted value for x =", x_test, "is", y_pred)

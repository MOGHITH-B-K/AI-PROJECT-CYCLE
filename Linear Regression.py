# Taking number of data points
n = int(input("Enter number of data points: "))

x = []
y = []

# Taking input values
for i in range(n):
    x_value = float(input("Enter X value: "))
    y_value = float(input("Enter Y value: "))
    x.append(x_value)
    y.append(y_value)

# Initialize sums
sum_x = 0
sum_y = 0
sum_xy = 0
sum_x2 = 0

# Calculating required summations
for i in range(n):
    sum_x += x[i]
    sum_y += y[i]
    sum_xy += x[i] * y[i]
    sum_x2 += x[i] * x[i]

# Calculating slope (m)
m = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x * sum_x)

# Calculating intercept (b)
b = (sum_y - m * sum_x) / n

print("Slope (m):", m)
print("Intercept (b):", b)

# Predicting value
x_test = float(input("Enter X value to predict Y: "))
y_pred = m * x_test + b

print("Predicted Y value:", y_pred)

data = [2, 4, 6, 8]

# Mean
total = 0
for i in range(len(data)):
    total += data[i]

mean = total / len(data)

# Variance
sq_diff = 0
for i in range(len(data)):
    diff = data[i] - mean
    sq_diff += diff * diff

variance = sq_diff / len(data)

# Standard Deviation
std_dev = variance ** 0.5

print("Standard Deviation =", std_dev)

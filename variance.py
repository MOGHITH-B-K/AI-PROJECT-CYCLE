data = [2, 4, 6, 8]

# Step 1: Calculate mean
total = 0
for i in range(len(data)):
    total += data[i]

mean = total / len(data)

# Step 2: Calculate squared differences
sq_diff = 0
for i in range(len(data)):
    diff = data[i] - mean
    sq_diff += diff * diff

# Step 3: Divide by number of elements
variance = sq_diff / len(data)

print("Variance =", variance)

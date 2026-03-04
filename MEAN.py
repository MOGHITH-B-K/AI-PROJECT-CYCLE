# List of numbers
numbers = [10, 20, 30, 40, 50]

# Step 1: Find total sum
total = 0
for num in numbers:
    total = total + num

# Step 2: Count total numbers
count = 0
for num in numbers:
    count = count + 1

# Step 3: Calculate mean
mean = total / count

# Output
print("Mean:", mean)
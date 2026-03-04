# Taking number of elements from user
n = int(input("Enter the number of elements: "))

numbers = []

# Taking elements as input
for i in range(n):
    value = float(input("Enter number: "))
    numbers.append(value)

# -------- Sorting the list manually --------
for i in range(n):
    for j in range(i + 1, n):
        if numbers[i] > numbers[j]:
            numbers[i], numbers[j] = numbers[j], numbers[i]

# -------- Finding Median --------
if n % 2 == 0:
    median = (numbers[n//2 - 1] + numbers[n//2]) / 2
else:
    median = numbers[n//2]

# Display result
print("Median =", median)
# Taking number of elements from user
n = int(input("Enter the number of elements: "))

numbers = []

# Taking elements as input
for i in range(n):
    value = float(input("Enter number: "))
    numbers.append(value)

# -------- Finding Frequency --------
frequency = {}

for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

# -------- Finding Mode --------
max_count = 0
mode = None

for key in frequency:
    if frequency[key] > max_count:
        max_count = frequency[key]
        mode = key

# Display result
print("Mode =", mode)

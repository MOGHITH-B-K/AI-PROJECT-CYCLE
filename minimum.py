data = [2, 9, 4, 7]

min_value = data[0]

for i in range(len(data)):
    if data[i] < min_value:
        min_value = data[i]

print("Minimum =", min_value)

data = [2, 9, 4, 7]

max_value = data[0]

for i in range(len(data)):
    if data[i] > max_value:
        max_value = data[i]

print("Maximum =", max_value)

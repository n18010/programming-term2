data = [i for i in range(2000, 2101)
        if i % 4 == 0 and i % 100 != 0 or i % 400 == 0]

print(data)

data = ["アホ" if i % 3 == 0 or i // 10 == 3 or i % 10 == 3 else str(i)
        for i in range(1, 41)]

print(data)

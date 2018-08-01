num_list = list(range(1, 41))

num3_func = lambda x: x % 3 == 0 or x // 10 == 3 or x % 10 == 3

print(list(filter(num3_func, num_list)))

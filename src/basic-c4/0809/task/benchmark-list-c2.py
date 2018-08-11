from datetime import datetime

s_time = datetime.now()
print(s_time)

data = [i for i in range(1, 1000000)]

f_time = datetime.now()
print(f_time)

print(f_time - s_time)

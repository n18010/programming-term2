# 掛け算九九を表形式で表示する
# 掛ける数の表示
str_line = ""
str_line = str_line + "|".rjust(3)
for i in range(1, 10):
    str_line = str_line + str(i).rjust(3)
print(str_line)

# 線の表示
str_line = ""
str_line = str_line + ("-" * 2) + "+" + ("-" * 27)
print(str_line)

# 掛けられる数と乗算結果の表示
for x in range(1, 10):
    str_line = ""
    str_line = str_line + str(x).rjust(2)
    str_line = str_line + "|"
    for y in range(1, 10):
        str_line = str_line + str(x * y).rjust(3)
    print(str_line)

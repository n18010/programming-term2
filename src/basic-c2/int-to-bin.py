# 変数の初期化
target_num = 100
amari = 0
sho = target_num
result_str = ""
devided_by = 2

# 商が1になるまで割り切る
while sho > 1:
    amari = target_num % devided_by
    sho = target_num // devided_by
    target_num = sho
    result_str = str(amari) + result_str

print(str(sho) + result_str)

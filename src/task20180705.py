# 支払い金額を求める
# 価格
beer_v = 200
otumami_v = 100
yakitori_v = 100

# 個数
beer_c = 2
otumami_c = 1
yakitori_c = 2

# 割引率
yakitori_rate = 0.2

# 使用ポイント数
point = 150

# 計算
beer_sum = beer_v * beer_c
otumami_sum = otumami_v * otumami_c
yakitori_sum = yakitori_v * (1 - yakitori_rate) * yakitori_c
payment = beer_sum + otumami_sum + yakitori_sum - point

# 結果を表示
print("支払金額", payment, "円")

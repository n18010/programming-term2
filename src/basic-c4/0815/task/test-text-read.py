# ファイルを読み込んで辞書型に変換
records = {}
with open("test-record.txt", encoding="utf-8") as tf:
    for line in tf:
        lis = line.split(",")
        records[lis[0]] = int(lis[1])

# 合計を求める
sum_v = 0
for v in records.values():
    sum_v += v

# 平均点を計算して結果を表示
ave_v = sum_v / len(records)
print("合計点:", sum_v)
print("平均点:", ave_v)

# 成績データの一覧と平均点との差を表示
fmt = "| {0:<7} | {1:>4} | {2:>5}"
print("| 名前    | 点数 | 差")
for name, v in sorted(records.items()):
    # 平均点との差を求める
    diff_v = v - ave_v
    # 小数点以下を丸める
    diff_v = round(diff_v, 1)
    # 書式にそって出力
    print(fmt.format(name, v, diff_v))

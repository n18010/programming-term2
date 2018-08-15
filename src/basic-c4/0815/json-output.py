import json

# 辞書型のデータ
data = {
    "no": 5,   # 数値
    "code": ("jas", 1, 19),   # タプル
    "src": "be quick to listen, slow to speak, slow to anger",   # 文字列
}

# ファイルへ書き込む
filename = "test.json"
with open(filename, "w") as fp:
    json.dump(data, fp)   # JSON形式で保存

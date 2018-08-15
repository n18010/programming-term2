import json

# ファイルから読み込む
filename = "test.json"
with open(filename, "r") as fp:
    r = json.load(fp)   # JSON形式のファイルから読み込む
    print("no=", r["no"])
    print("code=", r["code"])
    print("src=", r["src"])

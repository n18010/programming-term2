# 絶対に勝てないじゃんけん
# ユーザーの入力
janken = input("何を出しますか? 1:グー、2:チョキ、3:パー ")

# 結果メッセージ
message = "CPUが{0}を出しました。あなたの負けです。"

# 負ける条件式
if janken == "1":
    print(message.format("パー"))
elif janken == "2":
    print(message.format("グー"))
elif janken == "3":
    print(message.format("チョキ"))
else:
    print("入力が不正です。終了します。")

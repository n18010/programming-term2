import re

user = input("全角カナの文字を入力してください>> ")

zen_kana = re.match(r'[ァ-ヴ・ー]+$', user)
if zen_kana is not None:
    print("すべてが全角カタカナである")
else:
    print("すべてが全角カタカナではない")

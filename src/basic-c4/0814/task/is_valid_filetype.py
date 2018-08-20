import re

user = input("テキスト形式のファイル名を入力してください>> ")

ng_name = re.match(r".*[/,<=>!?#$*+\\].*", user)

if ng_name is None:
    txt_type = re.match(r".+\.txt$", user)
    if txt_type is not None:
        print('{0}は拡張子が".txt"のテキストファイルです'.format(user))
    else:
        print('{0}は拡張子が".txt"のテキストファイルではありません'.format(user))
else:
    print("不正な文字がふくまれています")

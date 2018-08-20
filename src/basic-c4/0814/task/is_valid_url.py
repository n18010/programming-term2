import re

user = input("URLを入力してください>> ")

url = re.match(r'https?://[\w:%#$&?()~.=+-]+', user)

if url is not None:
    print("{0}はURLの形式です".format(user))
else:
    print("{0}はURLの形式ではありません".format(user))

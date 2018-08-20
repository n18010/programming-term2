import re

user = input("メールアドレスを入力してください>> ")

email = re.match(r"[A-Za-z0-9._%-+]+@[A-Za-z0-9.-]+\.[A-Za-z]+$", user)

if email is not None:
    print("{0}はメールアドレスの形式です".format(user))
else:
    print("{0}はメールアドレスの形式ではありません".format(user))

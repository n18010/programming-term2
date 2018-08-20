import re

user = input("電話番号を入力してください>> ")

phone_regex = re.compile(r'''(
    (\d{1,4}|\(\d{1,4}\))
    (\s|-)
    (\d{1,4})
    (\s|-)
    (\d{3,4})
    (\s*(ext|x|ext.)\s*(\d{2,5}))?
    )''', re.VERBOSE)

phone_no = phone_regex.match(user)

if phone_no is not None:
    print("{0}は電話番号の形式です".format(user))
else:
    print("{0}は電話番号の形式ではありません".format(user))

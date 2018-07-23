operator_dict = {
    '+': 1,
    '-': 2,
    '*': 3,
    '/': 4
}
sentence = "結果は{0}です。"


def add(a, b):
    """
    足し算をする

    Parameters
    ----------
    a : int, float
    b : int, float

    Returns
    -------
    int, float
        足し算の結果
    """
    return a + b


def sub(a, b):
    """
    引き算をする

    Parameters
    ----------
    a : int, float
        引かれる数
    b : int, float
        引く数

    Returns
    -------
    int, float
        引き算の結果
    """
    return a - b


def mul(a, b):
    """
    掛け算をする

    Parameters
    ----------
    a : int, float
    b : int, float

    Returns
    -------
    int, float
        掛け算の結果
    """
    return a * b


def div(a, b):
    """
    割り算をする

    Parameters
    ----------
    a : int, float
        割られる数
    b : int, float
        割る数

    Returns
    -------
    float
        割り算の結果
    """
    try:
        return a / b
    except ZeroDivisionError:
        print("0で割らないでください。")


print("四則計算プログラムです。")

while True:
    user = input("第1パラメータを入力してください>>> ")
    try:
        num1 = float(user)
        break
    except ValueError:
        print("入力が間違っています。数値を入力してください。")

while True:
    user = input("第2パラメータを入力してください>>> ")
    try:
        num2 = float(user)
        break
    except ValueError:
        print("入力が間違っています。数値を入力してください。")

while True:
    user = input("演算方法を入力してください>>> ")
    if user in operator_dict:
        if operator_dict[user] == 1:
            print(sentence.format(round(add(num1, num2), 3)))
            print(help(add))
            break
        if operator_dict[user] == 2:
            print(sentence.format(round(sub(num1, num2), 3)))
            print(help(sub))
            break
        if operator_dict[user] == 3:
            print(sentence.format(round(mul(num1, num2), 3)))
            print(help(mul))
            break
        if operator_dict[user] == 4:
            try:
                print(sentence.format(round(div(num1, num2), 3)))
                print(help(div))
                break
            except TypeError:
                print("終了します。")
                break
    else:
        print("入力が間違っています。「 +, -, *, / 」から選んでください。")

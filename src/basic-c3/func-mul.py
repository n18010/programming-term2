# かけ算を行うだけの関数を定義
def mul(a, b):
    """
    掛け算を行う

    Parameteers
    -----------
    a : int
        掛ける数
    b : int
        掛けられる数

    Returns
    -------
    int
        掛け算結果
    """
    return a * b


# 定義した関数を使う
print(mul(2, 3))
print(mul(10, 3))

help(mul)

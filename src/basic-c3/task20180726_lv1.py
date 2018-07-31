# 自動双六プログラム ゴールちょうどじゃないバージョン

goal = 10  # 双六のゴール値

cur_x = 0  # 前に進んだ値の合計のための変数


def shake_dice():
    """
    1から6のサイコロの目をランダムに出す。

    Parameters
    ----------
    なし

    Returns
    -------
    dice : int
        1から6のランダムな値
    """
    from random import randint
    global dice
    dice = randint(1, 6)
    return dice


def go_forward(n):
    """
    前に進んだ値の合計を出す。

    Parameters
    ----------
    n : int
        前に進む値

    Returns
    -------
    なし
    """
    global cur_x
    cur_x += n


while cur_x < goal:
    input("サイコロを振ってください")
    go_forward(shake_dice())
    if cur_x < goal:
        print("{0}が出ました。現在位置は{1}です。".format(dice, cur_x))

print("{0}が出ました。おめでとうございます、ゴールしました！".format(dice))

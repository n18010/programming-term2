import calc_tax


def exec():
    """
    メインロジックを実行する
    Parameters
    ----------
    なし
    Returns
    -------
    list
        表示されるメッセージを要素に含むリスト
    """

    # 単価を管理するdictionary
    unit_dc = {
        'Banana': 100,
        'Apple': 200,
        'Orange': 150
    }
    # 個数を管理するdictionary
    nums_dc = {
        'Banana': 2,
        'Apple': 1,
        'Orange': 3
    }
    money = 2000    # 所持金
    total_ex_tax = 0    # 税抜き合計
    res_list = []   # 結果として返すリスト
    text01 = "{0}を{1}個買いました。商品計は{2}円です。"
    text02 = "総計の税抜き額は{0}円、税込額は{1}円です。"
    text03 = "残金は{0}円です。"

    for name, price in unit_dc.items():
        unit_total = price * nums_dc[name]  # 商品ごとの合計
        res_list.append(text01.format(name, nums_dc[name], unit_total))
        total_ex_tax += unit_total

    total_in_tax = round(calc_tax.calc_incl_tax(total_ex_tax))  # 税込み総額
    res_list.append(text02.format(total_ex_tax, total_in_tax))

    res_list.append(text03.format(money - total_in_tax))

    return res_list


def display(msgs):
    """
    結果を表示する
    Parameters
    ----------
    msgs: list
        表示するメッセージが格納されたリスト
    Returns
    -------
    なし
    """
    print("\n".join(msgs))


# メイン処理
if __name__ == '__main__':
    display(exec())

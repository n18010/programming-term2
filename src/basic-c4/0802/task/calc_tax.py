# 消費税率
TAX_RATE = 8


def calc_incl_tax(excl_tax):
    """
    税込み金額を計算する

    Parameters
    ----------
    excl_tax: int
        税抜き金額

    Returns
    -------
    int
        税込み金額
    """
    return excl_tax * (1 + TAX_RATE / 100)


if __name__ == '__main__':
    print(calc_incl_tax(100))

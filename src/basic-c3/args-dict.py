def print_args(**args):
    """
    引数を表示する。

    Parametrs
    ---------
    args : object[]
        キーと値の組み合わせ

    Returns
    -------
    なし
    """
    print(args)


print_args(a=30, b=50, c=40)
print_args(aa="hoge", bb="fuga")

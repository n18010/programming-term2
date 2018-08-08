from datetime import datetime, timedelta


def process(target_date):
    """
    メインロジックを実行する
    Parameters
    ----------
    target_date : datetime
        処理対象の日付
    Returns
    -------
    list
        表示されるメッセージを要素に含むリスト
    """

    res_list = []   # 結果として返すリスト

    w = target_date.strftime("%a")   # 曜日を取得
    ymd = target_date.strftime("%Y/%m/%d")

    if w == "Sat":
        res_list.append("{0} は {1} です。平日ではありません。".format(ymd, w))

        t = target_date + timedelta(days=2)   # 2日後の日付を取得
        res_list.append("次の平日は {0} です。".format(t.strftime("%Y/%m/%d")))

    elif w == "Sun":
        res_list.append("{0} は {1} です。平日ではありません。".format(ymd, w))

        t = target_date + timedelta(days=1)   # 1日後の日付を取得
        res_list.append("次の平日は {0} です。".format(t.strftime("%Y/%m/%d")))

    else:
        res_list.append("{0} は {1} です。平日です。".format(ymd, w))

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
    print(*msgs, sep="\n")


# メイン処理
if __name__ == '__main__':
    while True:
        try:
            input_date = input('日付を入力してください。')
            target_date = datetime.strptime(input_date, '%Y/%m/%d')

            display(process(target_date))
            break
        except:
            print('入力された日付が不正です。再入力してください。')

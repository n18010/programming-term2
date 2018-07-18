main_menu = {
    'DripCoffee': 280, 'ColdBrewCoffee': 320, 'CafeLatte': 330,
    'SoyLatte': 380, 'Cappuccino': 330, 'CaramelFrappuccino': 470,
    'MacchaCreamFrappuccino': 470
}
option_menu = {
    'LowFatMilk': 0, 'NonFatMilk': 0, 'SoyMilk': 50, 'DeepCoffee': 60,
    'WhipCream': 70, 'CaramelShrup': 60, 'ChocoSource': 0, 'DeCafe': 50
}
order_list = []
sum_v = 0
is_ordering = True
sentence = """
注文内容は{0}です。
合計金額は{1}円です。右奥のカウンターにてお待ちください。
"""

while is_ordering:
    order = input("メインメニューを選んでください ")
    if order == "" or order == "q":
        print("注文をキャンセルしました")
        break
    elif order in main_menu:
        order_list.append(order)
        sum_v += main_menu[order]
        order = input("オプションメニューを選んでください ")
        while True:
            if order == "" or order == "q":
                print(sentence.format(order_list, sum_v))
                is_ordering = False
                break
            elif order in option_menu:
                order_list.append(order)
                sum_v += option_menu[order]
                order = input("他にオプションメニューの注文はございますか？ ")
                continue
            else:
                print("選択されたオプションはありません")
                order = input("他にオプションメニューの注文はございますか？ ")
                continue
    else:
        print("選択されたメニューはありません")
        continue

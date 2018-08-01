TAX_RATE = 8

price_list = [13600, 14500, 16000, 11111, 11667]

tax_func = lambda x: int(round(x * (1 + TAX_RATE / 100), -1))

print(list(map(tax_func, price_list)))

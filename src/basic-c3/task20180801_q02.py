TAX_RATE = 10

price_list = [13600, 14500, 16000, 11111, 11667]

tax_func = lambda x: round(x * (1 + TAX_RATE / 100))

print(list(map(tax_func, price_list)))

from random import randint

a = "{0}の天気は{1}です。気温は{2}度です。"
when = ["今日", "明日", "明後日"]
weather = ["晴れ", "曇り", "雨"]

i = randint(0, len(when)-1)
j = randint(0, len(weather)-1)
k = randint(20, 40)
print(a.format(when[i], weather[j], str(k)))

age_dict = {
    "Aiba": 35,
    "Matsumoto": 34,
    "Ninomiya": 35,
    "Oono": 37,
    "Sakurai": 36
}

old_list = sorted(age_dict.items(), key=lambda x: x[1], reverse=True)

for name, age in old_list:
    print(name, age)

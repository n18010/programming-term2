height_dict = {
    "Aiba": 175,
    "Matsumoto": 172,
    "Ninomiya": 168,
    "Oono": 166,
    "Sakurai": 171
}

tall_list = sorted(height_dict.items(), key=lambda x: x[1])

for name, height in tall_list:
    print(name, height)

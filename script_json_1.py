import json


with open('todos.json', 'r', encoding='utf-8') as file:
    temp = json.load(file)

temp_2 = {
    'userId': 1,
    'title_c': '',
    'title_u': ''
    }

temp_3 = []
# temp_3 = {key: [] for key in temp}

# for i in temp:
#     temp_3.append(i)

temp_3 = [i for i in temp]

print(temp_3)
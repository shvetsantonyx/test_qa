import datetime as dt
import json
import os


create_file_time = dt.datetime.strftime(dt.datetime.now(), '%Y-%m-%dT%H-%M')
report_time = dt.datetime.strftime(dt.datetime.now(), '%Y.%m.%d %H:%M')

# Функция для выполненных\невыполненных задач
def report_func(file_, userid, complited):
    report = ''
    try:
        for element in file_:
            if element['userId'] == userid:
                if element['completed'] == complited:
                    if len(element['title']) > 50:
                        report += element['title'][:50] + '...' + '\n'
                    else:
                        report += element['title'] + '\n'
    except: KeyError
    return report


with open('todos.json', 'r', encoding='utf-8') as file:
    temp = json.load(file)
    
for element in temp:
    files_in_dir = os.listdir()
    try:
        file_name = str(element['userId']) + '_' + create_file_time
        if file_name not in files_in_dir:
            f = open(f'{file_name}' + '.txt', 'w', encoding='utf-8')
            f.write('Сотрудник №' + str(element['userId']) + '\n')
            f.write(report_time + '\n' + '\n')
            f.write('## Завершённые задачи:' + '\n')
            f.write(report_func(temp, element['userId'], True))
            f.write('\n')
            f.write('## Оставшиеся задачи:' + '\n')
            f.write(report_func(temp, element['userId'], False))
            f.close()

    except: KeyError

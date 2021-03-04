# data.json - файл с данными о некоторых математиках прошлого.
# 1. Необходимо написать функцию, которая считает эти данные из файла. Параметр функции - имя файла.
# 2. Написать функцию сортировки данных по ФАМИЛИИ в поле "name" (у тех у кого она есть).
# Например для Rene Descartes фамилия это Descartes, у Pierre de Fermat - Fermat и т.д.
# Если фамилии нет, то использовать имя, например Euclid.
# 3. Написать функцию сортировки по дате смерти из поля "years".
# Обратите внимание на сокращение BC. - это означает до н.э.
# 4. Написать функцию сортировки по количеству слов в поле "text"

import re
import json

# 1)


def read_json(filename):
    with open(filename, 'r') as json_file:
        data = json.load(json_file)
    return data


data = read_json('data.json')

# 2)


def sort_by_surname(sort_dict):
    return sort_dict['name'].split()[-1]


data = sorted(data, key=sort_by_surname)

print("\nSorted by surname:\n")
for i in range(9):
    # data[i]['name'] = ' '.join(data[i]['name'])
    print(data[i]['name'])

# 3)


def sort_by_age(sort_dict):
    years = re.findall(r"[0-9]+", sort_dict['years'])
    sort_dict['years'] = sort_dict['years'].split()
    # if sort_dict['years'].count('BC.') >= 1:
    if "BC." in sort_dict['years']:
        return int(years[-1]) * -1
    else:
        return int(years[-1])


data = sorted(data, key=sort_by_age)

print("\nSorted by the year of the death:\n")
for i in range(9):
    print(' '.join(data[i]['years']))

# 4)


def sort_by_len_text(sort_dict):
    return len(sort_dict['text'])


data = sorted(data, key=sort_by_len_text)

print("\nSorted by length of the 'text':\n")
for i in range(9):
    print(data[i]['text'], '\n')
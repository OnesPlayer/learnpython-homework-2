import csv
with open('Untitled-1.csv', 'w', encoding='utf-8') as f:
    user_list = [
        {'name': 'Маша', 'age': 25, 'job': 'Scientist'}, 
        {'name': 'Вася', 'age': 8, 'job': 'Programmer'}, 
        {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
            ]
    fieldnames = ['name', 'age', 'job']
    result = csv.DictWriter(f, fieldnames, user_list, delimiter = ' ')
    result.writeheader()
    for user in user_list:
        result.writerow(user)

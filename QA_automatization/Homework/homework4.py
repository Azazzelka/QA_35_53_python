import csv
import json


def save_shopping_list(items):
    with open('shopping.txt', 'w', encoding='utf-8') as file:
        for item in items:
            file.write(f'{item}\n')

items = [
    "Milk",
    "Bread",
    "Apples",
    "Coffee"
]
save_shopping_list(items)

with open('students.csv', 'w', encoding='utf-8') as file:
    writer = csv.writer(file)

    writer.writerow(['name','age'])
    writer.writerow(['Anna', '21'])
    writer.writerow(['Tom', '19'])
    writer.writerow(['Kate', '22'])

def read_students(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(f'Student: {row['name']} ({row['age']})')

read_students('students.csv')

def save_profile(name,age,city):
    profil = {'name':name, 'age':age,'city':city}
    with open('profile.json', 'w', encoding='utf-8') as file:
        json.dump(profil,file, indent=2)

save_profile('Vova', 29, 'Tel-aviv')

from pathlib import Path

def create_reports_folder():
    folder = Path('reports')
    folder.mkdir(exist_ok=True)
    file = folder/'result.txt'
    with open(file, 'w', encoding='utf-8') as f:
        f.write('Homework completed successfully')

create_reports_folder()

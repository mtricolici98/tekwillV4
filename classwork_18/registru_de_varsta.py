import json
from datetime import datetime

from dateutil.relativedelta import relativedelta

list_of_persons = []
DATE_FORMAT = '%m/%d/%Y'


def load_list():
    global list_of_persons
    try:
        with open('registry_age.json', 'r') as file:
            json_data = json.load(file)
        list_of_persons = []
        for person in json_data:
            list_of_persons.append(
                dict(
                    name=person['name'],
                    birthday=datetime.strptime(person['birthday'], DATE_FORMAT)
                )
            )
    except Exception as ex:
        print(ex)
        list_of_persons = []


def save_llist():
    to_save = []
    for person in list_of_persons:
        to_save.append(
            {'name': person['name'], 'birthday': person['birthday'].strftime(DATE_FORMAT)}
        )
    with open('registry_age.json', 'w') as file:
        json.dump(to_save, file)


def add_person():
    name = input("What is your name? ")
    while True:
        try:
            birthday = input("When is your birthday? Ex: dd/mm/yyyy")
            birthday = datetime.strptime(birthday, "%d/%m/%Y")
            break
        except ValueError:
            print("Invalid date format")
    list_of_persons.append(
        {
            'name': name,
            'birthday': birthday
        }
    )


def show_all_ages():
    time_now = datetime.now()
    for person in list_of_persons:
        date = person['birthday']
        years = relativedelta(time_now, date).years
        print(f"Name: {person['name']}, is: {years} years")


def main():
    load_list()
    print('Choose:')
    print('1. Add a person')
    print('2. Show all ages')
    print('0. Exit')
    match int(input('Enter')):
        case 1:
            add_person()
            save_llist()
        case 2:
            show_all_ages()
        case 0:
            exit()


if __name__ == '__main__':
    while True:
        main()

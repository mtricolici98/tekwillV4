import json
from datetime import datetime


def list_all_employee_names():
    path = r"employee_data.json"
    print("\nEmployees list: ")
    s = "-"
    print(s * 34)
    try:
        with open(path, 'r') as the_file:
            information_in_file = json.loads(the_file.read())
        for i in information_in_file:
            for key in i:
                if key == 'name':
                    print(i[key])
    except FileNotFoundError:
        pass
    except json.JSONDecodeError:
        pass
    print(s * 34)


def list_all_position_names():
    path = r"employee_data.json"
    print("\nPosition names: ")
    s = "-"
    print(s * 34)
    position_names_list = []
    try:
        with open(path, 'r') as the_file:
            information_in_file = json.loads(the_file.read())
        for i in information_in_file:
            for key in i:
                if key == 'position':
                    position_names_list.append(i[key])
        set_position_names_list = set(position_names_list)
        position_print = list(set_position_names_list)
        for i in position_print:
            print(i)
    except FileNotFoundError:
        pass
    except json.JSONDecodeError:
        pass
    print(s * 34)


def calculate_total_salary_per_month():
    path = r"employee_data.json"
    print("\nTotal salary to be paid per month: ")
    s = "-"
    print(s * 34)
    suma = 0
    try:
        with open(path, 'r') as the_file:
            information_in_file = json.loads(the_file.read())
        for i in information_in_file:
            for key in i:
                if key == 'salary':
                    suma += i[key]
        x = str(suma) + " EUR"
        print(x.center(34, " "))
    except FileNotFoundError:
        pass
    except json.JSONDecodeError:
        pass
    print(s * 34)


def calculate_total_taxes_per_month():
    path = r"employee_data.json"
    taxes_percent = float(input("Please type the Tax % to be calculated: "))
    round_nr = int(input("How many numbers we should round the result to: "))
    print("\nTotal amount of taxes to be paid per month: ")
    s = "-"
    print(s * 34)
    suma = 0
    taxes = 0
    try:
        with open(path, 'r') as the_file:
            information_in_file = json.loads(the_file.read())
        for i in information_in_file:
            for key in i:
                if key == 'salary':
                    suma += i[key]
        taxes = taxes_percent * suma / 100
        x = str(round(taxes, round_nr)) + " EUR"
        print(x.center(34, " "))
    except FileNotFoundError:
        pass
    except json.JSONDecodeError:
        pass
    print(s * 34)


def display_top_10_highest_paid_employees():
    path = r"employee_data.json"
    display_salaries = str.lower(input("\nWould you like to display also the salaries ? / Y or hit enter  "))
    header = "The top 10 highest paid employees".center(82)
    print("\n", header)
    s = "-"
    if display_salaries == 'y':
        print(s * 82)
        print("|" + "Name".center(18) + "|" + "Position".center(31) + "|" + "Salary".center(5) + "|"
              + "Employment_start_date".center(22) + "|")
        print(s * 82)
    else:
        print(s * 78)
        print("|" + "Name".center(20) + "|" + "Position".center(33) + "|" + "Employment_start_date".center(21) + "|")
        print(s * 78)
    salaries_list = []
    try:
        with open(path, 'r') as the_file:
            information_in_file = json.loads(the_file.read())
        for i in information_in_file:
            for key in i:
                if key == 'salary':
                    salaries_list.append(i[key])
        salaries_list2 = []
        for j in range(0, 10):
            x = max(salaries_list)
            index = salaries_list.index(x)
            salaries_list2.append(salaries_list.pop(index))
        j = 0
        while j <= 9:
            for i in information_in_file:
                for key in i:
                    if key == 'salary' and i[key] == salaries_list2[j]:
                        if display_salaries == 'y':
                            print(f"|{str(i['name']).ljust(18)}|{str(i['position']).rjust(31)}|"
                                  f"{str(i['salary']).rjust(6)}|{str(i['employee_from']).rjust(22)}|")
                        else:
                            print(f"|{str(i['name']).ljust(20)}|{str(i['position']).rjust(33)}|"
                                  f"{str(i['employee_from']).rjust(21)}|")
            j += 1
    except FileNotFoundError:
        pass
    except json.JSONDecodeError:
        pass
    if display_salaries == 'y':
        print(s * 81)
    else:
        print(s * 78)


def display_top_10_longest_working_time_employees():
    path = r"employee_data.json"
    display_salaries = str.lower(input("\nWould you like to display also the salaries ? / Y or hit enter  "))
    header = "The top 10 employees with the longest time in the company".center(82)
    print("\n", header)
    s = "-"
    if display_salaries == 'y':
        print(s * 82)
        print("|" + "Name".center(18) + "|" + "Position".center(31) + "|" + "Salary".center(5) + "|"
              + "Employment_start_date".center(22) + "|")
        print(s * 82)
    else:
        print(s * 78)
        print("|" + "Name".center(20) + "|" + "Position".center(33) + "|" + "Employment_start_date".center(21) + "|")
        print(s * 78)
    start_date_list = []
    try:
        with open(path, 'r') as the_file:
            information_in_file = json.loads(the_file.read())
        for i in information_in_file:
            for key in i:
                if key == 'employee_from':
                    z = i[key]
                    date_temp = datetime.strptime(z, '%m/%d/%Y').date()
                    start_date_list.append(date_temp)
        start_date_list_temp = []
        for j in range(0, 10):
            x = min(start_date_list)
            index = start_date_list.index(x)
            start_date_list_temp.append(start_date_list.pop(index))
        start_date_list2 = []
        for z in start_date_list_temp:
            start_date_list2.append(str(z.strftime("%m/%d/%Y")))
        j = 0
        while j <= 9:
            for i in information_in_file:
                for key in i:
                    if key == 'employee_from' and i[key] == start_date_list2[j]:
                        if display_salaries == 'y':
                            print(f"|{str(i['name']).ljust(18)}|{str(i['position']).rjust(31)}|"
                                  f"{str(i['salary']).rjust(6)}|{str(i['employee_from']).rjust(22)}|")
                        else:
                            print(f"|{str(i['name']).ljust(20)}|{str(i['position']).rjust(33)}|"
                                  f"{str(i['employee_from']).rjust(21)}|")
            j += 1
    except FileNotFoundError:
        pass
    except json.JSONDecodeError:
        pass
    if display_salaries == 'y':
        print(s * 81)
    else:
        print(s * 78)


def main():
    while True:
        print('\nChoose the number corresponding to your option')
        print('1. List all employee names')
        print('2. List all position names (without repeating the same position)')
        print('3. Calculate the amount of salary the company has to pay per month in total')
        print('4. Calculate the amount of money the company has to pay in taxes per month')
        print('5. Display information for the top 10 highest paid employees')
        print('6. Display information for the top 10 employees with the longest time in the company')
        print('Type quit to quit the program')
        main_option = input('Choose: ')
        match main_option:
            case '1':
                list_all_employee_names()
            case '2':
                list_all_position_names()
            case '3':
                calculate_total_salary_per_month()
            case '4':
                calculate_total_taxes_per_month()
            case '5':
                display_top_10_highest_paid_employees()
            case '6':
                display_top_10_longest_working_time_employees()
            case 'quit':
                print('Goodbye')
                break
            case _:
                print('Wrong choice')


if __name__ == "__main__":
    main()


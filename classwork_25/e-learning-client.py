import json

import requests


class CourseClient:

    def __init__(self, base_url):
        self.base_url = base_url
        self.token = ''
        self.headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json, text/plain, */*'
        }

    def get_course_list(self):
        response = requests.get(f"{self.base_url}/api/lms/course/list/", headers=self.headers)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            raise Exception(f"Server responses with {response.status_code}")

    def get_lesson_list_for_course(self, id_):
        response = requests.get(f"{self.base_url}/api/lms/course/get/{id_}/", headers=self.headers)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            raise Exception(f"Server responses with {response.status_code}")

    def get_profile_info(self):
        response = requests.get(f"{self.base_url}/api/auth/profile", headers=self.headers)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            raise Exception(f"Server responses with {response.status_code}")

    def register(self, email, name, password):
        payload = {'profile': {'name': name}, 'email': email, 'password': password}
        response = requests.post(f"{self.base_url}/api/auth/signup", data=json.dumps(payload))
        if response.status_code == 200:
            return True
        else:
            return False

    def login(self, email, password):
        response = requests.post(f"{self.base_url}/api/auth/signin", data=json.dumps(
            {'email': email, 'password': password}
        ), headers=self.headers)
        if response.status_code == 200:
            data = response.json()
            self.headers['Authorization'] = f"Bearer {data['token']}"
            return True
        else:
            return False


client = CourseClient('http://80.240.31.3')


def get_course_view():
    try:
        course_list = client.get_course_list()
        for course in course_list:
            print(f"{course['id']} | {course['title']} | {course['description'][:20]}...")
    except Exception as ex:
        print(ex)


def get_lesson_view():
    course_id = input('Enter course id:')
    try:
        course_dict = client.get_lesson_list_for_course(course_id)
        for lesson in course_dict['lessons']:
            print(f"{lesson['id']} | {lesson['title']} | {lesson['summary'][:20]}...")
    except Exception as ex:
        print(ex)


def auth_menu():
    print('1. Login')
    print('2. Register')
    choose_option = input("Enter")
    match choose_option:
        case '1':
            client.login(input("Email"), input("Password"))
        case '2':
            client.register(input("Email"), input("User"), input("Password"))


while True:
    profile = None
    try:
        profile = client.get_profile_info()
        print(f'Logged in as: {profile["data"][0]["name"]}')
    except Exception as ex:
        print("Not logged in ")
        auth_menu()
    if not profile:
        continue
    print('1. Get course list')
    print('2. Get course lessons by id')
    choose_option = input("Enter")
    match choose_option:
        case '1':
            get_course_view()
        case '2':
            get_lesson_view()

import json
import random
import time


def json_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return json.dumps(result)

    return wrapper


@json_decorator
def return_data():
    return ['1', 2, 3, 4, {'name': "Marius"}]


print(return_data())


def print_execution_time(funct):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        function_result = funct(*args, **kwargs)
        end_time = time.time()
        print(f"The function took {end_time - start_time} seconds to complete")
        return function_result

    return wrapper


@print_execution_time
def function_that_takes_long_time():
    time.sleep(random.randint(1, 5))


@print_execution_time
def function_that_takes_short_time():
    time.sleep(random.randint(1, 2) / 2)


function_that_takes_long_time()


function_that_takes_short_time()
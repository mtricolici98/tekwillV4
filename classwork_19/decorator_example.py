def my_decorator(function_to_run):
    def wrapper(*args, **kwargs):
        print("Im doing something")
        function_to_run(*args, **kwargs)
        print("Im done")

    return wrapper


@my_decorator
def my_function():
    print("Hello World!")


@my_decorator
def other_function():
    print("Hello Python!")


my_function()
other_function()

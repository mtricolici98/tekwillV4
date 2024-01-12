# user_params = {
#     'IS_DEVELOPER': 'true'
# }


def get_user_parameters(existing_parameters: dict = None):
    if existing_parameters is None:
        existing_parameters = dict()
    while True:
        print('add parameter')
        param_name = input('Param name or stop:')
        if param_name == 'stop':
            break
        param_value = input('Param value:')
        existing_parameters[param_name] = param_value
    return existing_parameters


# new_params = get_user_parameters()
# print(new_params)
#
# other_new_params = get_user_parameters()
# print(other_new_params)


def example() -> int:
    print('Example code')
    return '1'


print(type(example()))

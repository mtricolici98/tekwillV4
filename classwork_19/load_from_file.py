import json


def connect_to_db(ip, port, db_name, password):
    print(f'Connecting with: {ip}, {port}, {db_name}, {password}')


json_file = 'config.json'

connection_data = json.load(open(json_file))
connect_to_db(**connection_data)

import os
import shutil
from datetime import datetime

print(os.getcwd())

destination_base_folder = os.path.join(*os.path.split(os.getcwd())[:-1])
print(destination_base_folder)

destination_folder_name = "classwork_16_backup"

destination_path = os.path.join(destination_base_folder, destination_folder_name)

if not os.path.exists(destination_path):
    os.makedirs(destination_path)

for filename in os.listdir(os.getcwd()):
    source = os.path.join(os.getcwd(), filename)
    destination = os.path.join(destination_path, filename)
    print(datetime.fromtimestamp(os.path.getctime(source)))
    shutil.copy(source, destination)
    print(f'Copying {source} to {destination}')

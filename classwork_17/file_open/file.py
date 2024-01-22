import os


def print_cwd():
    print(os.getcwd())


def create_file():
    open(os.path.join(os.getcwd(), 'data', 'file.txt'), 'w')


def create_file_in_documents():
    open(
        os.path.join('C:\\Windows', 'file.example'),
        'w'
    )


def list_files_in_folder(path):
    for file in os.listdir(path):
        print(file)

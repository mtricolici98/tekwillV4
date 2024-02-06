import os


class FileUtils:

    @staticmethod
    def list_files_in_directory(dir_):
        results = []
        for file in os.listdir(dir_):
            if not os.path.isdir(os.path.join(dir_, file)):
                results.append(file)
        return results

    @staticmethod
    def get_files_sorted_by_time(dir_):
        results = []
        for file in sorted(os.listdir(dir_), key=os.path.getctime):
            if not os.path.isdir(os.path.join(dir_, file)):
                results.append(file)
        return results

class ExcellFileUtils:

    @staticmethod
    def get_sheets_count_in_excel_file(path_to_file):
        pass
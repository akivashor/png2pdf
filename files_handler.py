import datetime
import os


def get_files_list(directory, extension='', full_path=False, minimum_date=None):
    files_list = []
    for file in os.scandir(directory):
        if minimum_date:
            creation_date = datetime.datetime.fromtimestamp(file.stat().st_ctime).date()
            if creation_date < minimum_date:
                continue
        if extension:
            if not file.name.endswith(extension):
                continue
        if full_path:
            files_list.append(file.path)
        else:
            files_list.append(file.name)
    return files_list
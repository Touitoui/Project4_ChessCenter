import os


def create_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)

def str_to_date(text, date_format="%d-%m-%Y"):
    pass
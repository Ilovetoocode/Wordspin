import random
def make_list_from_file(file):
    with open(file, 'r', encoding='utf8') as file:
        items = []
        for line in file:
            items += line.splitlines()
        print(items)

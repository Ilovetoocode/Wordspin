import random
def make_list_from_file(file):
    with open(file, 'r', encoding='utf8') as file:
        items = []
        for line in file:
            items += line.splitlines()
        return items
def make_synonym_dictionary(list):
    synonymdict={}
    broken_list=[]
    second_broken_list=[]
    for lines in list:
        broken_list=lines.split(":")
        synonymdict[broken_list[0]]=[]
        second_broken_list=broken_list[1].split(",")
        synonymdict[broken_list[0]]+=second_broken_list
class Spinner:
    def __int__(self):
        self.synonyms=make_synonym_dictionary(make_list_from_file("synonyms-simplified.txt"))
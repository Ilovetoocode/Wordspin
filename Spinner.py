import random
def make_list_from_file(file):
    with open(file, 'r', encoding='utf8') as file:
        items = []
        for line in file:
            items += line.splitlines()
        return items
def make_synonym_dictionary(list):
    synonym_dict = {}
    broken_list = []
    second_broken_list = []
    for lines in list:
        broken_list = lines.split(":")
        synonym_dict[broken_list[0]] = []
        second_broken_list = broken_list[1].split(",")
        synonym_dict[broken_list[0]] += second_broken_list
    return synonym_dict
def wordrandomizer(input, syndict):
    maybe_change = random.randint(0,100)
    new_word = ""
    if maybe_change >= 50:
        word_change = random.randint(0,len(syndict[input])-1)
        new_word = syndict[input][word_change]
    else:
        new_word = input
    return new_word


class Spinner:
    def __init__ (self, input):
        self.synonyms = make_synonym_dictionary(make_list_from_file("synonyms-simplified.txt"))
        self.input = input
    def Spintowin(self):
        output = ""
        input = self.input
        for word in input:
            if word in self.synonyms:
                output += (wordrandomizer(word, self.synonyms))
            else:
                output += (word)
            output += " "
        return output





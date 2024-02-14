import random
## Code from the bot project that was needed here! Simply makes a list from the file.... Infact...
def make_list_from_file(file):
    with open(file, 'r', encoding='utf8') as file:
        items = []
        for line in file:
            items += line.splitlines()
        return items
## This second one is also from the bot project! Though, it's been, slightly modified... Originally it would only have one list
##For broken list stuff, but due to how this new program needs to handle abritrary numbers of values for keys. Works pretty well!
def make_synonym_dictionary(list):
    synonymdict = {}
    broken_list = []
    second_broken_list = []
    for lines in list:
        broken_list=lines.split(":")
        synonymdict[broken_list[0]]=[]
        second_broken_list=broken_list[1].split(",")
        synonymdict[broken_list[0]]+=second_broken_list
    return synonymdict
##Here's a function that, pretty much exists so I don't have to nest a later method as much.... Pulls input text and randomizes it from a given dictionary for synonyms.
##Really all of this code didn't need to be up here... I just did it like this so I could minimize the clutter down in the Spintowin method.
##Works very well this way, and also means you need not pay as much attention to... nonsense nested code clutter
def wordrandomizer(input, syndict):
    maybe_change=random.randint(0,100)
    new_word=""
    if maybe_change >= 50:
        word_change=random.randint(0,len(syndict[input])-1)
        new_word=syndict[input][word_change]
    else:
        new_word=input
    return new_word


class Spinner:
    ##The spinner itself, first part calls earlier functions for the dictionary, alongside taking an input agrument
    ##so it can work with the one method it has.
    def __init__ (self, input):
        self.synonyms= make_synonym_dictionary(make_list_from_file("synonyms-simplified.txt"))
        self.input=input
    def Spintowin(self):
        ##This is the main spinning function itself, taking in text to determine whether or not to send it to the wordrandomizer function defined earlier, putting in either the output of the function
        ##Or just putting in the text itself if the word's not in the self.synonyms dictionary
        ##Here you can see why I moved that up, probably. The if word in part would have, looked so much worse thanks to the extra nesting needed....

        output=""
        input=self.input
        for word in input:
            if word in self.synonyms:
                output+=(wordrandomizer(word, self.synonyms))
            else:
                output+=(word)
            output+=" "
        return output





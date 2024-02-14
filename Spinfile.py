# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from Spinner import Spinner
import string


def read_text(filename):
   with open(filename,'r') as file:
      text = file.read().lower().translate(str.maketrans('', '', string.punctuation))
      return text

def main():
   original_text = read_text('essay.txt') # read the original text from essay
   print("Original", "\n", original_text)

   spinner = Spinner(original_text)
   for i in range(3): # convert the original text 3 times
      changed_text = spinner.Spintowin()
      print("Option", i+1, "\n", changed_text) # prints the index of the current location
      original_text = changed_text

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
   main();

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

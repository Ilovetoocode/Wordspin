# Code by Connor Walton and Long Nguyen
# Assignment A4, Word Spinner for comp 1020

# Starting out: we import both the spinner object and the string package.
from Spinner import Spinner
import string


# This function is used to grab a text file and use it as a string value.
# This is done so later on we can use it on the essay.txt file as a parameter for the Spinner object.
def read_text(filename):
    with open(filename, 'r') as file:
        text = file.read().lower().translate(str.maketrans('', '', string.punctuation))
        return text


# This function's a little bit extra! The original idea goes to Nguyen. He decided that the results file should
# automagically be updated each time you ran the program! The original version had this code in the main function,
# as seen in the git repo For readability however, anything pertaining to the printing has been turned into its own
# function to be called. With all that out of the way, this first one overwrites the original results.txt file,
# starting it over with the original text. This makes sure that the file is cleaned up, making the next step of the
# output file work more easily. Note however this will destroy any previous version of the results file,
# so if there's any results you like in a generation? Make sure you save them somewhere else before running the
# program again!
def file_writer(text_to_print):
    with open('results.txt', 'w') as result_file:
        result_file.write("Original\n")
        result_file.write(text_to_print + "\n\n")


# This function takes in the same results file as the file writer above.
# The only difference? This function is set to append mode, rather than write mode.
# This results in this function being able to add new data to a file, rather than fully overwriting one.
def file_appender(text_to_add):
    with open('results.txt', 'a') as result_file:
        result_file.write("Option {i+1}\n")
        result_file.write(text_to_add + "\n\n")


# #Finally we reach the main function. #This function: 1: calls the read_text function to get the essay for the
# original_text variable, #2: Prints that text out with a marker showing it is the original version #3:Calls the file
# writer to overwrite the results file with that text #4: Creates a Spinner object named spinner using the
# original_text as the argument #5:Creates a loop that uses the spintowin method to change the text, and using that
# result to print to console and pass into the file appender.
def main():
    original_text = read_text('essay.txt')  # read the original text from essay
    print("Original", "\n", original_text)
    file_writer(original_text)
    spinner = Spinner(original_text)
    for i in range(3):  # convert the original text 3 times
        changed_text = spinner.spintowin()
        file_appender(changed_text)
        print("Option", i + 1, "\n", changed_text)  # prints the index of the current location


if __name__ == '__main__':
    main()

import nltk
import re
import io


def get_ing():

#A methods which gets all the words ending of -ing

    #get all the words from the file
    fo = open("Earl Grey.member.txt", 'r')
    fo.close()
    words = "Earl Grey.member.txt"



    #for word in words:
    #print word
    #removing proper names (every word which is written with an upper case letter in the beginning) from the english word corpus
    wordlist = [word for word in fo.words("en") if word.islower()]
    #ing$ is the regular expression for finding ing at the end of a word.
    #re.search = check whether a pattern can be found inside a string
    end_ing = [word for word in wordlist if re.search("remember.ing$",word)]


    print end_ing

    #create new file
    with io.FileIO("Ear Grey extracted data.txt", "w") as file:
        file.write(end_ing)

    return wordlist

get_ing()

'''


def find_pattern():

    textfile = open('Earl Grey.member.txt', 'r')              #open and read the file
    content = textfile.read()                                   #store it in a var
    textfile.close()
    found_pattern = re.findall("[A-Za-z]+ one [A-Za-z]+",content)
    return found_pattern                                         #print and return the pattern

print find_pattern()


import re

textfile = open('Earl Grey.member.txt', 'r')
filetext = textfile.read()
textfile.close()
matches = re.findall("(<(\d{4,5})>)?", filetext)
'''
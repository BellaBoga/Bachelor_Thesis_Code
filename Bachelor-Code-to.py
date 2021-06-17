import nltk
from nltk import *

def bigramList(text):
    textfile = open(text, 'r')  # open and read the file
    content = textfile.read()
    textfile.close()
    contentList = content.split()       #das Dokument in Liste packen
    bigramListing = list(bigrams(contentList))  #list erstellen mit den bigrams
    return bigramListing    # store the list to use it later


wordlist = bigramList('Lord Brougham.member.txt')       #testprint
#print "bigramlist:", wordlist

def findVerbcomplementation():
    rememberList = []   #leere Liste erstellen fuer spaeter
    wordlist1 = bigramList('Lord Brougham.member.txt')  #store the list to get the bigrams

    for bigram in wordlist1:
      if "like" in bigram[0] and "to" in bigram:#checks if in the bigram remember followed by a gerund is
          rememberList.append(bigram)

#fuer to einfach string mit "to" in der for schleife oben



    return rememberList #return to store for laterfrom nltk import *
import sys
import codecs
import io
from nltk.tokenize import sent_tokenize, word_tokenize

def open_file(text):
    with open(text, 'r') as textfile:  # open and read the file
        content = textfile.read()

    return content

#open_file('Sir Robert Peel.member.txt')

def create_bigram_list(text):
    # textfile = open(text, 'r')  # open and read the file
    # content = textfile.read()
    # textfile.close()
    bigram = list(bigrams(text.split()))  #list erstellen mit den bigrams
    #tokenized_text = nltk.sent_tokenize(open_file('Sir Robert Peel.member.txt').decode('utf-8'))     #change it to sentences or smth
    #print tokenized_text

    return bigram  # function returns list of bigrams


#wordlist = create_bigram_list('Sir Robert Peel.member.txt')       #testprint
#print "bigramlist:", wordlist


def get_sentences():
    sentences_i_need=[]
    sentences = sent_tokenize(open_file('Sir Robert Peel.member.txt').decode('utf-8'))
    #print sentences[:10]
    #print type(sentences)

    words = ["avoid", "know", "remember"]

    for index, sent in enumerate(sentences):
        bigrams = create_bigram_list(sent)

        bigrams_ing = []

        for bigram in bigrams:
            if bigram[0] in words and "to" in bigram:  # checks if in the bigram remember followed by a gerund
                bigrams_ing.append(bigram)

        if len(bigrams_ing) > 0:
            sentences_i_need.append((index, sent))

        #if bigram in findVerbcomplementation():
                #print 'a'
    #print sentences_i_need[:10]
    return sentences_i_need

sentences = get_sentences()

with codecs.open("bigram_sentences-to.txt", "a", "utf-8") as f:
    for sent in sentences:
        f.write(u"{}\t{}\n".format(sent[0], sent[1].replace("\n", " ")))

sys.exit()

def findVerbcomplementation():
    bigrams_ing = []   #leere Liste erstellen fuer spaeter
    bigram_list = create_bigram_list('Sir Robert Peel.member.txt')  #store the bigrams from the input text

    for bigram in bigram_list:
      if "avoid" == bigram[0] and bigram[1].endswith("ing"):#checks if in the bigram remember followed by a gerund
          bigrams_ing.append(bigram)
                      #fuer to einfach string mit "to" in der for schleife oben
    return bigrams_ing #returns all bigrams that are followed by a gerund

print "verb and ing:", findVerbcomplementation()   #die brauch ich, keine test prints
print "Count of all occurences of verb+ing:", len(findVerbcomplementation())                    #gibt ANzahl aller Verb+ing an auch doppelte

#numberOf = FreqDist(findVerbcomplementation())

#print numberOf

def count_method():
    countedelements={}                  #created dict to store key:value pairs how often which combination occurs
    liste = findVerbcomplementation()   #function above stored in a variable to get the list of the remember occurences


    for element in liste:               #for elements in the word+ing list:

        if element  not in countedelements:     # wenn Element noch nicht drin, dann min 1 mal rein, weiter unten im Text
            countedelements[element] = 1

        else:
            countedelements[element]= countedelements[element]+1    #wenn schon drin, dann um 1 erhoehen

    return countedelements      #return to store


print "counted list:", count_method()   #that rints the dict with all entrys
print "Unique verb+ing:", len(count_method())               # counts how many unique verb+ing occurences in a dict




print "verb and to:", findVerbcomplementation()   #die brauch ich, keine test prints
print "Count of all occurences of verb+to:", len(findVerbcomplementation())                    #gibt ANzahl aller Verb+ing an auch doppelte

#numberOf = FreqDist(findVerbcomplementation())

#print numberOf

def count_method():
    countedelements={}                  #created dict to store key:value pairs how often which combination occurs
    liste = findVerbcomplementation()   #function above stored in a variable to get the list of the remember occurences


    for element in liste:               #for elements in the word+ing list:

        if element  not in countedelements:     # wenn Element noch nicht drin, dann min 1 mal rein, weiter unten im Text
            countedelements[element] = 1

        else:
            countedelements[element]= countedelements[element]+1    #wenn schon drin, dann um 1 erhoehen

    return countedelements      #return to store

print "counted list:", count_method()   #that orints the dict with all entrys
print "Unique verb+to:", len(count_method())               # counts how many unique verb+ing occurences in a dict


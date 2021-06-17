from nltk import *
import codecs
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


def get_sentences(filename):
    sentences_i_need=[]
    sentences = sent_tokenize(open_file(filename).decode('utf-8'))
    #print sentences[:10]
    #print type(sentences)

    words = ["avoid", "know", "remember", "forbear"]

    for index, sent in enumerate(sentences):
        bigrams = create_bigram_list(sent)

        bigrams_ing = []

        for bigram in bigrams:
            if bigram[0] in words and bigram[1].endswith("ing"):  # checks if in the bigram remember followed by a gerund
                bigrams_ing.append(bigram)

        if len(bigrams_ing) > 0:
            sentences_i_need.append((index, sent, bigrams_ing))

        #if bigram in findVerbcomplementation():
                #print 'a'
    #print sentences_i_need[:10]
    return sentences_i_need

dirs = [i for i in os.listdir("Data")] #loads all files from the data folder

for dir in dirs:
    sentences = get_sentences("Data/" + dir)
    flat_bigrams = [i for i in [i[2] for i in sentences]]
    print dir,"Number of Bigrams:", len(flat_bigrams)
    with codecs.open("Bigrammes/" + dir + ".bigrames", "a", "utf-8") as f:
        for sent in sentences:
            f.write(u"{}\t{}\t{}\n".format(sent[0], sent[1].replace("\n", " "), u",".join([u"({}|{})".format(bigram[0], bigram[1]) for bigram in sent[2]])))

#bigrams = [i[2] for i in sentences] list of lists of bigrams for each sentence

# def findVerbcomplementation():
#     bigrams_ing = []   #leere Liste erstellen fuer spaeter
#     bigram_list = create_bigram_list('Sir Robert Peel.member.txt')  #store the bigrams from the input text
#
#     for bigram in bigram_list:
#       if "avoid" == bigram[0] and bigram[1].endswith("ing"):#checks if in the bigram remember followed by a gerund
#           bigrams_ing.append(bigram)
#                       #fuer to einfach string mit "to" in der for schleife oben
#     return bigrams_ing #returns all bigrams that are followed by a gerund
#
# print "verb and ing:", findVerbcomplementation()   #die brauch ich, keine test prints
# print "Count of all occurences of verb+ing:", len(findVerbcomplementation())                    #gibt ANzahl aller Verb+ing an auch doppelte
#
# #numberOf = FreqDist(findVerbcomplementation())
#
# #print numberOf





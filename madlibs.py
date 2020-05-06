#! Python3
#! Mad libs project - reads text files and then adds texts based
# on the words that appear in the file.


# Step1 - open the file with the text.
import re

Textopen = open('textrep.txt', 'r')
Replacedwordsfile = open('replacedwords.txt', 'w')

#  Read the file
Textread = Textopen.read() # reads the file and saves to new variable.
IndiWords = Textread.split() # splits the text file into words.
Textopen.close()

#replace the words Adjective, Noun, Adverb, Verb in the file based on user input
adjregex = re.compile(r'ADJECTIVE')
nounregex = re.compile(r'NOUN')
verbregex = re.compile(r'VERB')

newstring = ""

#index, enumerate
for word in IndiWords:
    if adjregex.match(word):
        print('Enter an adjective:')
        word = adjregex.sub(str(input()), word)
    elif nounregex.match(word):
        print('Enter an Noun:')
        word = nounregex.sub(str(input()), word)
    elif verbregex.match(word):
        print('Enter an verb:')
        word = verbregex.sub(str(input()), word)
    newstring += word + " "
    Replacedwordsfile.write(word + " ")
    
#Replacedwordsfile.write(str(newstring))

# print the text file on the screen and save to the new text file.
print(newstring)


Replacedwordsfile.close()

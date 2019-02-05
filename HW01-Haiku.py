# homework 1- determine if a text if a haiku
import nltk

# get cmu dict of syllables
nltk.download('cmudict')
arpabet = nltk.corpus.cmudict.dict()

# get list of words from text and save in set
words = set()
fin = open("seasons.txt")
for line in fin:
    words.add(line.strip())
fin.close()

# function that takes in a word and uses cmu dict to tell us how many syllables the word has
def countSyllables(word):
    pronunciationList = arpabet[word]
    # there may be more than one pronunciation of a word so here I only count the first one
    count = 0
    # for each group
    for w in pronunciationList[0]:
        # for each char in the group
        for c in w:
            # if there is a number, that means that is another syllable
            if c in '0123456789':
                count += 1
    return count

# function that takes in a word and checks to see if it is a list of valid haiku words
def validHaikuWord(word):
    return True if word.upper() in words else False

# function that determines if input text is a haiku
def determineHaiku(text):
    # need to check that the text has 3 lines
    lines = text.split('\n')
    if len(lines) == 3:
        # now we need to check that each line has the correct amount of syllables
        # iterate through each line, keep track of what line we are up to
        lineCount = 0
        for line in lines:
            # initialize count for syllables
            syllableCount = 0
            # split the line into each words
            words = line.split()
            # and for each word, get the number of syllables and add it to count
            for word in words:
                # check that the word is a valid word, if not return False
                if not validHaikuWord(word):
                    return False
                syllableCount += countSyllables(word)
            # at the end of the line, check that the syllable count is correct, if not return False
            if (lineCount % 2 == 0 and syllableCount != 5) or (lineCount % 2 != 0 and syllableCount != 7):
                return False
            lineCount +=1
        return True
    return False

print(determineHaiku("there was a young man\nfrom cork who got limericks\nand haikus confused"))
print(determineHaiku("hot spring freeze chill leaf\ncool blossom soil melt trees breeze\nsolstice autumn bright"))
# homework 2- determine if a text if a limerick
# the meter of syllable stress is that for every 3 syllables in the line of 8 or 9, then 2 out of 3 has to be the
# stressed syllable
import nltk

# get cmu dict of syllables
# nltk.download('cmudict')
arpabet = nltk.corpus.cmudict.dict()

# initialize list to keep track of last syllable of each line
lastSyllables = [None] * 5

# function to check if two lines are rhyming
# takes in two integers that represent the line number which refers to pos in the global last syllables list
def checkRhyme(a, b):
    if lastSyllables[a] == lastSyllables[b]:
        return True
    return False

# function to get the last syllable and put it into global list. takes in str word and an int of the line number
def addLastSyllable(word, lineNum):
    pronunciationList = arpabet[word]
    lastSyllables[lineNum] = pronunciationList[0][-1]

# function that takes in a list of words in each line and tells if the meter is proper
# returns true if meter is proper, false otherwise
def checkMeter(line):
    syllables = []
    for word in line:
        prounounciationList = arpabet[word]
        for syllable in prounounciationList:
            syllables.append(syllable[0])
    for i in range(0, len(syllables)-3, 3):
        if syllables[i][-1] not in "0ABCDEFGHIJKLMNOPQRSTUVWXYZ" and syllables[i+1][-1] not in '123456789' \
            and syllables[i+2][-1] not in "0ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            return False
    return True

def determineLimerick(text):
    text = text.lower()
    # first determine if there are 5 lines
    lines = text.split('\n')
    if len(lines) == 5:
        # then add the last syllables to the global list
        for i in range(len(lines)):
            words = lines[i].split()
            addLastSyllable(words[-1], i)
            # check to see if this line has proper meter
            if not checkMeter(words):
                return False
        # check lines 1, 2, 5 and 3, 4
        if checkRhyme(0, 1) and checkRhyme(1, 4) and checkRhyme(2, 3):
            return True
    return False

print(determineLimerick('The limerick packs laughs anatomical\nInto space that is quite economical\nBut the good ones I\'ve seen\nSo seldom are clean\nAnd the clean ones so seldom are comical'))


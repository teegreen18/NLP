import nltk
#nltk.download()
from nltk.book import *

# Exercise 22
print("Exercise 22")
four_letter = [w for w in text5 if len(w) == 4]
fdist = FreqDist(four_letter)
fdist_dict = dict(fdist)
print(sorted(fdist_dict, key=fdist_dict.get, reverse=True))

# Exercise 24
print("Exercise 24")
V = set(text6)
retVal = [w for w in V if "z" in w or "Z" in w or "pt" in w or w[-1:-4] == "ize" or w[0] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" and w[1:] in "abcdefghijklmnopqrstuvwxyz"]
print(retVal)

# Exercise 25
print("Exercise 25")
sent = ['she', 'sells', 'sea', 'shells', 'by', 'the', 'sea', 'shore']
print([w for w in sent if w[0:2] == "sh"])
print([w for w in sent if len(w) > 4])
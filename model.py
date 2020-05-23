import math
from Trie.TrieDataStructure import Trie

kndConstant = 0.75

#read files 
trainingSetFile = open("training_set.txt", "r")
testingSetFile = open("testing_set.txt", "r")

def file_read(fread):
    read_array = []
    while 1 > 0:
        lineText = fread.readline().lower()
        if len(lineText) == 0:
           break
        lineText = lineText[:-1]
        words = lineText.split(' ')
        words.append("</s>")
        read_array.append(words)
    return read_array

#initialize tries
uniGram = Trie()
biGram = Trie()
triGram = Trie()
uniGram.insert("<unk>")

trainingSet = file_read(trainingSetFile)
testingSet = file_read(testingSetFile)

#fill words to tries
for s in trainingSet:
    previous1 = "<s>"
    previous2 = "<s>"
    for word in s:
        uniGram.insert(word)
        biGram.insert(previous2 + word)
        triGram.insert(previous1 + previous2 + word)
        previous1 = previous2
        previous2 = word

#normalize testingSet
for i in range(len(testingSet)):
    for j in range(len(testingSet[i])):
        if uniGram.search(testingSet[i][j]) == 0:
            testingSet[i][j] = '<unk>'

vocab = uniGram.vocabulary_count()


def search(trieGram, word):
    return trieGram.search(word) + 1

def searchTotChild(trieGram, word):
    return trieGram.searchTotChild(word) + vocab

def searchDiffChild(trieGram, word):
    return vocab

# three words "x y z" respectively appear and z is the last one
def calculate_probability(x, y, z):
    uniString = z
    biString = y + z
    triString = x + y + z

    d = kndConstant
    triProb = max(search(triGram, triString) - d, 0) / searchTotChild(triGram, x + y)
    biProb = max(search(biGram, biString) - d, 0) / searchTotChild(biGram, y)
    uniProb = max(search(uniGram, uniString) - d, 0) / searchTotChild(uniGram, "") 

    uniProb = uniProb + d / searchTotChild(uniGram, "")
    
    biTheta = d * searchDiffChild(biGram, y) / searchTotChild(biGram, y)
    biProb = biProb + biTheta * uniProb

    triTheta = d * searchDiffChild(triGram, x + y) / searchTotChild(triGram, x + y)
    triProb = triProb + triTheta * biProb

    return triProb

sumPerplexity = 0
for s in testingSet:
    perplexity = 0
    
    previous1 = "<s>"
    previous2 = "<s>"
    for word in s:
        perplexity += abs(math.log2(calculate_probability(previous1, previous2, word)))
        previous1 = previous2
        previous2 = word
    sumPerplexity += perplexity / len(s)

finalPerplexity = sumPerplexity / len(testingSet)
print(abs(finalPerplexity))
import pandas as pd
import math

def computeTF(wordDict, bow):
    tfDict = {}
    bowCount = len(bow)
    for word, count in wordDict.items():
        tfDict[word] = count / float(bowCount)

    return tfDict

def computeIDF(docList):
    idfDict = {}
    N = len(docList)
    #print(f'DocLen: {N}')

    #counts the number of documents that contain a word w
    idfDict = dict.fromkeys(docList[0].keys(), 0)
    for doc in docList:
        for word, val in doc.items():
            # print('i m here')
            # print(doc.items())
            # print(word, val)
            if val > 0:
                idfDict[word] += 1
                #print(f'idfDict: {idfDict}')
        print(f'idfDict: {idfDict}')

    #divide N by denominator above, take the log of that
    for word, val in idfDict.items():
        idfDict[word] = math.log(N / float(val))

    return idfDict

def computeTFIDF(tfBow, idfs):
    tfidf = {}
    for word, val in tfBow.items():
        tfidf[word] = val * idfs[word]
    return tfidf

docA = 'the cat sat on my face'
docB = 'the cat sat on my bed'

bowA = docA.split(' ')
bowB = docB.split(' ')

print(f'bowA : {bowA}')
print(f'bowB : {bowB}')

wordSet = set(bowA).union(set(bowB))
print(f'wordSet : {wordSet}')

wordDictA = dict.fromkeys(wordSet, 0)
wordDictB = dict.fromkeys(wordSet, 0)

print(f'wordDictA : {wordDictA}')
print(f'wordDictB : {wordDictB}')

for word in bowA:
    wordDictA[word] += 1

for word in bowB:
    wordDictB[word] += 1

print('-------------')
print(f'wordDictA : {wordDictA}')
print(f'wordDictB : {wordDictB}')

table = pd.DataFrame([wordDictA, wordDictB])
print(table)


#TF
print('TF')
tfBowA = computeTF(wordDictA, bowA)
tfBowB = computeTF(wordDictB, bowB)
print(tfBowA)
print(tfBowB)

#IDF
print('IDFs')
idfs = computeIDF([wordDictA, wordDictB])
print(f'idfs : \n {idfs}')

#TF-IDFS
tgidfBowA = computeTFIDF(tfBowA, idfs)
tgidfBowB = computeTFIDF(tfBowB, idfs)
print('-------')
print(tgidfBowA)
print(tgidfBowB)

prnt = pd.DataFrame([tgidfBowA, tgidfBowB])
print(prnt)

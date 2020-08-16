from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from xlrd import open_workbook
import numpy as np
import codecs
import re
from array import *
import xlrd
import xlsxwriter
from xlsxwriter.utility import xl_rowcol_to_cell

book=open_workbook('expert.xlsx')
stop_words = set(stopwords.words('english'))
question=input("Enter the question!")
text=question.lower()
data=[]
data=word_tokenize(text)
filtered_sentence = [w for w in data if not w in stop_words]

filtered_sentence = []

for w in data:
    if w not in stop_words and w not in filtered_sentence:
        filtered_sentence.append(w)

print(filtered_sentence)
length=len(filtered_sentence)
with open("temp.txt","w+") as temp_file:
    for line in filtered_sentence:
        temp_file.write("".join(line)+"\n")
    temp_file.close()
data2=[]
with open('Keywords.txt','r') as file1:
    with open('temp.txt','r') as file2:
        same= set(file1).intersection(file2)
#same.discard('\n')
with open('output.txt','w+') as file3:
    for line in same:
        data2=line

        file3.write(line)
file3.close()

with open('output.txt','r') as file4:
    d=[]
    with open('output.txt','rt') as file4:
        for myline in file4:
            d.append(myline)
        x1=len(d)
        for sh in xlrd.open_workbook('expert.xlsx').sheets():
            for row in range(sh.nrows):
                for col in range(sh.ncols):
                    myCell = sh.cell(row, col)
                    #print(myCell)
                    for i in range(x1):

                        #print(myCell.value)
                        if myCell.value == 'cloudy':
                            print('-----------')
                            print('Found!')
                            print(xl_rowcol_to_cell(row, col))

                        i=i+1




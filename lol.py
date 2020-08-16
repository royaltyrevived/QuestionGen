from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from xlrd import open_workbook
import numpy as np
import codecs
import re
from array import *
import sqlite3
from db import Database

db = Database()

def insert_file(text):
    conn=sqlite3.connect("db1.db")
    c=conn.cursor()
    news=text
    c.execute("INSERT INTO words (news) VALUES(""news"")")

#def find_complexity_of_keywords(x):
 #   with sqlite3.connect("database.db") as db1:
  #      cursor = db1.cursor()
   #     find_user = ("SELECT complexity from question WHERE keywords=?")
    #    cursor.execute(find_user, [(x)])
     #   results = cursor.fetchall()
    #return results

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
        data2+=line

        file3.write(line)
file3.close()

with open('output.txt','r') as file4:






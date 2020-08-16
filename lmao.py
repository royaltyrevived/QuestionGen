from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import sqlite3
from db import Database


db = Database()
conn=sqlite3.connect('db1.db')
c=conn.cursor()

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
c.execute("INSERT INTO words VALUES(?)", (filtered_sentence))
conn.commit()

conn=sqlite3.connect('db1.db')
c=conn.cursor()
c.execute("SELECT keyword score,level FROM main INTERSECT SELECT words FROM filtered sentences")
c.fetchall()
print(c.fetchall())

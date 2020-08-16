from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import sqlite3
import numpy as np

conn = sqlite3.connect('db1.db')
c = conn.cursor()

stop_words = set(stopwords.words('english'))
question = input("Enter the question!")
text = question.lower()
data = []
data = word_tokenize(text)
filtered_sentence = []
filtered_sentence = [w for w in data if not w in stop_words]
filtered_sentence.append("")
x = len(filtered_sentence)
d = []
d1 = []
f = []
for i in range(x - 1):
    c.execute("SELECT score FROM words WHERE words=?", (filtered_sentence[i],))
    d.append(c.fetchall())

    print(f"score of {filtered_sentence[i]}={d[i]}")
    print(d[i])
    if d[i] != []:
        g = d[i]
        f = g[0]
        h = f[0]
        d1.append(h)
        print(d1)





print('-----')
print(d1)
x = len(d1)
s = 0
for i in range(x):
    a = d1[i]
    s = s + a

avg = s / x
print(avg)

#

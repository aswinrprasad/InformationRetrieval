#!/usr/bin/env python
import textmining
import glob
from nltk.stem import PorterStemmer

tdm = textmining.TermDocumentMatrix()
ps=PorterStemmer()
files = glob.glob("*.txt")
print(files)
newcont=[]
newst=''
for f in files:
    content = open(f).read()
    content = content.replace('\n', ' ')
    c=content.split()
    for i in c:
        newcont.append(ps.stem(i))
    newst=" ".join(newcont)
    tdm.add_doc(newst)
tdm.write_csv('matrix.csv', cutoff=1)
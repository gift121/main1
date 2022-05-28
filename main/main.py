from cgitb import text
from itertools import count
from typing import Counter


file = open('story.txt', 'r')
f = file.readlines()
neWList = []
for line in f:
    
       neWList.append(line.strip())

print(neWList)

#open in read mode
with open('story.txt', 'r') as f:
       count = 0
       for line in f:
              if line != "\n":
                     count += 1
print('Total Lines', count)

#
from collections import Counter
def word_count(fname):

       with open(fname) as f:
              return Counter(f.read().split())
print("Number of words in the file :",word_count('story.txt'))
import re, os, sys
from collections import Counter

fileInput = sys.argv[1]
fileOutput = sys.argv[2]

words = re.findall(r'\w+', open(fileInput).read())
newDict = Counter(words).most_common(1000)


with open(fileOutput,'w+') as f:
    for keys, values in newDict:
        f.writelines(' '+ keys + ' %d' %(values)+'\n')



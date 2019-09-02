import re, os, sys

# File name inputs
fileInput = sys.argv[1]
fileOutput = sys.argv[2]

fileDict = {}

with open(fileInput, 'r') as txtIn:
    for line in txtIn:
        lowercaseLine = line.lower()

        # For chaeacters inside current line between alphabet range
        words = re.findall(r'\b[a-z]{1,25}\b', lowercaseLine)

        # If word already exists increment else start
        for word in words:
            if word in fileDict:
                fileDict[word] += 1
            else:
                fileDict[word] = 1

# Sort fileDict by keys then write to opened file
with open(fileOutput,'w') as txtOut:
    for key in list(sorted(fileDict.keys())):
        txtOut.writelines("%s %d\n" %(key, fileDict[key]))


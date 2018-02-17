#!/usr/bin/env python3


import sys
import re


# remove extra characters and classify into word/integer
def process(item):
    if re.search('[A-Za-z]', item):  # is a word
        newString = re.sub('[^A-Za-z]', '', item)
        return ('string', newString)
    else:  # is a number
        newNumber = int(re.sub('[^0-9]', '', item))
        if re.match('-', item):  # negative number
            newNumber *= -1
        return ('int', newNumber)

def getOutputString(inputString):
    inputWords = inputString.split()

    # read through words on first line of file
    intOrWord = []
    integers = []
    words = []
    for item in inputWords:
        itemClass, newItem = process(item)
        intOrWord.append(itemClass)
        if itemClass == 'int':
            integers.append(newItem)
        else:
            words.append(newItem)

    # sort each list
    integers.sort()
    words.sort()
    intIndex = 0
    wordIndex = 0

    # write sorted items to file
    newList = []
    for c in intOrWord:
        if c == 'int':
            newList.append(str(integers[intIndex]))
            intIndex += 1
        else:
            newList.append(words[wordIndex])
            wordIndex += 1

    return(' '.join(newList))


# run analysis
if len(sys.argv) == 3:
    infile = sys.argv[1]
    outfile = sys.argv[2]
    with open(infile) as f:
        line = f.readline()
        outString = getOutputString(line)
        fout = open(outfile, 'w')
        fout.write(outString + "\n")

        



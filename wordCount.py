
#!/bin/env python

import sys        # command line arguments
import re         # regular expression tools
import os         # checking if file exists
import subprocess # executing program
import string

# set input and output files from command line call
if len(sys.argv) is not 3:
    print("Correct usage: wordCount.py <input file name> <output file name>")
    exit()

inFile = sys.argv[1]
output_File = sys.argv[2]

# counts words in an input file
def countWords(inputF, dictionary):

    for word in input_File.read().split():
        word = word.lower() # makes sure all letters are lower case
        word = word.translate(None, string.punctuation)
        #print(word)
        if word not in dictionary:
            dictionary[word] = 1
            # print(dictionary[word])
        else:
            dictionary[word]+= 1
            # print(dictionary[word])


def export_Dictionary(output_File, dictionary):
    output_File = open("output.txt","w+")
    for i in sorted(dictionary):
        output_File.write("%s %d \n" % (i, dictionary[i]))
    #output_File.close()
    print("dictionary file exported")

# calls the above functions
dictionary = {}
input_File = open(inFile, "r")
countWords(input_File, dictionary)
export_Dictionary(output_File, dictionary)

#! python3
# smil.py
# Author: Sohil Ellabban

#Challenge:
# Your task is to find the smiles in the memory of SMIL. 
# A smile is sequence of symbols of the form “:)”, “;)”, “:-)”, or “;-)”.
#
#Input:
# A single line of at most 2048 symbols, such as letters from the English alphabet, digits, space, and many punctuation marks. 
# (To be precise, the symbols are from the ASCII range 32 to 126.) 
# The line contains at least one “:)”.

import sys

InputList = sys.stdin.readline()

def SmileCounter(Input):
    SmileIndex = []
    for x in range(len(Input)):
        if Input[x] == ":" or Input[x] == ";":
            if Input[x+1] == (")"):
                SmileIndex.append(x)
            elif Input[x+1] == ("-") and Input[x+2] == (")"):
                SmileIndex.append(x)
            else:
                pass
    for x in range(len(SmileIndex)):
        print(SmileIndex[x])

SmileCounter(InputList)
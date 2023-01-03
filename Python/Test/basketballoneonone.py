#! python3
# basketballoneonone.py
# Author: Sohil Ellabban 

# ScoreList = ("A2B1A2B2A1A2A2A2")

import sys
 
 
ScoreList = sys.stdin.readline()

def Win_Definer(ScoreList):
    z = len(ScoreList)
    y = z//2
    
    ScorerList = ScoreList[::2]
    PointsList = ScoreList[1::2]
    
    ScoreA = 0
    ScoreB = 0
    
    # print("Score list is:", ScoreList)
    
    for x in range(y):
        if ScorerList[x]=="A":
            ScoreA = ScoreA + int(PointsList[x])
        elif ScorerList[x]=="B":
            ScoreB = ScoreB + int(PointsList[x])
        else:
            print("Invalid input")
            break
    
    if ScoreA > ScoreB:
        print("A")
    elif ScoreA < ScoreB:
        print("B")
            
Win_Definer(ScoreList)
 
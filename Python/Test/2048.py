#! python3
# 2048.py
# Author: Sohil Ellabban

# Challenge: 2048
# Simulate a turn of 2048 given a starting board and a direction
# 
# Input: A single line of 16 integers separated by spaces. 
# The first 4 integers are the first row of the board, the next 4 integers are the second row, and so on. 
# The last integer is the direction of the move: 0 for left, 1 for up, 2 for right, and 3 for down.

import sys

Board = []
Direction = 0

for line in sys.stdin:
    item = line.split()
    if len(item) <= 1:
        Direction = int(item[0])
    Board.append(item)

# print(Board)
# print(Direction)

def M():
    pass

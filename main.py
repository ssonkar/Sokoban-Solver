# -*- coding: utf-8 -*-

import os
os.chdir(r"C:\Users\ARKADEEP\Desktop\ai proj\sokoban-master"+"//")
path=r"C:\Users\ARKADEEP\Desktop\ai proj\sokoban-master\tests"+"//"
lines = []                  # Declare an empty list named "lines"
with open ('testcase.txt', 'rt') as in_file:  # Open file lorem.txt for reading of text data.
    for l in in_file:  # For each line of text in in_file, where the data is named "line",
        lines.append(l.rstrip('\n'))   # add that line to our list of lines, stripping newlines.

def conv():
   #print("enter h,v")
   #path+'outfile'+np.random(4)+
   f=open('boardlayout.txt', 'w+')

   h,v=map(int,lines[0].split())
   #print(v)
   board= [[" " for _ in range(h)] for _ in range(v)] 
   #print("enter wallsquares")
   wallsquares=(lines[1].split())
   #walls = wallsquares[0]
   wallsquares = wallsquares[1:]
   wallsquares=list(map(int,wallsquares))
   for i in range(0, len(wallsquares)-1,2):
       board[wallsquares[i]-1][wallsquares[i+1]-1]="#"
   #print("enter boxes")
   boxes=list(map(int,lines[2].split()))
   for i in range(1, len(boxes)-1,2):
       board[boxes[i]-1][boxes[i+1]-1]="$"
   #print("enter storge")    
   storage=list(map(int,lines[3].split()))
   for i in range(1, len(storage)-1,2):
       board[storage[i]-1][storage[i+1]-1]="."
   #print("enter player position")    
   player=list(map(int,lines[4].split()))
   board[player[0]-1][player[1]-1]="@"
   f.write(str(v)+"\n")
   for i in range(v):
       for j in range(h):
           f.write(board[i][j])
       f.write("\n")
       
   f.close()
conv()
exec(open('test.py').read())
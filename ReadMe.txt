This is a part of our final project for the course CS271: Introduction to Artificial Intelligence,Fall 2018 at University of California,Irvine

Project: Sokoban
Project done by: Siddhant Sonkar and Arkadeep Adhikari

Project Description:
Input is 5 lines defining the board :
sixeH sizeV, e.g. "3 5"
nWallSquares a list of coordinates of wall squares, e.g. "12 1 1 1 2 1 3 2 1 2 3 3 1 3 3 4 1 4 3 5 1 5 2 5 3"
nBoxes a list of coordinates of boxes, e.g. "1 3 2"
nStorageLocations a list of coordinates of storage locations, e.g. "1 4 2"
playes initial locatin x and y, e.g. "2 2"

Output gives the moves taken by Sokoban to insert the boxes in the goals, and the duration for our algorithms to run
We have implemented BFS,UCS, and A* Search algorithms and user is prompted to select one of them at run.

Instructions to run the codes:

To run a given testcase put it inside the testcase.txt file and run main.py
Then select the algorithm you want to run.
You will get the board design in boardlayout.txt
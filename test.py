import sys
from sokoban import Sokoban

'''
Tests search algos
Handles command line and user input
'''


def runSearch(s, filename, option):
    ''' Runs the search based on filename and option selected '''
    b = s.new_board(filename)
    print('\nSolving ' + filename + '...')
    s.doSearches(b, option)

sok = Sokoban()

print("Which algorithm?")
print("1 for Breadth first search")
print("2 for Uniform cost search")
print("3 for A* Search")

p = input("Enter algorithm option: ")
option = int(p)

# gets file from args and plays that puzzle
if len(sys.argv) == 2:
    runSearch(sok, sys.argv[1], option)
else:
    runSearch(sok, 'boardlayout.txt', option)


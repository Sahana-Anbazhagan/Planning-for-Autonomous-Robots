Project 1: Solving the 8 - Puzzle game using BFS algorithm

I have used numpy and copy modules in this project

1) Run the E_Puzzle_Game.py
Enter the initial state you want for the puzzle seperated by space
For example,
Input:	     1 2 3
	     4 0 5 
	     6 7 8
Enter it as: 1 2 3 4 0 5 6 7 8
The output will print whether or not the puzzle is solvable and the parent nodes as a list.

2) Sample of an output screen:

Enter the initial state you want for the puzzle, seperated by space 1 0 3 4 2 5 7 8 6
The initial state is: 
 [[1 0 3]
 [4 2 5]
 [7 8 6]]
The goal state is: 
 [[1 2 3]
 [4 5 6]
 [7 8 0]]
This is solvable
[1, 4, 8, 17]

3) This will generate 3 text files:
nodePath.txt
Nodes.txt
NodesInfo.txt
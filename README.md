# N_Queens

## Problem Statement
The N-Queen problem is a classic problem in Computer Science and AI.
The Goal is to place N number of queens on an N x N chessborad in such a way that No two queens threaten each other.

That means
* No two queens in same row
* No two queens in same column
* No two queens share the same diagonal

## Approach

The problem can be solved using recursion and backtracking techniques. Here’s a brief overview of the approach:

* Recursion: The solution involves placing queens one row at a time and recursively trying to place a queen in the next row.
* Backtracking: If a placement leads to a conflict (i.e., the newly placed queen threatens another queen), we backtrack by removing the queen and trying the next possible placement.

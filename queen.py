def is_safe(row,col,queen_count,n):
    for posi in queen_count:
        #check column
        if posi[1]==col:
            return False
        #check upper left diagonal
        elif ((posi[0]-posi[1])+(n-1)) == ((row-col)+(n-1)):
            return False
        #check upper right diagonal
        elif (posi[0]+posi[1]) == (row+col):
            return False
    return True
    
def n_queens(board,row,n,queen_count=[],solutions = []):
    if  len(queen_count)==n:
        print(board)
        solutions.append([row[:] for row in board]) 
        return

    for i in range(n):
        if is_safe(row,i,queen_count,n):
            board[row][i]=1
            queen_count.append((row,i))
            n_queens(board,row+1,n,queen_count,solutions)
            board[row][i]=0
            queen_count.remove((row,i))

    return solutions

n = 3
board = [[0] * n for _ in range(n)]
solutions = n_queens(board, 0, n)
if len(solutions)==0:
    print("No Possible configuration !!")
for solution in solutions:
    for row in solution:
        print(row)
    print()
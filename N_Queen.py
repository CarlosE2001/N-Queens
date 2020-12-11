"""
Developer: Carlos Espinoza 
Version: 1.0
Date: December 2020
Contact: E-Mail: Carlosespinoza400@gmail.com | Github: https://github.com/CarlosE2001

Breif: This program solves the problem of the N chess queen usin a backtraking algorithm. On further versions this program will also
       use a more complex algorithm that takes into consideration the values of each position (weights) so it always gets the best
       and most profitable outcome possible.
"""

"""
Function: validPosition(T, R, C)
EFE: Checks if the queen's position is valid on a given table. Returns a boolean.
REQ: Table T and Position (R,C)
MOD: N/A
"""
def validPosition(T, R, C):
    tSize = len(T)
    #Save the original values of R and C
    rOrig = R
    cOrig = C

    #Check the current Row
    for i in range(tSize):
        if(T[R][i] == 1):
            return False

    #Check the upper diagonal
    while(R - 1 >= 0 and C - 1 >= 0):
        if(T[R-1][C-1] == 1):
            return False
        R -= 1
        C -= 1
    
    #Reset R and C values that were modified before
    R = rOrig
    C = cOrig

    #Check the lower diagonal
    while(R + 1 < tSize and C - 1 >= 0):
        if(T[R+1][C-1] == 1):
            return False
        R += 1
        C -= 1

    return True

"""
Function: solveProblem(T, C)
EFE: Solves the N-Queen problem
REQ: Table T and Column C
MOD: Table T with the right answer
"""
def solveProblem(T, C):

    if(C >= len(T)): #Base case to stop the backtracking. If reached, all queens were placed.
        return True
    
    for i in range(len(T)):
        if(validPosition(T, i, C)):
            T[i][C] = 1

            if(solveProblem(T, C + 1)):
                return True
    
            T[i][C] = 0

    return False

"""
Function: createTable(N)
EFE: Creates a NxN table to use and returns it
REQ: N size of the table
MOD: N/A
"""
def createTable(N):
    table = []
    for i in range(N):
        row = [0 for i in range(N)]
        table.append(row)
    return table

"""
Function: showTable(T)
EFE: Prints the Table 
REQ: Table T 
MOD: N/A
"""
def showTable(T):
    row = ""
    for i in range(len(T)):
        for j in range(len(T)):
            row += str(T[i][j]) + " "
        row += "\n"
    print(row)

"""
Function: main()
EFE: Creates the table, fills it and prints it
REQ: N/A
MOD: N/A
"""
def main():
    T = createTable(5)
    if(solveProblem(T,0)):
        showTable(T)
    else:
        print("There's no valid solution")

main()
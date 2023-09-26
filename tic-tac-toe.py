def tic_tac_toe(board):
    col1 = []
    col2 = []
    col3 = []
    cross1 = []
    cross2 = []
    ltor = 0
    rtol = 2
    X = ["X","X","X"]
    O = ["O","O","O"]
    for line in board:
        if(line == O):
            return "O"
        elif(line == X):
            return "X"
        col1.append(line[0])
        col2.append(line[1])
        col3.append(line[2])
        cross1.append(line[ltor])
        ltor+=1
        cross2.append(line[rtol])
        rtol-=1
    if ((col1 == X) or (col2 == X) or (col3 == X)) or ((cross1 == X) or (cross2 == X)):
        return "X"
    elif (col1 == O) or (col2 == O) or (col3 == O) or ((cross1 == O) or (cross2 == O)):
        return "O"  
    else:
        return "Draw"

print(tic_tac_toe([
  ["X", "O", "X"],
  ["O", "X",  "O"],
  ["O", "X",  "X"]
]))
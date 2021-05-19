def Orgin(moves):
    x = 0
    y = 0
    
    for move in moves:
        if(move == "u"):
            y +=1
        elif(move == "r"):
            x +=1
        elif(move == "d"):
            y -=1
        elif(move == "l"):
            x -=1
            
    return print(x==0 and y==0)

moves ="udrl"
Orgin(moves)
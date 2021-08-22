import time
game=True
x="X"
X=False
x=["X","O"]
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("---------------TIC TAC TOE-------------------")
print("--------------------AI-----------------------")
print("-----------------PLAY FUN--------------------")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
a=[[]]

print("")
print("")

def evaluate(a):
    for i in range(3):
        if(a[0][i]==a[1][i]==a[2][i]==X):
            return 10
        if(a[0][i]==a[1][i]==a[2][i]==(not X)):
            return -10
        if(a[i][0]==a[i][1]==a[i][2]==(not X)):
            return -10
        if(a[i][0]==a[i][1]==a[i][2]==X):
            return 10
    if(a[0][0]==a[1][1]==a[2][2]):
        if(a[0][0]==X):
            return 10
        elif(a[0][0]==(not X)):
            return -10
    if(a[0][2]==a[1][1]==a[2][0]):
        if(a[0][2]==X):
            return 10
        elif(a[0][2]==(not X)):
            return -10
        

def minimax(a,depth,isMax):
    score=evaluate(a)
    if score==10 or score==-10:
        return score
    # if(Left(a)==False):
    #     return 0
    if(isMax):
        best=-1000
        for i in range(3):
            for j in range(3):
                if(a[i][j]==-1):
                    a[i][j]=X
                    best=max(best,minimax(a,depth+1,not isMax))
                    a[i][j]=-1
        return best
    else:
        best=1000
        for i in range(3):
            for j in range(3):
                if(a[i][j]==-1):
                    a[i][j]=not X
                    # time.sleep(2)
                    # print(a)
                    best=min(best,minimax(a,depth+1,not isMax))
                    a[i][j]=-1
        print(best)
        return best
        
    


def bestmove(a):
    bestval=-1000
    move=(-1,-1)
    for i in range(3):
        for j in range(3):
            if(a[i][j]==-1):
                a[i][j]=X
                moveval=minimax(a,0,False)
                print(a)
                a[i][j]=-1
                time.sleep(2)
                print(moveval)
                if(bestval<moveval):
                    move=(i,j)
                    bestval=moveval
    return move
        
for i in range(3):
    
    a[i].append(-1)
    a[i].append(-1)
    a[i].append(-1)
    if(i!=2):
        a.append([])
    print("\t|",end="")
    print("\t|")
    if(i!=2):
        print("------------------------")        
    
def print_array():
    for i in range(3):
        if(a[i][0]!=-1):
            print("   ",x[a[i][0]],end="")
            

        print("\t|",end="")
        if(a[i][1]!=-1):
            print("   ",x[a[i][1]],end="")
            

        print("\t|",end="")
        if(a[i][2]!=-1):
            print("   ",x[a[i][2]],end="")
            

        if(i!=2):
            print("\n------------------------")


print("Position values are 1 -9")
while(game):


    print("")
    n=int(input("Enter Your Postion:"))
    if(n==0):
        break
    n-=1
    if(n<3):
        a[0][n]=X
    elif(n<6):
        a[1][n%3]=X
    elif(n<9):
        a[2][n%3]=X
    
    X=(not X)

    
    print_array()
    print("")
    print(bestmove(a))
    game=False
    print(a)



print("Fun-----------")



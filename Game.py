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
    
    X=not X

    
    print_array()
    print("")

print("Fun-----------")



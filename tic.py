print("TIC TAC TOE")
r=input("Enter the name of the 1st player:")
p=input("Enter the name of the 2nd player:")
r1c1="1"
r1c1s="|"
r1c2="2"
r1c2s="|"
r1c3="3"
r1c3s="|"
sep1="--------------"
r2c1="4"
r2c1s="|"
r2c2="5"
r2c2s="|"
r2c3="6"
r2c3s="|"
sep2="--------------"
r3c1="7"
r3c1s="|"
r3c2="8"
r3c2s="|"
r3c3="9"
r3c3s="|"
sep3="---------------"
print("\n",r1c1,r1c1s,r1c2,r1c2s,r1c3,r1c3s,"\n",sep1,"\n","\n",r2c1,r2c1s,r2c2,r2c2s,r2c3,r2c3s,"\n",sep2,"\n","\n",r3c1,r3c1s,r3c2,r3c2s,r3c3,r3c3s,"\n",sep3,"\n")
while(True):
    x=int(input(f"Enter the roll of {r}:"))
    if(x==1):
        r1c1="X"
    elif(x==2):
        r1c2="X"
    elif(x==3):
        r1c3="X"
    elif(x==4):
        r2c1="X"
    elif(x==5):
        r2c2="X"
    elif(x==6):
        r2c3="X"
    elif(x==7):
        r3c1="X"
    elif(x==8):
        r3c2="X"
    elif(x==9):
        r3c3="X"
    print("\n",r1c1,r1c1s,r1c2,r1c2s,r1c3,r1c3s,"\n",sep1,"\n","\n",r2c1,r2c1s,r2c2,r2c2s,r2c3,r2c3s,"\n",sep2,"\n","\n",r3c1,r3c1s,r3c2,r3c2s,r3c3,r3c3s,"\n",sep3,"\n")
    y=int(input(f"Enter the roll of {p}:"))
    if(y==1):
        r1c1="O"
    elif(y==2):
        r1c2="O"
    elif(y==3):
        r1c3="O"
    elif(y==4):
        r2c1="O"
    elif(y==5):
        r2c2="O"
    elif(y==6):
        r2c3="O"
    elif(y==7):
        r3c1="O"
    elif(y==8):
        r3c2="O"
    elif(y==9):
        r3c3="O"
    print("\n",r1c1,r1c1s,r1c2,r1c2s,r1c3,r1c3s,"\n",sep1,"\n","\n",r2c1,r2c1s,r2c2,r2c2s,r2c3,r2c3s,"\n",sep2,"\n","\n",r3c1,r3c1s,r3c2,r3c2s,r3c3,r3c3s,"\n",sep3,"\n")
    if((r1c1=="X" or r2c2=="X" or r3c3=="X")and (r2c1=="X" or r2c2=="X" or r2c3=="X") and (r3c1=="X" or r3c2=="X" or r3c3=="X") and (r1c3=="X" or r2c2=="X" or r3c1=="X") and (r1c1=="X" or r1c2=="X" or r1c3=="X")):
        print(f"{r} is the winner")
        break
    elif((r1c1=="O" or r2c2=="O" or r3c3=="O")and (r2c1=="O" or r2c2=="O" or r2c3=="O") and (r3c1=="O" or r3c2=="O" or r3c3=="O") and (r1c3=="O" or r2c2=="O" or r3c1=="O") and (r1c1=="O" or r1c2=="O" or r1c3=="O")):
        print(f"{p} is the winner")
        break
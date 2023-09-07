def rps(num1,num2,bit1,bit2):
    p1=int(num1[bit1])%3
    p2=int(num2[bit2])%3 #getting indexes from 0 to 2
    if a[p1]==b[p2]:
        print("draw")
    elif a[p1]=="Rock" and b[p2]=="Scissors":
        print("Player one wins!")
    elif a[p1]=="Rock" and b[p2]=="Paper":
        print("Player two wins!")
    elif a[p1]=="Paper" and b[p2]=="Scissors":
        print("Player two wins!")
    elif a[p1]=="Paper" and b[p2]=="Rock":
        print("Player one wins!")
    elif a[p1]=="Scissors" and b[p2]=="Rock":
        print("Player two wins!")
    elif a[p1]=="Scissors" and b[p2]=="Paper":
        print("Player one wins!")

a={0:"Rock",1:"Paper",2:"Scissors"} #player 1 rock paper scissors location
b={0:"Paper",1:"Rock",2:"Scissors"} #player 2 rock paper scissors location
while (1):
    num1=input("enter your choice")
    num2=input("enter your choice")
    bit1=int(input("Player 1 enter your secret bit position"))
    bit2=int(input("Player 2 enter your secret bit position"))
    rps(num1,num2,bit1,bit2)
    ch=input("Do you want to continue? y/n")
    if ch=="n":
        break
    
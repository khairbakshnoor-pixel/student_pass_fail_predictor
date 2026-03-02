import random

def p1roll():
    return random.randint(1,6)
def p2roll():
    return random.randint(1,6)

score=0
while True:
    print("welcome to dice game")
    print("1. Play Dice game ")
    print("2 Check your score")
    print("3. Exit")
    
    choice=input("your choice")
    if choice=='1':
     
        dice1=p1roll()
        computer=p2roll()

        print(f"you rolled {dice1}")
        print(f"computer rolled  {computer}")
        if dice1>computer:
            print("you won")
            score+=10
        elif dice1==computer:
            print("Match tied")
        else:
            print("computer won")
    
    elif choice=='2':
        print(f"you scored {score} ")

    elif choice=='3':
        print("Good bye ")
        break
    else:
        print("invalid choice")

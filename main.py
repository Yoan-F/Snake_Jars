import random

print("Welcome on this game play !")

difficulty = int(input("Choice your difficult please : 1 = Easy ; 2 = Normal ; 3 = Hard : "))

#keys
bunch = 0

print("Let's start !")

while bunch != 3:
    print("You have 5 choices, select on number between 1 and 5")

    # random choice of loose value : random number between 1 and 5
    snakes = ['S'] * difficulty
    keys = ['K'] * (5 - difficulty)
    jars = snakes + keys

    # random value in table
    random.shuffle(jars)
    #print(jars)

    # user choice a value
    choice = int(input())

    if jars[choice-1] == 'S':
        print("You loose ! Snake is on choice number !")
        if bunch > 0:
            bunch -= 1
        print(f"You have {bunch}/3 keys")
    else:
        print("You win ! you have one key !")
        bunch += 1
        print("You have ", bunch, "/3 keys")
        print("Congratulation you have open the treasure chest !")

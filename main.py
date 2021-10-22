import random
import time
lst=['s','w','g']
chance=int(input())
no_of_chance=0
computer_point=0
human_point=0
print("Snake,Water and Gun Game \n")
print("s for snake,w for water and g for gun \n")
while no_of_chance<chance:
    x=input("Snake, Water ,Gun \n")
    _random=random.choice(lst)
    if x == _random:
        print("Tie Both get 0 Points \n")
    elif x=="s" and _random=="g" or x=="w" and _random=="s" or x=="g" and _random=="w":
        computer_point=computer_point+1
        print(f"your guess {x} and computer guess is {_random} \n" )
        print("Computer winns 1 point \n")
        print(f"computer point is {computer_point} and your point is {human_point} \n")
    elif x=="s" and _random=="w" or x=="w" and _random=="g" or x=="g" and _random=="s":
        human_point=human_point+1
        print(f"your guess {x} and computer guess is {_random} \n" )
        print("Computer winns 1 point \n")
        print(f"computer point is {computer_point} and your point is {human_point} \n")
    else:
        print("you have wrong input \n")
    no_of_chance=no_of_chance+1
    print(f"{chance-no_of_chance} is left out of chance \n")
print("game over")
time.sleep(5)
if human_point==computer_point:
    print("tie")
elif human_point<computer_point:
    print("computer wins and you lose")
else:
    print("you win and computer lose")
print(f"your point is {human_point} and computer point is {computer_point}")


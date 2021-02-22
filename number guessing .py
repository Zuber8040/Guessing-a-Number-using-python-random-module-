import random 

n = random.randint(1,100)

guess = int(input("guess a +ve interger "))

#no_of_chance = input("You have only 5 chance to guess the right number ")

sure = input(f"You want to enter {guess} number ? if no then type no or type yes to continue : ")

while sure=='no':
    guess = int(input("please enter new +ve integer  "))
    sure = input(f"You want to enter {guess} number ? if no then type no or type yes to continue : ")
    break
while sure=='yes':
    if guess == n:
        print("your guess is right")
        break
    elif guess!=n:
        print(f"OOPS Worngs guess\n" + f"guess number is {n}")
        break













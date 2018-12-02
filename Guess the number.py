import random
a=random.randint(1,9)
c=1
while True:
    b=int(input("Guess the no i have got(1-9): "))
    if a>b:
        print("You guessed low.. ")
        if str(input("Do you want to try again (y/n)? "))=='y':
            c=c+1
            continue
        else:
            break
    elif a<b:
        print("You guessed high.. ")
        if str(input("Do you want to try again (y/n)? "))=='y':
            c=c+1
            continue
        else:
            break
    else:
        print("Your guessed right in "+ str(c)+ "times")
        break


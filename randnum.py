import random

random_number=random.randint(1,21)

count=0

max_guesses=5

while count<max_guesses:
    user_guess=int(input("Enter your guess:"))
    count+=1

    if user_guess<1 or user_guess>20:
        print("Invalid input")
        continue


    elif user_guess< random_number:
        print("too low")

    elif user_guess>random_number:
        print("too high")


    
    else:
        print("Congratulations!, You have guessed correctly")

if count == max_guesses and user_guess != random_number:
    print("Game Over! The correct number was:",random_number)
              

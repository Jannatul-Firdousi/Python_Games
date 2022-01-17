import time
import random
number=random.randint(1,100)
print("Guess one integer number between 1 and 100 within 5 seconds!")
time.sleep(5)
guess=int(input("\nNow enter the number you guessed!\n"))
attempt=1
while True:
    if number==guess:
        print("Let's see ! Fingers crossed!!")
        time.sleep(5)
        guess = int(input(f"Hurray! You made a perfect guess!\n You guessed the number in  {attempt} attempts."))
        break
    elif number - 1 <= guess <= number + 1:
        guess = int(input(f"You are very near to the number.\nQuickly guess a number which is between {number - 1} and {number + 1}\n"))
        attempt += 1
    elif number-5 <= guess <= number + 5:
        guess = int(input(f"You are very near to the number.\nQuickly guess a number which is between {number-5} and {number+5}\n"))
        attempt+=1
    elif guess>number:
        guess=int(input("Oops! You guessed too high!\n Think of a smaller number again!\n"))
        attempt+=1
    elif guess<number:
        guess = int(input("Oops! You guessed too low!\n Think of a bigger number again!\n"))
        attempt+=1
    else:
        print("Something went wrong! Try again from the beginning!")





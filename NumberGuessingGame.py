# Number Guessing Game:

import random 

guessesTaken = 0

print("Welcome to Gussing Game ")
print("Hello! What is your name? ")
myName = input()
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')

number = random.randint(1, 20)

while guessesTaken < 6:
     print('Take a guess.')
     guess = int(input())
     guessesTaken = guessesTaken + 1
     
     if guess < number:
          print("The Guessed number is low than the actual number")
     
     elif guess > number:
          print("The Guessed Number is higher than the actual Number")
         
     else:
          break
          
if guess == number:
     print(f"Your Number matches with the Actual Number and you have gussed in {guessesTaken} Guesses!")
    
if guess != number:
     print(f"You have not able to guess the actual number in {guessesTaken} Guesses!")
    
          
        

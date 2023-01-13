import random

number_of_attempt = 0
number = random.randint(1, 100)

while number_of_attempt < 6:
  print('Enter  a number between 1 to 100:')
  guess = int(input())
  # if and else statment
  if guess < number:
    print(guess, ' Guess too low.')
  if guess > number:
    print(guess, ' number too high.')
  if guess == number:
    print(guess, ' = ', number)
    print("Thank you for playing.")
    break
  
  
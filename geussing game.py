# In plain English and with the Given-required-algorithm table write
# a guessing game where the user has to guess a secret number.
# After every guess the program tells the user whether their number
# was too large or too small. At the end the number of tries needed should be printed.


print("\nHi! Here we have a game. I think of a number, and you as a user you have to guess that number.\n"
      " If you are interested in our game create a user name so that I can know who I am playing with. "
      "you try only three times.\n")

name=input("Create your user name:")
print("Welcome in a game",name,". Let get started\n")

secret_number=5  #the secret number the user is supposed to guess
num= int(input("Guess a number="))

while num != secret_number:
    if num > secret_number:
       print("The number you guessed is too high")
       num= int(input("Guess a number="))
    elif num < secret_number:
       print("The number you guessed is too low")
       num = int(input("Guess a number="))

print("Congratulations", name, "!", "The number is correct\n","the number is: ", secret_number)

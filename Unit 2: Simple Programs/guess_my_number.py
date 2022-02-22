""""
Created on Wed Feb 15 00:12:30 2022

@author: elvisckyung
"""""
low = 0
high = 100
print('Please think of a number between 0 and 100!')
while True:
    guess = (high + low)//2
    print('Is your secret number ' + str(guess) + '?')
    user_input = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if user_input == 'c':
        print('Game over. Your secret number was : ' + str(guess))
        break
    elif user_input == 'l':
        low = guess
    elif user_input == 'h':
        high = guess
    else: 
        print('Sorry, I did not understand your input.')




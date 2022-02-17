# Program that finds the square root using the Heron of Alexandria's Algorithm 

import random
message = 'The square root you are looking for is '
input_value = input('Please, enter the number to find square root for: ')

x = int(input_value)
g = random.randint(0, x)
print("First guess: " + str(g))

i = 0
while g**2 != x:
    g = (g + (x/g)) / 2
    print("Loop " + str(i) + ": " + str(g))

    i += 1
    if i > 25:
        break

if g**2 == x:
    print(message + str(g) + ".")
else:
    print(str(g) + " is not the perfect squared root of " + input_value)
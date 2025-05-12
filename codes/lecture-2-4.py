#random.randint() function that returns a random int val between the starting and ending point entered in the function: a = random.randint(1,10) >> 5
# a = [random.randint(1,10) for i in range (0,10)] >> [4, 9, 8, 4, 9, 5, 9, 3, 9, 4]
#random.randrange() function that includes the step parameter and excludes the upper limit entered in the func:
#random.sample() function
#random.uniform() function
#numpy.random.randint() function
#numpy.random.uniform() function
#numpy.random.choice() function
#secrets.randbelow() function

#https://www.pythoncentral.io/how-to-generate-a-random-number-in-python/

import random

random_number = random.randint(1, 10)
#print(random_number)
guessed_number = int(input('well well well.. guess the number between 1 and 10: '))

if guessed_number == random_number:
    print('congrats!')
else:
    while guessed_number != random_number:
        guessed_number = int(input('ehhh, that is not correct. try again: '))
    print('eeey good job!! ')
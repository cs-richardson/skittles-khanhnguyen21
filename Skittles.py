import random
print ('I am thinking of a random number between 0 and 1023, can you guess it?')
RAND = random.randint(0,1023)
GUESS = int(input('What is your guess?'))
while(GUESS != RAND):
    if GUESS > RAND - 10 and GUESS < RAND + 10:
        print ('You are close')
    elif GUESS < RAND:
        print('Too low')
    elif GUESS > RAND:
        print('Too high')
    print ('Guess again mate')
    GUESS = int(input('What is your guess?'))
print('Nice, mmkay')

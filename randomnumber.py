import random as r

def guess(x):
    random_num = r.randint(1,x)
    guess = 0
    while guess != random_num:
        guess = int(input(f'guess a random number between 1 and {x}: '))
        if guess < random_num:
            print('Sorry, guess again. Too low.')
        elif guess > random_num:
            print('Sorry, guess again. Too high.')
            
    print(f'Congratulations!! You are a genius, you guessed the number {random_num} correct!')
    
def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = r.randint(low,high)
        else:
            guess = low 
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)?? ').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f'Goodjob the computer guessed your number, {guess} correctly!')
    
guess(100)
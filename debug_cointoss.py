#! python3

import logging
import random

logging.basicConfig(level=logging.INFO, format=' %(asctime)s - %(levelname)s - %(message)s')

guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
    logging.info(f'guess should be {guess}')
toss = random.randint(0, 1) # 0 is tails, 1 is heads
logging.info(f'toss should be {toss}')
logging.debug(f'{toss} == {guess}')
if toss == 1:
    toss = 'heads'
    logging.debug(f'{toss} == {guess}')
else:
    toss = 'tails'
    logging.debug(f'{toss} == {guess}')
if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')

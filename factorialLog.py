#! python3
# example of logging

import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s \
        - %(message)s')
logging.debug('Start of Program')


def factorial(n):
    logging.debug('start of factorial(%s%%)' % (n))
    total = 1
    for i in range(n + 1):
        if i == 0:
            continue
        total *= i
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
    logging.debug('End of factorial(%s%%)' % (n))
    return total

print(factorial(5))
logging.debug('End of Program')


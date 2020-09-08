#! python3 # notes on ch12 of ATBS
# raise Exception("This is an error message you can raise if something goes wrong")

try:
    print('4' * 45 + str(5) % 'hello')
except Exception as err:
    print('An Exception Happened: ' + str(err))

print('"except Exception as err" is a cleaner way to check for ')
print('errors without crashing your whole program')

print()

### TRACEBACK
import traceback
try:
    raise Exception('this is an error message')
except:
    errorFile = open('errorinfo.txt', 'w')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('The Traceback info was written to errorinfo.txt')


### ASSERTIONS
ages = [1, 3, 5, 4, 7, 9, 34, 67, 88, 44]
ages.sort()
assert ages[4] < ages[2] # AssertionError

# if you run a script with the -O flag
# it will skip assertion errors

### LOGGING
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)
        s - %(message)s')


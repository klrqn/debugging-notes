#! python3
# Makes a box with the proper arguments

def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('Symbol must be a single character string.')
    if width <= 2:
        raise Exception('Width must be greater than 2')
    if height <= 2:
        raise Exception('Height must be greaterthan 2')

    print(symbol * width)
    for i in range(height-2):
        print(symbol + (' ' * (width-2)) + symbol)
    print(symbol * width)

# to enter into interactive shell after running program
# use the -i flag
# i.e. python3 -i boxprint.py

for sym, w, h in (('*', 4, 4), ('j', 5, 5), ('x', 1, 3), ('QRS', 3, 3)):
    try: 
        boxPrint(sym, w, h)
    except Exception as err:
        print('An exception happened: ' + str(err))

# this program uses the "except Exception as err" form of the except statement
# if an Exception object is returned from the function, it is stored in a var
# named err. Convert err to a string to produce a user-friendly error message


def spam(): # 1
    bacon() # 2

def bacon(): # 4
    raise Exception('This is an error message') #5

spam() # 7

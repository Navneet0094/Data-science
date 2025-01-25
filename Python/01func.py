# positional arguments
def printnum(*args):
    for i in args:
        print(i)
printnum(1,2,3,4,5,'navneet')

# keyword arguments
def printnum(**kwargs):
    for i in kwargs:
        print(i,kwargs[i])
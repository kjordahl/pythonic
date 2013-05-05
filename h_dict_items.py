numbers = ['one','two','three','four','five','six','seven']
colors = ['red','orange','yellow','green','blue','indigo','violet']

from itertools import izip

mydict = dict(izip(numbers, colors))

def lookup():
    for k in mydict:
        color2 = mydict[k]

def regular_items():
    for number, color in mydict.items():
        color2 = color

def iter_items():
    for number, color in mydict.iteritems():
        color2 = color

if __name__ == '__main__':
    import timeit
    print("lookup = ", timeit.timeit("lookup()", setup="from __main__ import lookup"))
    print("regular_items = ", timeit.timeit("regular_items()", setup="from __main__ import regular_items"))
    print("iter_items = ", timeit.timeit("iter_items()", setup="from __main__ import iter_items"))


colors = ['red','orange','yellow','green','blue','indigo','violet']

def index_lookup():
    for i in range(len(colors)-1, -1, -1):
        foo = colors[i]

def xrange_lookup():
    for i in xrange(len(colors)-1, -1, -1):
        foo = colors[i]

def sliced():
    for color in colors[::-1]:
        foo = color

def iterator():
    for color in reversed(colors):
        foo = color

if __name__ == '__main__':
    import timeit
    print("index_lookup = ", timeit.timeit("index_lookup()", setup="from __main__ import index_lookup"))
    print("xrange_lookup = ", timeit.timeit("xrange_lookup()", setup="from __main__ import xrange_lookup"))
    print("sliced = ", timeit.timeit("sliced()", setup="from __main__ import sliced"))
    print("iterator = ", timeit.timeit("iterator()", setup="from __main__ import iterator"))

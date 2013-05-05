colors = ['red','orange','yellow','green','blue','indigo','violet']

def index_lookup():
    for i in range(len(colors)):
        foo = colors[i]

def iterator():
    for color in colors:
        foo = color

if __name__ == '__main__':
    import timeit
    print("index_lookup = ", timeit.timeit("index_lookup()", setup="from __main__ import index_lookup"))
    print("iterator = ", timeit.timeit("iterator()", setup="from __main__ import iterator"))

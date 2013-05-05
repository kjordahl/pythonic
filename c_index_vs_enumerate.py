colors = ['red','orange','yellow','green','blue','indigo','violet']

def index_lookup():
    for i in range(len(colors)):
        j = i
        c = colors[i]

def enumerator():
    for (i, color) in enumerate(colors):
        j = i
        c = color

if __name__ == '__main__':
    import timeit
    print("index_lookup = ", timeit.timeit("index_lookup()", setup="from __main__ import index_lookup"))
    print("enumerator = ", timeit.timeit("enumerator()", setup="from __main__ import enumerator"))

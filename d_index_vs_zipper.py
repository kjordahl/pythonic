numbers = ['one','two','three','four','five','six','seven']
colors = ['red','orange','yellow','green','blue','indigo','violet']

def index():
    n = min(len(numbers), len(colors))
    for i in range(n):
        number = numbers[i]
        color = colors[i]

def xrange_index():
    n = min(len(numbers), len(colors))
    for i in xrange(n):
        number = numbers[i]
        color = colors[i]

def zipper():
    for n, c in zip(numbers, colors):
        number = n
        color = c

def i_zipper():
    for n, c in zip(numbers, colors):
        number = n
        color = c

if __name__ == '__main__':
    import timeit
    print("index = ", timeit.timeit("index()", setup="from __main__ import index"))
    print("xrange_index = ", timeit.timeit("xrange_index()", setup="from __main__ import xrange_index"))
    print("zipper = ", timeit.timeit("zipper()", setup="from __main__ import zipper"))
    print("i_zipper = ", timeit.timeit("i_zipper()", setup="from __main__ import i_zipper"))

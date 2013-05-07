colors = ['red','orange','yellow','green','blue','orange','orange','green']

def simple():
    d = {}
    for color in colors:
        if color not in d:
            d[color] = 0
        d[color] += 1

def try_except():
    d = {}
    for color in colors:
        try:
            d[color] = 0
        except:
            d[color] += 1

def with_get():
    d = {}
    for color in colors:
        d[color] = d.get(color, 0) + 1

from collections import defaultdict
def default_dict():
    d = defaultdict(int)
    for color in colors:
        d[color] += 1

if __name__ == '__main__':
    import timeit
    print("simple = ", timeit.timeit("simple()", setup="from __main__ import simple"))
    print("try_except = ", timeit.timeit("try_except()", setup="from __main__ import try_except"))
    print("with_get = ", timeit.timeit("with_get()", setup="from __main__ import with_get"))
    print("default_dict = ", timeit.timeit("default_dict()", setup="from __main__ import default_dict"))



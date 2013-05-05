names = ['mary','ed','chris','brendan','colin','shannon','ciaran','liam']

def old_way():
    d = {}
    for name in names:
        key = len(name)
        if key not in d:
            d[key] = []
        d[key].append(name)

def set_default():
    d = {}
    for name in names:
        key = len(name)
        d.setdefault(key, []).append(name)

from collections import defaultdict
def default_dict():
    d = defaultdict(list)
    for name in names:
        key = len(name)
        d[key].append(name)

if __name__ == "__main__":
    import timeit
    print("old_way = ", timeit.timeit("old_way()", setup="from __main__ import old_way"))
    print("set_default = ", timeit.timeit("set_default()", setup="from __main__ import set_default"))
    print("default_dict = ", timeit.timeit("default_dict()", setup="from __main__ import default_dict"))

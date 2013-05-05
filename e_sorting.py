
colors = ['red','orange','yellow','green','blue','indigo','violet']

def use_comparator(): # won't even work in python 3
    def compare_length(c1, c2):
        if len(c1) < len(c2): return -1
        if len(c1) > len(c2): return 1
        return 0
    return sorted(colors, cmp=compare_length)

def use_key():
    return sorted(colors, key=len)

if __name__ == '__main__':
    import timeit
    print("use_comparator = ", timeit.timeit("use_comparator()", setup="from __main__ import use_comparator"))
    print("use_key = ", timeit.timeit("use_key()", setup="from __main__ import use_key"))

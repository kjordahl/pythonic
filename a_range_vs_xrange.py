def using_range():
    a = 0
    for i in range(100):
        a += i

def using_xrange():
    a = 0
    for i in range(100):
        a += i

if __name__ == '__main__':
    import timeit
    print("range = ", timeit.timeit("using_range()", setup="from __main__ import using_range"))
    print("xrange = ", timeit.timeit("using_xrange()", setup="from __main__ import using_xrange"))

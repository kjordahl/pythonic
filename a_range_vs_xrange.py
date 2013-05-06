def using_range(N=100):
    a = 0
    for i in range(N):
        a += i

def using_xrange(N=100):
    a = 0
    for i in xrange(N):
        a += i

if __name__ == '__main__':
    import timeit
    print("range = ", timeit.timeit("using_range()", setup="from __main__ import using_range"))
    print("xrange = ", timeit.timeit("using_xrange()", setup="from __main__ import using_xrange"))

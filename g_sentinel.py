seq = ['red','orange','yellow','green','blue','indigo','violet']

def old_find():
    found = False
    for i, value in enumerate(seq):
        if value == 'indigo':
            found = True
            break
    if not found:
        return -1
    return i

def for_else():
    for i, value in enumerate(seq):
        if value == 'indigo':
            break
    else:
        return -1

    return i

if __name__ == '__main__':
    import timeit
    print("old_find = ", timeit.timeit("old_find()", setup="from __main__ import old_find"))
    print("for_else = ", timeit.timeit("for_else()", setup="from __main__ import for_else"))

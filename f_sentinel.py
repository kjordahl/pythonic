global number
number = 0

def next_number():
    global number
    number += 1
    return number

def looper():
    global number
    total = 0
    number = 0
    while True:
        n = next_number()
        if n == 10:
            break
        total += n

def two_arg_iter():
    global number
    total = 0
    number = 0
    for n in iter(next_number, 10):
        total += n

if __name__ == '__main__':
    import timeit
    print("looper = ", timeit.timeit("looper()", setup="from __main__ import looper"))
    print("two_arg_iter = ", timeit.timeit("two_arg_iter()", setup="from __main__ import two_arg_iter"))

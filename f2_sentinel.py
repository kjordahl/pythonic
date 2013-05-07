import StringIO
s = """red
orange
yellow
green
blue
indigo
violet
"""

def looper():
    f = StringIO.StringIO(s)
    blocks = []
    while True:
        block = f.readline()
        if block == '':
            break
        blocks.append(block)
    f.close()

def two_arg_iter():
    f = StringIO.StringIO(s)
    blocks = []
    for block in iter(f.readline, ''):
        blocks.append(block)
    f.close()

if __name__ == '__main__':
    import timeit
    print("looper = ", timeit.timeit("looper()", setup="from __main__ import looper"))
    print("two_arg_iter = ", timeit.timeit("two_arg_iter()", setup="from __main__ import two_arg_iter"))

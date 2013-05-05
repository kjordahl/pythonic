colors = ['red','orange','yellow','green','blue','indigo','violet']

def old_way():
    red = colors[0]
    orange = colors[1]
    yellow = colors[2]
    green = colors[3]
    blue = colors[4]
    indigo = colors[5]
    violet = colors[6]

def unpack():
    red, orange, yellow, green, blue, indigo, violet = colors

if __name__ == "__main__":
    import timeit
    print("old_way = ", timeit.timeit("old_way()", setup="from __main__ import old_way"))
    print("unpack = ", timeit.timeit("unpack()", setup="from __main__ import unpack"))

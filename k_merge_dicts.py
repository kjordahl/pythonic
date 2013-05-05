early = {"apple" : "green", "banana" : "green", "olive":"green"}
ripe = {"apple" : "red", "banana" : "yellow", "olive" : "black"}
spoiled = {"banana" : "black"}

def old_way():
    d = early.copy()
    d.update(ripe)
    d.update(spoiled)

# introduced in python 3.3.  Oh well.
from collections import ChainMap
def chain_map():
    d = ChainMap(early, ripe, spoiled)

if __name__ == "__main__":
    import timeit
    print("old_way = ", timeit.timeit("old_way()", setup="from __main__ import old_way"))
    print("chain_map = ", timeit.timeit("chain_map()", setup="from __main__ import chain_map"))

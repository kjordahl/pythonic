def influence(m, x, y, dx, dy, partial=''):
    """ Made up influence function
    """
    if partial == 'x':
        return dx + 0.01
    else:
        return dy - 0.01

def tmp_vars(N=10):
    m, x, y = 1, 0, 0
    dt, dx, dy = 0.1, 0.1, 0.1
    for i in xrange(N):
        tmp_x = x + dt * x
        tmp_y = y + dt * y
        tmp_dx = influence(m, x, y, dx, dy, partial='x')
        tmp_dy = influence(m, x, y, dx, dy, partial='y')
        x = tmp_x
        y = tmp_y
        dx = tmp_dx
        dy = tmp_dy

def atomic(N=10):
    m, x, y = 1, 0, 0
    dt, dx, dy = 0.1, 0.1, 0.1
    for i in xrange(N):
        x, y, dx, dy = (x + dt * x,
                        y + dt * y,
                        influence(m, x, y, dx, dy, partial='x'),
                        influence(m, x, y, dx, dy, partial='y'))

if __name__ == "__main__":
    import timeit
    print("tmp_vars = ", timeit.timeit("tmp_vars()", setup="from __main__ import tmp_vars"))
    print("atomic = ", timeit.timeit("atomic()", setup="from __main__ import atomic"))

from utils import read_input_prob2
import heapq
import collections

UNINITIALIZED = -1
INFINITY = int(1e15)

def trace_route(n, k, m, c, f):
    # returns: m + 1 indicies of platforms to jump
    
    # base case: we start from 0
    if n == 0:
        return []
    
    # subproblem: pick the best platform to jump from 
    for i in range(max(0, n - k), n):
        if f[n][m] == dp(i, k, m - 1, c, f) + c[i]:
            return trace_route(i, k, m - 1, c, f) + [n]

    assert False, "unreachable"

def dp(n, k, m, c, f):
    # returns: cost to get to platform n with exactly m jumps
    
    # base case 1: we start from 0
    if n == 0:
        # no jumping, so cost is 0 if m = 0, otherwise infinity
        return 0 if m == 0 else INFINITY
    
    # base case 2: no jumps left and n != 0
    if m == 0:
        return INFINITY

    # memoization: if we have already computed the cost, return it
    if f[n][m] != UNINITIALIZED:
        return f[n][m]

    f[n][m] = INFINITY

    # subproblem: pick the best platform to jump from 
    for i in range(max(0, n - k), n):
        f[n][m] = min(f[n][m], dp(i, k, m - 1, c, f) + c[i])

    return f[n][m]

def task6(n, k, m, c):

    f = [[UNINITIALIZED for _ in range(m + 1)] for _ in range(n + 1)]
    
    dp(n, k, m, c, f)
    
    return f[n][m], f

if __name__ == "__main__":
    
    n, k, m, c = read_input_prob2()
    
    _, f = task6(n, k, m, c)
    
    order = trace_route(n, k, m, c, f)

    for it in order:
        print(it,' ', end="")
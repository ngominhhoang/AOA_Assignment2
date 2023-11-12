from utils import read_input_prob2
import heapq
import collections

INFINITY = int(1e15)

def trace_route(n, k, m, c, f):
    # returns: m + 1 indicies of platforms to jump
    
    # base case: we start from 0
    if n == 0:
        return []
    
    # subproblem: pick the best platform to jump from 
    for i in range(max(0, n - k), n):
        if f[n][m] == f[i][m - 1] + c[i]:
            return trace_route(i, k, m - 1, c, f) + [n]

    assert False, "unreachable"

def dp(n, k, m, c, f):
    # returns: cost to get to platform n with exactly m jumps
    
    # base case: we start from (0, 0)
    f[0][0] = 0

    # iterate through all subproblems
    for i in range(1, n + 1):
        # exact number of jumps (has to be positive)
        for jumps in range(1, m + 1):
            # pick the best platform to jump from
            for j in range(max(0, i - k), i):
                f[i][jumps] = min(f[i][jumps], f[j][jumps - 1] + c[j])

    return f[n][m]

def task6(n, k, m, c):

    f = [[INFINITY for _ in range(m + 1)] for _ in range(n + 1)]
    
    dp(n, k, m, c, f)
    
    return f[n][m], f

if __name__ == "__main__":
    
    n, k, m, c = read_input_prob2()
    
    _, f = task6(n, k, m, c)
    
    order = trace_route(n, k, m, c, f)

    for it in order:
        print(it,' ', end="")
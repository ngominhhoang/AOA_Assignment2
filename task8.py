from dataclasses import dataclass, field
from typing import Any
import heapq
import collections

from utils import read_input_prob2

INFINITY = int(1e15)

def trace_route(n, k, m, c, f):
    # returns: m indicies of platforms to jump
    
    # base case: we start from 0
    if n == 0:
        return []
    
    # subproblem: pick the best platform to jump from 
    for i in range(max(0, n - k), n):
        if f[n][m] == dp(i, k, m - 1, c, f) + c[i]:
            return trace_route(i, k, m - 1, c, f) + [i]

    assert False, "unreachable"

def dp(n, k, m, c, f):
    # returns: cost to get to platform n with exactly m jumps
    
    # base case: we start from (0, 0)
    f[0][0] = 0

    @dataclass(order=True)
    class PrioritizedItem:
        value: int
        index: int=field(compare=False)

    # iterate through all subproblems
    # exact number of jumps (has to be positive)
    for jumps in range(1, m + 1):
        # initialize a min heap
        q = collections.deque()

        for i in range(0, n + 1):
            while q and q[0].index < max(0, i - k):
                q.popleft()

            f[i][jumps] = q[0].value if q else INFINITY

            if i < n:
                while q and q[-1].value > f[i][jumps - 1] + c[i]:
                    q.pop()

                q.append(PrioritizedItem(
                    value=min(f[i][jumps - 1] + c[i], INFINITY), 
                    index=i
                ))

    return f[n][m]

def task8(n, k, m, c):

    f = [[INFINITY for _ in range(m + 1)] for _ in range(n + 1)]
    
    dp(n, k, m, c, f)
    
    return f[n][m], f

if __name__ == "__main__":
    
    n, k, m, c = read_input_prob2()
    
    _, f = task8(n, k, m, c)
    
    order = trace_route(n, k, m, c, f)

    for it in order:
        print(it,'', end="")
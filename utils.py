import sys
from typing import NamedTuple, Any

def read_input_basic(f=sys.stdin):
    # read the input from stdin. The complexity is O(n)
    n, k = map(int, f.readline().split())
    cost = list(map(int, f.readline().split()))
    return n, k, cost

def read_input_prob2(f=sys.stdin):
    # read the input from stdin. The complexity is O(n)
    n, k, m = map(int, f.readline().split())
    cost = list(map(int, f.readline().split()))
    return n, k, m, cost

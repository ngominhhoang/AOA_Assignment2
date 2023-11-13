from utils import read_input_basic
import heapq
import collections

# find the order of platforms
def trace_route(n, k, c, f):
    order = []
    i = n
    while i != 0:
        minn = 1e15
        saved = -1
        for j in range(max(0, i-k), i):
            if f[j] + c[j] < minn:
                minn = f[j] + c[j]
                saved = j
        i = saved
        order.append(saved)
    order.reverse()
    return order

def task2b(n, k, c):
    
    # implement dp function as the bottom-up approach
    f = [1e15 for i in range(0,n+1)]
    f[0] = 0
    for i in range(1,n+1):
        for j in range(max(0,i-k), i):
            f[i] = min(f[i], f[j] + c[j])
    return f[n], f

if __name__ == "__main__":
    
    n, k, c = read_input_basic()
    
    res, f = task2b(n, k, c)
    
    order = trace_route(n, k, c, f)
    order.append(n)
    for it in order:
        print(it, '', end="")

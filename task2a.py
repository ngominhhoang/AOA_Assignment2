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

def task2a(n, k, c):
    #Task 2a: implement dp function as the top-down approach
    def find_min(i):
        if i == 0:
            return 0
        if f[i] != 1e15:
            return f[i]

        for j in range(max(0,i-k), i):
            f[i] = min(f[i], find_min(j)+c[j])
        return f[i]

    f = [1e15 for i in range(0,n+1)]

    f[0] = 0
    return find_min(n), f

if __name__ == "__main__":
    
    n, k, c = read_input_basic()
    
    res, f = task2a(n, k, c)
    
    order = trace_route(n, k, c, f)
    for it in order:
        print(it, '', end="")

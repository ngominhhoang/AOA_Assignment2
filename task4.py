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

def task4(n, k, c):
    
    # improve the dp with deque
    f = [1e15 for i in range(0,n+1)]

    f[0] = 0
    q = collections.deque([(f[0]+c[0], 0)])

    for i in range(1,n+1):
        #print('-----',i)
        while True:
            f_val, index = q[0]
            #print(index)
            if index >= i-k:
                f[i] = f_val
                if i != n:
                    #print(q[-1][0])
                    while len(q) > 0 and f[i]+c[i] <= q[-1][0]:
                        q.pop()
                    q.append((f[i]+c[i],i))
                break
            else:
                q.popleft()

    return f[n], f

if __name__ == "__main__":
    
    n, k, c = read_input_basic()
    
    res, f = task4(n, k, c)
    
    order = trace_route(n, k, c, f)
    order.append(n)
    for it in order:
        print(it, '', end="")

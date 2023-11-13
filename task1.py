def read_input():
    correct_input = False
    while not correct_input:
        try:
            n, k = map(int, input().split())
            correct_input = True
        except:
            print("You must enter two integers. Please try again: ")
            continue

    cost = [0] * n
    correct_input = False
    while not correct_input:
        try:
            cost = list(map(int, input().split()))
            correct_input = True
        except:
            print("You must enter integers. Please try again: ")
            continue

    # print(n, k)
    # print(cost)
    return n, k, cost


def alg1(n, k, cost):
    minimum = [-1] * (n + 1)
    minimum[0] = 0
    minimum_order = [-1]
    minimum_order[0] = 0
    if n == 0:
        return minimum, minimum_order
    else:
        for i in range(1, k + 1):
            if n - i >= 0:
                minimum_placeholder, minimum_placeholder_order = alg1(n - i, k, cost)
                minimum_placeholder.append(minimum_placeholder[n - i] + cost[n - i])
                minimum_placeholder_order.append(n)
                if minimum[-1] == -1 or minimum[-1] > minimum_placeholder[-1]:
                    minimum_order = minimum_placeholder_order
                    minimum[-1] = minimum_placeholder[-1]
                    minimum[-1 - i] = minimum_placeholder[-2]
                    j = 1
                    while -1 - i - j >= -n:
                        minimum[-1 - i - j] = minimum_placeholder[-2 - j]
                        j += 1

        return minimum, minimum_order

if __name__ == "__main__":
    n, k, cost = read_input()
    minimum, minimum_order = alg1(n, k, cost)
    for i in minimum_order[0:-1]:
        print(i, '', end="")

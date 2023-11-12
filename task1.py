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
    if n == 0:
        return minimum
    else:
        for i in range(1, k + 1):
            if n - i >= 0:
                minimum_placeholder = alg1(n - i, k, cost)
                minimum_placeholder.append(minimum_placeholder[n - i] + cost[n - i])
                if minimum[-1] == -1 or minimum[-1] > minimum_placeholder[-1]:
                    minimum[-1] = minimum_placeholder[-1]
                    minimum[-1 - i] = minimum_placeholder[-2]
                    j = 1
                    while -1 - i - j >= -n:
                        minimum[-1 - i - j] = minimum_placeholder[-2 - j]
                        j += 1

        return minimum


"""
def alg1(n, k, cost):
    minimum = [-1] * (n + 1)
    minimum[0] = 0
    for position in range(n):
        for i in range(position + 1, position + k + 1):
            if i > n:
                continue
            elif minimum[i] == -1 or minimum[position] + cost[position] < minimum[i]:
                minimum[i] = minimum[position] + cost[position]

    print(minimum)
    print(minimum[n])
    return minimum
"""

if __name__ == "__main__":
    n, k, cost = read_input()
    minimum = alg1(n, k, cost)
    # print(minimum)
    print(minimum[n])

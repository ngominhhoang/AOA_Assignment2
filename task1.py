# Reads input
def read_input():
    # Reads user input for the number of platforms (n) and maximum jump length (k).
    correct_input = False
    while not correct_input:
        try:
            n, k = map(int, input().split())
            correct_input = True
        except:
            print("You must enter two integers. Please try again: ")
            continue

    # Reads user input for the cost of jumping from each platform (cost).
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


# Algorithm 1, brute-force algorithm
def alg1(n, k, cost):
    minimum = [-1] * (n + 1)
    minimum[0] = 0
    minimum_order = [-1]
    minimum_order[0] = 0
    if n == 0:
        # Base case
        return minimum, minimum_order
    else:
        for i in range(1, k + 1):
            if n - i >= 0:
                # Recursive call, ultimately k sub-problems that decrease by as little as 1 each iteration. O(k^n)
                minimum_placeholder, minimum_placeholder_order = alg1(n - i, k, cost)

                # Potentially our new minimum and minimum order.
                minimum_placeholder.append(minimum_placeholder[n - i] + cost[n - i])
                minimum_placeholder_order.append(n)

                # If our calculated minimum is smaller than our current minimum, we have a new solution.
                if minimum[-1] == -1 or minimum[-1] > minimum_placeholder[-1]:
                    minimum_order = minimum_placeholder_order
                    minimum[-1] = minimum_placeholder[-1]
                    minimum[-1 - i] = minimum_placeholder[-2]
                    j = 1
                    while -1 - i - j >= -n:
                        minimum[-1 - i - j] = minimum_placeholder[-2 - j]
                        j += 1

        return minimum, minimum_order


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

# Main function for running code.
if __name__ == "__main__":
    n, k, cost = read_input()
    minimum, minimum_order = alg1(n, k, cost)
    # print(minimum)
    # print(minimum[n])
    # print(minimum_order)

    # Prints the platform jumping order for each platform.
    for i in minimum_order[:-1]:
        print(i, '', end="")

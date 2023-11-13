# Reads input
def read_input():
    # Reads user input for the number of platforms (n), maximum jump length (k), and required number of jumps (m).
    correct_input = False
    while not correct_input:
        try:
            n, k, m = map(int, input().split())
            correct_input = True
        except:
            print("You must enter three integers. Please try again: ")
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

    """
    correct_input = False
    while not correct_input:
        try:
            m = int(input())
            correct_input = True
        except:
            print("You must enter an integer. Please try again: ")
            continue
    """

    # print(n, k)
    # print(cost)
    # print(m)
    return n, k, cost, m

# Algorithm 5, brute-force algorithm
def alg5(n, k, cost, m, final_n):
    minimum = [-1] * (n + 1)
    minimum_order = [-1]
    if n == 0:
        # Base case. If m is 0, we have the required number of jumps. Otherwise, it's not a viable solution.
        if m == 0:
            minimum[0] = 0
            minimum_order[0] = 0
            return minimum, minimum_order
        else:
            return minimum, minimum_order
    else:
        for i in range(1, k + 1):
            if n - i >= 0:
                # Recursive call, ultimately k sub-problems that decrease by as little as 1 each iteration. O(k^n)
                minimum_placeholder, minimum_placeholder_order = alg5(n - i, k, cost, m - 1, final_n)

                # Potentially our new minimum and minimum order. Ignored if not required number of jumps.
                if minimum_placeholder[-1] != -1:
                    minimum_placeholder.append(minimum_placeholder[n - i] + cost[n - i])
                    minimum_placeholder_order.append(n)
                else:
                    minimum_placeholder.append(-1)
                    minimum_placeholder_order.append(-1)

                # If our calculated minimum is smaller than our current minimum, we have a new solution.
                if minimum_placeholder[-1] != -1 and (minimum[-1] == -1 or minimum[-1] > minimum_placeholder[-1]):
                    minimum_order = minimum_placeholder_order
                    minimum[-1] = minimum_placeholder[-1]
                    minimum[-1 - i] = minimum_placeholder[-2]
                    j = 1
                    while -1 - i - j >= -n:
                        minimum[-1 - i - j] = minimum_placeholder[-2 - j]
                        j += 1

        return minimum, minimum_order


# Main function for running code.
if __name__ == "__main__":
    n, k, cost, m = read_input()
    final_n = n
    minimum, minimum_order = alg5(n, k, cost, m, final_n)
    # print(minimum)

    # Prints the platform jumping order for each platform if a solution exists.
    if minimum[n] == -1:
        print("No solution possible.")
    else:
        # print(minimum[n])
        # print(minimum_order)
        for i in minimum_order[:-1]:
            print(i, '', end="")

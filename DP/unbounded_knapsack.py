"""
Given a set of items, each with a weight and a value,
determine the number of each item to include in a collection
so that the total weight is less than or equal to a given limit (knapsack capacity)
and the total value is as large as possible.
Each item can either be picked up many times.

input:
weights = [10, 20, 30]
values = [60, 100, 120]
capacity = 50

output = 300
"""


def unbounded_knapsack(weights, values, max_capacity):
    n = len(weights)
    dp = [[0 for _ in range(max_capacity + 1)] for _ in range(n + 1)]

    # dp[i][capacity] = max value in knapsack of size 'capacity' considering items 0..i-1
    for i in range(1, n + 1):
        for capacity in range(1, max_capacity + 1):
            wt = weights[i - 1]
            val = values[i - 1]
            if wt > capacity:
                dp[i][capacity] = dp[i - 1][capacity]
            else:
                dp[i][capacity] = max(dp[i - 1][capacity], val + dp[i][capacity - wt])

    return dp[n][max_capacity]


print(unbounded_knapsack([10, 20, 30], [60, 100, 120], 50))

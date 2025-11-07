def knapsack_01(weights, values, capacity):
    n = len(values)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Build table dp[][] in bottom-up manner
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                # Take max of including or excluding the item
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                # If item weight exceeds current capacity, skip it
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]

number_of_items = int(input("Enter the number of items: "))

values = []
weights = []

# Input values and weights of each item
for i in range(number_of_items):
    value = int(input(f"Enter the value of item {i + 1}: "))
    weight = int(input(f"Enter the weight of item {i + 1}: "))
    values.append(value)
    weights.append(weight)

capacity = int(input("Enter capacity of knapsack: "))

max_value = knapsack_01(weights, values, capacity)
print("Maximum value in Knapsack =", max_value)

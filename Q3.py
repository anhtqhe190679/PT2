def knapsack(N, W, items):
    # Initialize a 2D array to store the maximum profit for each subproblem
    dp = [[0] * (W + 1) for _ in range(N + 1)]

    # Fill the dp array
    for i in range(1, N + 1):
        weight_i, value_i, _ = items[i - 1]
        for w in range(1, W + 1):
            if weight_i <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weight_i] + value_i)
            else:
                dp[i][w] = dp[i - 1][w]

    # Trace back to find the selected items
    selected_items = []
    i, w = N, W
    while i > 0 and w > 0:
        if dp[i][w] != dp[i - 1][w]:
            weight_i, value_i, name_i = items[i - 1]
            selected_items.append((name_i, w // weight_i))
            w -= weight_i
        i -= 1

    return dp[N][W], selected_items

def main():
    with open("BAG.INP", "r") as file:
        N, W = map(int, file.readline().split())
        items = []
        for _ in range(N):
            weight, value, name = file.readline().split()
            items.append((int(weight), int(value), name))

    max_profit, selected_items = knapsack(N, W, items)

    # Write result to output file
    with open("Result", "w") as file:
        file.write(str(max_profit) + "\n")
        for name, quantity in selected_items:
            file.write(f"{name} {quantity}\n")

if __name__ == "__main__":
    main()

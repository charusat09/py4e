#code
def binary_knapsack(values, weights, capacity):
    n = len(values)
    profits = [[0 for j in range(n+1)] for i in range(capacity+1)]
    for cap in range(1,capacity+1):
        for item in range(1, n+1):
            if weights[item-1] <= cap:
                profits[cap][item] = max( profits[cap-weights[item-1]][item-1] + values[item-1],
                                          profits[cap][item-1])
            else:
                profits[cap][item] = profits[cap][item-1]

    return profits[capacity][n]

tn = int(input())
for tc in range(tn):
    n = int(input())
    cap = int(input())
    arr2 = list(map(int, input().split()))
    arr3 = list(map(int, input().split()))
    print(binary_knapsack(arr2, arr3, cap))

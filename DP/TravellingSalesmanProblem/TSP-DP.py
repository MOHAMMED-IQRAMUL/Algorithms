def tsp(graph):
    
    n = len(graph)
    dp = [[float('inf')] * n for _ in range(1 << n)] 

    for i in range(n):
        dp[1 << i][i] = 0

    for subset in range(2, 1 << n):  
        for j in range(n):
            if subset & (1 << j) != 0: 
                for k in range(n):
                    if (subset & (1 << k)) != 0 and j != k:  
                        dp[subset][j] = min(dp[subset][j], graph[j][k] + dp[subset ^ (1 << k)][k])

    minimum_cost = min(dp[(1 << n) - 1][i] for i in range(n))

    return minimum_cost  # Return the minimum cost

graph1 = [[0, 10, 15, 20], [5, 0, 9, 10], [6, 13, 0, 12], [8, 8, 9, 0]]
graph2 = [[0, 5, 10, 7], [6, 0, 11, 5], [8, 5, 0, 6], [9, 4, 11, 0]]

result1 = tsp(graph1)
result2 = tsp(graph2)

print("Graph 1: Minimum Cost =", result1)
print("Graph 2: Minimum Cost =", result2)

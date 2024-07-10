# This program illustrate 0/1 Knapsack problem solved using Dynamic Programming

def knapsack(OWP, M):
    """
    int[3][N] OWP --> Object, Weight and Profit of items
    int M --> Maximum weight that can be carried
    """
    N = len(OWP)
    DP = [[0 for i in range(M+1)] for j in range(N+1)]
    for i in range(1, N+1):
        for j in range(1, M+1):
            if OWP[i-1][1] <= j:
                DP[i][j] = max(OWP[i-1][2] + DP[i-1][j-OWP[i-1][1]], DP[i-1][j])
            else:
                DP[i][j] = DP[i-1][j]
    print("DP Table : ")
    for row in DP:
        print(row)
    print_knapsack(DP, OWP, M)
    return DP[N][M]

# Program To Print Which Objects are included in the Knapsack
def print_knapsack(DP, OWP, M):
    """
    int[M+1][N+1] DP --> DP Table
    int[3][N] OWP --> Object, Weight and Profit of items
    int M --> Maximum weight that can be carried
    """
    print("Objects included in the Knapsack are: ", end='')
    N = len(OWP)
    i = N
    j = M
    while i > 0 and j > 0:
        if DP[i][j] != DP[i-1][j]:
            print(OWP[i-1][0], end=' ')
            j -= OWP[i-1][1]
        i -= 1
    print()


def main2():
    OWP = [[1, 100, 500], [2, 50, 200], [3, 20, 20], [4, 10, 60], [5, 7, 84], [6, 3, 45]]
    M = 165
    print("Objects\tWeight\tProfit")
    for row in OWP:
        print(f"{row[0]}\t{row[1]}\t{row[2]}") 
    print("Maximum Weight : ", M)
    print("Maximum Profit : ", knapsack(OWP, M))
main2()

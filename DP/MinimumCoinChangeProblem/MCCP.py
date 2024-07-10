def main(Coins, W):
    N = len(Coins)
    DP = [[0 for i in range(W + 1)] for j in range(N)]

    for i in range(0, W+1):
        DP[0][i] =  i   

    for i in range(1, N):
        for j in range(1, W + 1):
            if j >= Coins[i]:
                DP[i][j] = min(DP[i-1][j], DP[i][j - Coins[i]] +1 )  
            else:
                DP[i][j] = DP[i-1][j]

    Coins_Count = {}
    i, j = N-1, W
    while j > 0:
        if DP[i][j] != DP[i-1][j]:
            Coins_Count[Coins[i]] = Coins_Count.get(Coins[i], 0) + 1
            j = j - Coins[i]
        else:
            i -= 1

    print("DP Table : ")
    for row in DP:
        print(row)
    print("Coins and Their Count :")
    for key, value in Coins_Count.items():
        print(f"{key} : {value}")
    print("Minimum No of Coins : ", DP[N-1][W])
    print()


Coins = [1, 5, 6, 9]
W = 10
main(Coins, W)

Coins = [1, 5, 6, 9]
W = 11
main(Coins, W)

Coins = [1, 5, 6, 8]
W = 11
main(Coins, W)

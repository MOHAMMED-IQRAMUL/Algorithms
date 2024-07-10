def main(PW, M):
    N = len(PW)
    DP = [[0 for _ in range(M+1)] for _ in range(N+1)]
    PW.sort(key=lambda x: x[1])
    
    for i in range(1, N+1):
        for w in range(M+1):
            j = w-PW[i-1][1]
            if j >= 0 :
                DP[i][w] = max(DP[i-1][w], (DP[i-1][j]+PW[i-1][0]))
            else:
                DP[i][w] = DP[i-1][w]
    objs, i, j = [0]*N, N, M
    
    while i > 0 and j > 0:
        if DP[i][j] != DP[i-1][j]:
            objs[i-1] = 1
            j -= PW[i-1][1]
        i -= 1

    print("Profit\tWeight")
    for row in PW:
        print(row[0], "\t", row[1])
    print("Answer - Maximum Profit : ", DP[N][M])
    for row in DP:
        print(row)
    print("Objects : ")
    for o in objs:
        print(o, end=" ")
    else:
        print()
    print()
    
Case1 = {
    'PW':[[1, 2], [2, 3], [5, 4], [6, 5]], # Profit, Weight
    'M': 8
}
main(Case1['PW'], Case1['M'])
# --> 8

Case2 = {
    'PW':[[10, 1], [12, 2], [15, 2], [20, 3]], # Profit, Weight
    'M': 5
}
main(Case2['PW'], Case2['M'])
# --> 37

Case3 = {
    'PW':[[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8]], # Profit, Weight
    'M': 11
}






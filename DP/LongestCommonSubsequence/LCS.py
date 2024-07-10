def main(S1, S2):
    
    M = len(S1)
    N = len(S2)
    
    DP = [[0 for _ in range(N+1)] for _ in range(M+1)]
    
    for i in range(1, M+1):
        for j in range(1, N+1):
            if S1[i-1] == S2[j-1]:
                DP[i][j] = DP[i-1][j-1] + 1
            else:
                DP[i][j] = max(DP[i-1][j], DP[i][j-1])
    SEQ = ""
    i, j = M, N
    while i > 0 and j > 0:
        if S1[i-1] == S2[j-1]:
            SEQ = S1[i-1] + SEQ
            i -= 1
            j -= 1
        else:
            if DP[i][j] == DP[i][j-1]:
                j -= 1
            # if DP[i-1][j] > DP[i][j-1]:
            #     i -= 1
            # else:
            #     j -= 1
            
    print("DP Table : ")
    for row in DP:
        print(row)
    print("Longest Common Sub-Sequence is : ", SEQ)
    print("Length Of Longest Sub-Sequence is : ", DP[M][N])
    print()

main("BD", "ABCD")
main("STONE", "LONGEST")
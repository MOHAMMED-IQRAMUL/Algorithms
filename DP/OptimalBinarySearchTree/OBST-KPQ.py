def main(Key, Pi, Qi):
    
    N = len(Qi)
    DP = [[0 for _ in range(N)] for _ in range(N)]
    W  = [[0 for _ in range(N)] for _ in range(N)]
    R  = [[0 for _ in range(N)] for _ in range(N)]
    
    for S in range(0, N):
        for i in range(0, N-S): 
            j = i+S
            if i == j :
                DP[i][j] = 0
                R[i][j] = 0
                W[i][j] = Qi[i]
            else:
                DP[i][j] = 32767 
                W[i][j] = W[i][j-1] + Pi[j] + Qi[j] 
                for k in range(i, j+1):
                    q = DP[i][k-1] + DP[k][j] + W[i][j]
                    if q < DP[i][j]:
                        DP[i][j] = q
                        R[i][j] = k
                        
    print("DP Table : ", DP)
    print("Weights : ", W)
    print("Roots : ", R)              
    print("Optimal Binary Search Tree Cost : ", DP[0][N-1])
    print()
    
Data = [ [0, 10, 20, 30, 40], [0, 3, 3, 1, 1], [2, 3, 1, 1, 1] ]
# [Key], [Pi], [Qi] 
main(Data[0], Data[1], Data[2] )
# Data = [ [10, 4], [20, 3]] # Key, Frequency
# main(Data)
# Data = [ [10, 3], [20, 4]] # Key, Frequency
# main(Data)

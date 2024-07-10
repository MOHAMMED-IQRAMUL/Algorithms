def main(KF):
    N = len(KF) + 1
    DP = [[0 for _ in range(N)] for _ in range(N)]
    ROOT = [[0 for _ in range(N)] for _ in range(N)]
    for S in range(0, N):
        for i in range(0, N-S):
            j = i+S
            W = sum(key[1] for key in KF[i:j])  
            DP[i][j] = 0 if i == j else 32767
            for k in range(i, j+1):
                q = DP[i][k-1] + DP[k][j] + W 
                if q < DP[i][j]:
                    DP[i][j] = q
                    ROOT[i][j] = k
    print("Roots : ", ROOT)             
    print("DP Table :", DP)
    print("Optimal Binary Search Tree Cost : ", DP[0][N-1])
    print()

def Generate_Tree(KF, ROOT):
    pass

Data = [ [10, 4], [20, 2], [30, 6], [40, 3] ] # Key, Frequency
main(Data)
Data = [ [10, 4], [20, 3]] # Key, Frequency
main(Data)
Data = [ [10, 3], [20, 4]] # Key, Frequency
main(Data)

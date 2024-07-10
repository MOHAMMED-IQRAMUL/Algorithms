from math import inf
I = (inf)


def main(A0):
    
    print("Graph :- ")
    for row in A0:
        print(row)
    
    n = len(A0)
    Ans = A0
    
    for M in range(0,n):
        for i in range(n):
            for j in range(n):
                if i == M or j == M or i == j:
                     Ans[i][j] = Ans[i][j]
                else:
                    Ans[i][j] = min(Ans[i][j], Ans[i][M] + Ans[M][j])
        Ans = Ans
    
    print("Solution :- ")  
    for row in Ans:
        print(row)        

M1 = [[0, 3, I, 7], [8, 0, 2, I], [5, I, 0, 1], [2, I, I, 0]]
main(M1)

M2 = [[0, 4, I, 5, I], [I, 0, 1, I, 6], [2, I, 0, 3, I], [I, I, 1, 0, 2], [1, I, I, 4, 0]]
main(M2)

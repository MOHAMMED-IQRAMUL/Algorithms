def main(Data):
    
    P = Data['P'] #Dimensions
    n = Data['n'] #Number of Matrices + 1
    M = [[0]*n for _ in range(n)] #Matirx
    S = [[0]*n for _e in range(n)] #Store K values
    
    for d in range(1, n-1):
        for i in range(1, n-d):
            j = i+d
            min = 32767
            for k in range(i, j):
                q = M[i][k] + M[k+1][j] + P[i-1]*P[k]*P[j]
                if q < min:
                    min = q
                    S[i][j] = k
            M[i][j] = min
    print("Dimensions of Matrices : ", end = " ")
    for i in range(n-1):
        print( "M", i+1, "(", P[i], " X ", P[i+1], ") ", end = " ", sep="")
    else:
        print()
    print("Minimum No Of Multiplication Possible",M[1][n-1])
    

D1 = {
    'P' : [5, 2, 10, 5], #Dimensions
    'n' : 4 #Number of Matrices + 1
}
D2 = {
    'P' : [2, 5, 10, 3], #Dimensions
    'n' : 4 #Number of Matrices + 1
}
D3 = {
    'P' : [2, 1, 3, 4, 5], #Dimensions
    'n' : 5 #Number of Matrices + 1
}
D4 = {
    'P' : [5, 4, 6, 2, 7], #Dimensions
    'n' : 5 #Number of Matrices + 1
}

print("Problem : D1")
main(D1)
print()
print("Problem : D2")
main(D2)
print()
print("Problem : D3")
main(D3)
print()
print("Problem : D4")
main(D4)
print()
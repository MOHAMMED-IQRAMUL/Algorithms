def main(S1, S2):
    def LCS(i, j):
        if i == len(S1) or j == len(S2):
            return 0
        elif S1[i] == S2[j]:
            return 1 + LCS(i+1, j+1)
        else:
            return max(LCS(i+1, j), LCS(i, j+1))
        
    ANS = LCS(0, 0)
    print("Length Of Longest Common Sub-Sequence is : ", ANS)
    print()

main("BD", "ABCD")
main("STONE", "LONGEST")
#   KnapSack Problem Using Brute Force

def KnapSack_Greedy(WP, MaxWeight):
    WP.sort(key=lambda x: x[1]/x[0], reverse=True)
    TotalValue = 0
    TotalWeight = 0
    for i in range(len(WP)):
        if TotalWeight + WP[i][0] <= MaxWeight:
            TotalValue += WP[i][1]
            TotalWeight += WP[i][0]
        else:
            TotalValue += (MaxWeight - TotalWeight) * (WP[i][1] / WP[i][0])
            TotalWeight = MaxWeight
            break
    return TotalValue

def main():
    Arr1 = [ [2,10], [1,5], [3,15], [4,20] ]
    MaxWeight = 5
    print(KnapSack_Greedy(Arr1, MaxWeight))
    
    Arr2 = [ [5, 30], [10, 40],[15, 45], [22, 77], [25, 90] ]
    MaxWeight = 60
    print(KnapSack_Greedy(Arr2, MaxWeight))
    
    Arr3 = [ [40, 280], [10, 100],[20, 120], [24, 120] ]
    MaxWeight = 60
    print(KnapSack_Greedy(Arr3, MaxWeight))
    
main()
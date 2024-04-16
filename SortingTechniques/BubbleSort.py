def BubbleSort(Arr):
    for i in range(len(Arr)):
        flag = False 
        for j in range(len(Arr) - 1 - i):
            if Arr[j] > Arr[j + 1]:
                Arr[j], Arr[j + 1] = Arr[j + 1], Arr[j]
                flag = True
        if flag : break
    return Arr

def SelectionSort(Arr):
    for i in range(len(Arr)-1):
        k = i
        for j in range(i, len(Arr)):
            if Arr[j] < Arr[k]:
                k = j
        Arr[i], Arr[k] = Arr[k], Arr[i]
   
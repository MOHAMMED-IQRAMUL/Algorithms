
def mid(L,H):
    return (L + H) // 2

def mergeDiff(A,B):
    C = []
    i = 0
    j = 0
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            C.append(A[i])
            i += 1
        else:
            C.append(B[j])
            j += 1
    if i < len(A):
        C.extend(A[i:])
    else:
        C.extend(B[j:])
    return C

def mergeSelf(A,l,m,h):
    i = l
    j = m + 1
    B = []
    while i <= m and j <= h:
        if A[i] < A[j]:
            B.append(A[i])
            i += 1
        else:
            B.append(A[j])
            j += 1
    if i <= m:
        B.extend(A[i:m+1])
    else:
        B.extend(A[j:h+1])
    A[l:h+1] = B
    return A

def mergeRecursiveSort(A,L,H):
    if L < H :
        mergeRecursiveSort(A, L, mid(L, H))
        mergeRecursiveSort(A, mid(L, H) + 1, H)
        mergeSelf(A, L, mid(L, H), H)
  
def mergeing():
    A = [2,4,6,8,10]
    B = [1,3,5,7,9]
    print(mergeDiff(A, B))
    
    
    C = [1,3,5,7,9,2,4,6,8]
    print(mergeSelf(C, 0, 4, 8))
    D = [1,2,4,3,5,7,1,1]
    print(mergeSelf(D, 0, 2, 4))
    
    print(mergeDiff(C[0:5],C[5:9]))
    print(mergeSelf(A+B, 0, len(A) - 1, len(A) + len(B) - 1))
# mergeing()

def Sorting():

    print("RECURSIVE APPROACH")
    arr1 = [9,8,7,6,5,4,3,2,1]
    print(arr1, end=" --> ")
    mergeRecursiveSort(arr1, 0, len(arr1) - 1)
    print(arr1)

    arr2 = [1,2,3,4,5,6,7,8,9]
    print(arr2, end=" --> ")
    mergeRecursiveSort(arr2, 0, len(arr2) - 1)
    print(arr2)

    arr1 = [9,8,7,6,5,4,3,2,1,0]
    print(arr1, end=" --> ")
    mergeRecursiveSort(arr1, 0, len(arr1) - 1)
    print(arr1)

    arr2 = [0,1,2,3,4,5,6,7,8,9]
    print(arr2, end=" --> ")
    mergeRecursiveSort(arr2, 0, len(arr2) - 1)
    print(arr2)
    
    
# Sorting()

def Chat_GPT():
    def merge_sort(arr):
        if len(arr) <= 1:
            return arr
        
        def merge(left, right):
            result = []
            while left and right:
                if left[0] < right[0]:
                    result.append(left.pop(0))
                else:
                    result.append(right.pop(0))
            return result + left + right
        n = len(arr)
        size = 1
        while size < n:
            for start in range(0, n, 2*size):
                mid = min(start + size, n)
                end = min(start + 2*size, n)
                arr[start:end] = merge(arr[start:mid], arr[mid:end])
            size *= 2
        return arr


    arr = [38, 27, 43, 3, 9, 82, 10]
    print("Original array:", arr)
    sorted_arr = merge_sort(arr)
    print("Sorted array:", sorted_arr)


print(end="\n\n\n\n")
###### ********************************* #######

import random
def TestCase():
    
    def generate(size, min_num, max_num):
        return [random.randint(min_num, max_num) for _ in range(size)]
    
    def run_Test(size, min_num, max_num):
        
        print("RECURSIVE APPROACH")
        arr1 = generate(size, min_num, max_num)
        print(arr1, end=" --> ")
        mergeRecursiveSort(arr1, 0, len(arr1) - 1)
        print(arr1)
        
        
    print("\nT1")
    for i in range(1,6):
        print(f"\nTEST CASE {i}\n")
        run_Test(i*10, 0, 100)
        
    print("\n\nT2")
    for i in range(1,6):
        print(f"\nTEST CASE {i}\n")
        run_Test(i*8, 10, 55)
        
    print("\n\nT3")
    for i in range(1,6):
        print(f"\nTEST CASE {i}\n")
        run_Test(i*9, 9, 999)
        
    print("\n\nT4")
    for i in range(1,6):
        print(f"\nTEST CASE {i}\n")
        run_Test(50, 0, 10000)
        
    print("\n\nT5")
    for i in range(1,6):
        print(f"\nTEST CASE {i}")
        run_Test(100, 100, 1000) 
# TestCase()  



gglobalRecursiveTotalCount = 0
gglobalRecursiveTrueCount = 0
gglobalIterative1TotalCount = 0
gglobalIterative1TrueCount = 0
gglobalIterative2TotalCount = 0
gglobalIterative2TrueCount = 0
gglobalIterative3TotalCount = 0
gglobalIterative3TrueCount = 0
gglobalIterative4TotalCount = 0
gglobalIterative4TrueCount = 0
gTotal = 0
gTotalTrue = 0

def TestCaseBoolean():
    
    def generate(size, min_num, max_num):
        return [random.randint(min_num, max_num) for _ in range(size)]
    
    def run_Test(size, min_num, max_num):
        global gglobalRecursiveTotalCount, gglobalRecursiveTrueCount, gglobalIterative1TotalCount, gglobalIterative1TrueCount, gglobalIterative2TotalCount, gglobalIterative2TrueCount, gglobalIterative3TotalCount, gglobalIterative3TrueCount, gglobalIterative4TotalCount, gglobalIterative4TrueCount, gTotal, gTotalTrue
        
        print("RECURSIVE APPROACH")
        gglobalRecursiveTotalCount += 1
        arr1 = generate(size, min_num, max_num)
        arr2 = arr1.copy()
        mergeRecursiveSort(arr2, 0, len(arr1) - 1)
        print(sorted(arr1) == arr2)
        if sorted(arr1) == arr2:
            gglobalRecursiveTrueCount += 1
            
            
        gTotal = gglobalRecursiveTotalCount + gglobalIterative1TotalCount + gglobalIterative2TotalCount + gglobalIterative3TotalCount + gglobalIterative4TotalCount
        gTotalTrue = gglobalRecursiveTrueCount + gglobalIterative1TrueCount + gglobalIterative2TrueCount + gglobalIterative3TrueCount + gglobalIterative4TrueCount


    print("\nT1")
    for i in range(1,6):
        print(f"\nTEST CASE {i}\n")
        run_Test(i*10, 0, 100)
        
    print("\n\nT2")
    for i in range(1,6):
        print(f"\nTEST CASE {i}\n")
        run_Test(i*8, 10, 55)
        
    print("\n\nT3")
    for i in range(1,6):
        print(f"\nTEST CASE {i}\n")
        run_Test(i*9, 9, 999)
        
    print("\n\nT4")
    for i in range(1,6):
        print(f"\nTEST CASE {i}\n")
        run_Test(50, 0, 10000)
        
    print("\n\nT5")
    for i in range(1,6):
        print(f"\nTEST CASE {i}")
        run_Test(100, 100, 1000)       
TestCaseBoolean()       
gTotal = gglobalRecursiveTotalCount + gglobalIterative1TotalCount + gglobalIterative2TotalCount + gglobalIterative3TotalCount + gglobalIterative4TotalCount
gTotalTrue = gglobalRecursiveTrueCount + gglobalIterative1TrueCount + gglobalIterative2TrueCount + gglobalIterative3TrueCount + gglobalIterative4TrueCount
print(f"Total Recursive Count: {gglobalRecursiveTotalCount}")
print(f"Total Recursive True Count: {gglobalRecursiveTrueCount}")
print(f"Total Iterative 1 Count: {gglobalIterative1TotalCount}")
print(f"Total Iterative 1 True Count: {gglobalIterative1TrueCount}")
print(f"Total Iterative 2 Count: {gglobalIterative2TotalCount}")
print(f"Total Iterative 2 True Count: {gglobalIterative2TrueCount}")
print(f"Total Iterative 3 Count: {gglobalIterative3TotalCount}")
print(f"Total Iterative 3 True Count: {gglobalIterative3TrueCount}")
print(f"Total Iterative 4 Count: {gglobalIterative4TotalCount}")
print(f"Total Iterative 4 True Count: {gglobalIterative4TrueCount}")
print(f"Total Count: {gTotal}")
print(f"Total True Count: {gTotalTrue}")

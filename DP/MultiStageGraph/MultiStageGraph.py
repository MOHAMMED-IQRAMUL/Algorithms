def main():
    Stages = int(input("Enter No of Stages "))
    min = 32767
    n = int(input("Enter No of Vertices "))
    cost, d, path = [0] * (n+1), [0] * (n+1), [0] * (Stages+1)
    # c = [input(f"Enter {n+1} X {n+1} Graph matrix ")]
    c = [
        [0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,9,7,3,2,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,4,2,1,0,0,0,0],
        [0,0,0,0,0,0,2,7,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,11,0,0,0,0],
        [0,0,0,0,0,0,0,11,8,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,6,5,0,0],
        [0,0,0,0,0,0,0,0,0,4,3,0,0],
        [0,0,0,0,0,0,0,0,0,0,5,6,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,4],
        [0,0,0,0,0,0,0,0,0,0,0,0,2],
        [0,0,0,0,0,0,0,0,0,0,0,0,5],
        [0,0,0,0,0,0,0,0,0,0,0,0,0]]
    
    c = [
        [0,0,0,0,0,0,0,0,0],
        [0,0,1,2,5,0,0,0,0],
        [0,0,0,0,0,4,11,0,0],
        [0,0,0,0,0,9,5,16,0],
        [0,0,0,0,0,0,0,2,0],
        [0,0,0,0,0,0,0,0,18],
        [0,0,0,0,0,0,0,0,13],
        [0,0,0,0,0,0,0,0,2],
        [0,0,0,0,0,0,0,0,0]
        ]
    
    i = n-1
    while i >= 1:
        min = 32767
        for k in range(i+1, n+1, 1):
            if c[i][k] != 0 and (c[i][k]+cost[k]) < min:
                min = (c[i][k]+cost[k])
                d[i] = k
        cost[i] = min
        i -= 1 
    path[1], path[Stages] = 1, n
    for i in range(2, Stages, 1):
        path[i] = d[path[i-1]]
    print("\nCost is ", cost[1])
    print("\nPath is ")
    for i in range(1, Stages+1, 1):
        print(path[i], end="->" if i != Stages else " ")
        
    
main()
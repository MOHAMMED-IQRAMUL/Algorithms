def main(Graph):

    def TSP(S, V):
        if len(V) == 0:
            return Graph[S][0]
        Min = []
        for k in V:
            i = V.index(k)
            V_copy = V[:]
            Min.append(TSP(k, V_copy[:i] + V_copy[i+1:]) + Graph[S][k])
        return min(Min)

    V = [i for i in range(1, len(Graph))]
    Answer = TSP(0, V)
    print(Answer)
    print()
graph = [[0, 10, 15, 20], [5, 0, 9, 10], [6, 13, 0, 12], [8, 8, 9, 0]]
main(graph)
#==> 35, 40, 43    ---    1 --> 2 --> 4 --> 3

graph = [[0, 5, 10, 7], [6, 0, 11, 5], [8, 5, 0, 6], [9, 4, 11, 0]] 
#==> 29, 26, 29    ---    1 --> 3 --> 4 --> 2
main(graph)

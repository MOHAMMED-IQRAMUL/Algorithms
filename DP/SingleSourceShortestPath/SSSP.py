def main(graph, source):
    distances = {vertex: float('inf') for vertex in graph}
    distances[source] = 0

    for _ in range(len(graph)):
        for u in graph:
            for v, weight in graph[u].items():
                if distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight

    for u in graph:
        for v, weight in graph[u].items():
            if distances[u] + weight < distances[v]:
                print("Graph contains negative weight cycle")
                break

    for vertex, distance in distances.items():
        print(f"Distance from {source} to {vertex}: {distance}")
    else:
        print()


graph = {
    'A': {'B': 10, 'C': 5},
    'B': {'C': -8},
    'C': {}
}
source = 'A'
main(graph, source) 
# --> 0, 10, 2

graph = {
    '1': {'2': 6, '3': 5, '4': 5},
    '2': {'5': -1},
    '3': {'2': -2, '5': -1},
    '4': {'3': -2, '6': -1},
    '5': {'7': 3},
    '6': {'7': 3},
    '7': {}
}
source = '1'
main(graph, source)
# 0, 1, 3, 5, 0, 4, 3

graph = {
    'A': {'B': 4, 'D': 5},
    'B': {},
    'C': {'B': -10},
    'D': {'C': 3}
}
source = 'A'
main(graph, source) 
# --> 0, -2, 8, 5

graph = {
    'A': {'B': 4, 'D': 5},
    'B': {'D': 1},
    'C': {'B': -10},
    'D': {'C': 3}
}
source = 'A'
main(graph, source) 
# --> negative cycle
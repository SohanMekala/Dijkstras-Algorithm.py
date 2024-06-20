nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

edges = {
    ('A', 'C') : 3,
    ('A', 'F') : 2,
    ('C', 'F') : 2,
    ('F', 'E') : 3,
    ('C', 'E') : 1,
    ('E', 'B') : 2,
    ('B', 'F') : 6,
    ('C', 'D') : 4,
    ('F', 'G') : 5,
    ('B', 'D') : 1,
    ('B', 'G') : 2,
}

start = 'A'
end = 'B'

'''
1. constantly update estimates
2. choose next vertex
'''

def minimum(dict):
    min_key = list(dict.keys())[0]
    for i in list(dict.keys())[1:]:
        if dict[i] < dict[min_key]:
            min_key = i
    return(min_key)

def dijkstra(nodes, edges, start, end):
    unexplored = {node : float('inf') for node in nodes}
    unexplored[start] = 0
    while len(unexplored) != 0:
        explore = minimum(unexplored)
        if explore == end:
            break
        else:
            for path in edges.items():
                if path[0][0] == explore:
                    if path[0][1] in unexplored.keys():
                        check_time = unexplored[path[0][0]] + path[1]
                        if check_time < unexplored[path[0][1]]:
                            unexplored[path[0][1]] = check_time
                elif path[0][1] == explore:
                    if path[0][0] in unexplored.keys():
                        check_time = unexplored[path[0][1]] + path[1]
                        if check_time < unexplored[path[0][0]]:
                            unexplored[path[0][0]] = check_time
            del unexplored[explore]

    return(unexplored[explore])

print(dijkstra(nodes, edges, start, end))

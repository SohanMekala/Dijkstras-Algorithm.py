nodes = ['A', 'B', 'C', 'D', 'E']

edges = {
    ('A', 'B') : 4,
    ('A', 'C') : 2,
    ('B', 'C') : 1,
    ('B', 'D') : 2,
    ('C', 'D') : 4,
    ('C', 'E') : 5,
    ('E', 'D') : 1,
}

start = 'A'
end = 'D'


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

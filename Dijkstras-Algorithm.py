nodes = nodes = ['A', 'B', 'C', 'D', 'E', 'F']

edges = {
    ('A', 'B') : 2,
    ('A', 'D') : 8,
    ('B', 'D') : 5,
    ('B', 'E') : 6,
    ('D', 'E') : 3,
    ('D', 'F') : 2,
    ('E', 'F') : 1,
    ('E', 'C') : 9,
    ('F', 'C') : 1,
}

start = 'A'
end = 'C'

'''
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

unvisited = []

shortestDist = {} #shortest dist between start and any given node
prevNode = {} #prev node, used for backtracking


for node in nodes:
    #setting all nodes to unvisted
    unvisited.append(node)

    #setting shortest dist of all nodes to infinity except the starting node, which is 0
    if node == start:
        shortestDist[node] = 0
    else:
        shortestDist[node] = float('inf')
    
    prevNode[node] = None

workingNode = start

while workingNode != end:
    neighbors = {}

    #identify neighbors and set shortest distance
    for edge in edges:
        if workingNode in edge:

            neighbor = edge[1-edge.index(workingNode)] #works bcuz there is only two elements in edge tuple

            if neighbor in unvisited:
                
                if shortestDist[workingNode]+edges[edge] < shortestDist[neighbor]:
                    shortestDist[neighbor] = shortestDist[workingNode]+edges[edge]
                    prevNode[neighbor] = workingNode

    unvisited.remove(workingNode)

    #greedy aproach to find closest node
    closestNeighborDist = float('inf')
    closestNeighbor = None

    for neighbor in unvisited:
        if shortestDist[neighbor] < closestNeighborDist:
            closestNeighbor = neighbor
            closestNeighborDist = shortestDist[neighbor]
    
    workingNode = closestNeighbor

#backtracking
path = []
node = end
while node is not None:
    path.append(node)
    node = prevNode[node]

disp = ""

for i in range(len(path)):
    if(i!=len(path)-1):
        disp+=path[i]
        disp+=" -> "
    else:
        disp+=path[i]

print("Shortest Distance from ",start," to ",end," is ",shortestDist[end])
print(disp)





    




#Graph with Dictionary in format of ['Node', Weightage]
nodes = {
         'A': [['B', 6], ['F', 3]],
         'B': [['A', 6], ['C', 3], ['D', 2]],
         'C': [['B', 3], ['D', 1], ['E', 5]],
         'D': [['B', 2], ['C', 1], ['E', 8]],
         'E': [['C', 5], ['D', 8], ['I', 5], ['J', 5]],
         'F': [['A', 3], ['G', 1], ['H', 7]],
         'G': [['F', 1], ['I', 3]],
         'H': [['F', 7], ['I', 2]],
         'I': [['G', 3], ['H', 2], ['E', 5], ['J', 3]],
         'J': [['E', 5], ['I', 3]]
        }

# Heuristics for each node
h = {
     'A' : 10,
     'B' : 8,
     'C' : 5,
     'D' : 7,
     'E' : 3,
     'F' : 6,
     'G' : 5,
     'H' : 3,
     'I' : 1,
     'J' : 0
    }

def astar(start, goal):
    opened = []                              #To store paths that are not complete i.e. Goal isn't reached
    closed = []                              #To store paths that are complete i.i. Goal is reached 
    visited = set()                          #To store nodes that are already visited
    opened.append([start, h[start]])         #Initialize start node
    while opened :                           #To check paths that are not complete
        min = 1000                           #Can be any number that is much greater than the ones in Graph to find the minimum length
        val = ''                             #To store the current traversing path
        for i in opened:                       
            if i[1] < min:                   #To find the path with the lowest weight/length
                min = i[1]
                val = i[0]
        closed.append(val)
        visited.add(val)
        if goal not in closed:
            for i in nodes[val]:
                if i[0] not in visited:
                    opened.append([i[0], (min-h[val]+i[1]+h[i[0]])])      #Adds previous weight and the current heuristics and weight of the node
        else:
            break
        opened.remove([val, min])

    closed = closed[::-1]                    
    min = 1000
    for i in opened:                         #To get the minimum weight of the paths
        if i[1] < min:
            min = i[1]
                  
    lens = len(closed)
    i = 0
    while i < lens-1:
        nei = []
        for j in nodes[closed[i]]:
            nei.append(j[0])
        if closed[i+1] not in nei:
            del closed[i+1]
            lens-=1
        i+=1
    closed = closed[::-1]
    return closed, min                       #Returns shortest path and the weight corresponding to it

# Start - 'A', Goal = 'J'
print(astar('A', 'J'))

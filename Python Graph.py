structure = {'A': ['B', 'C', 'E'], 'B':['E', 'D'], 'C':['E', 'D'], 'D':['B', 'C'], 'E': []} 

fullPath = []

def recursiveDFS (structure, nodeStart, fullPath): #Define our function with structure, nodeStart, fullPath
    
    fullPath = fullPath + [nodeStart] #Set our fullPath variable to fullPath + node start so we can navigate the structure
    print (fullPath)
    
    for node in structure[nodeStart]:
        if not node in fullPath:
            fullPath = recursiveDFS(structure, node, fullPath)
    return fullPath

print ('Recursive Depth First Search Result', recursiveDFS(structure, 'A', fullPath))

def iterativeBFS(structure, nodeStart, fullPath):
    x = [nodeStart] #x is set to the start of the node
    while x:
        print(x) #print the node
        firstNode = x.pop(0)
        if not firstNode in fullPath: #if this is not the first top node then increment the node by 1 travesring the "graph"
            fullPath = fullPath + [firstNode]
            x = x + structure[firstNode]
    return fullPath

print ('Iterative Breadth First Search Result', iterativeBFS(structure, 'A', fullPath))

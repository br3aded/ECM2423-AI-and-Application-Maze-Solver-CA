import time

def bi_directional_breadth_first_search(fileName):
    st =  time.time()
    f = open(fileName+".txt", "r")
    data = f.readlines()
    maze = []
    for x in data:
        if x.split != []:
            maze.append(x.split())
    startPosition = (maze[0].index('-'),0)
    goal = (maze[len(maze)-1].index('-'),len(maze)-1)
    bi_directional_breadth_first_search_loop(maze,[[startPosition]],[[goal]])
    et = time.time()
    print(fileName + " took " + str(et-st) + " seconds to execute" )


def bi_directional_breadth_first_search_loop(maze,queueFoward,queueBackward):#
    nodes = 1
    fowardExplored = []
    backwardExplored = []
    while True:
        pathFoward = queueFoward.pop(0)
        nodeFoward = pathFoward[-1]      
        if nodeFoward in backwardExplored:
            for i in range(len(backwardExplored)):
                #change to find the shortest path that contains nodeFoward
                #delete anything after node foward to do this and compare lists
                if nodeFoward in queueBackward[-i]:
                    reverseList = (queueBackward[-i])[::-1]
                    if len(pathFoward) > len(reverseList):
                        for i in pathFoward:
                            if i in reverseList:
                                pathFoward.remove(i)
                    else:
                        for i in reverseList:
                            if i in pathFoward:
                               reverseList.remove(i)
                    path = pathFoward + reverseList
                    for x in path:
                        if path.count(x) > 1:
                            path.remove(x)
                            print("repeated node : " + str(x))
                    print("path : " + str(path))
                    print("path length : " + str(len(path)))
                    print("nodes visited : " + str(nodes))
                    maze_visited(fowardExplored+backwardExplored,maze)
                    maze_solution(path,maze)
                    return                    
        if nodeFoward not in fowardExplored:
        #calculate all possible directions from current node
            possibleNode = []
            if maze[nodeFoward[1]][nodeFoward[0]-1] == "-":
                possibleNode.append((nodeFoward[0]-1,nodeFoward[1]))
            if maze[nodeFoward[1]][nodeFoward[0]+1] == "-":
                possibleNode.append((nodeFoward[0]+1,nodeFoward[1]))
            if maze[nodeFoward[1]-1][nodeFoward[0]] == "-":
                possibleNode.append((nodeFoward[0],nodeFoward[1]-1))    
            if maze[nodeFoward[1]+1][nodeFoward[0]] == "-":
                possibleNode.append((nodeFoward[0],nodeFoward[1]+1))
            for x in possibleNode:
                nodes += 1
                new_path = list(pathFoward)
                new_path.append(x)
                queueFoward.append(new_path)
            fowardExplored.append(nodeFoward)
        pathBackward = queueBackward.pop(0)
        nodeBackward = pathBackward[-1]
        if nodeBackward not in backwardExplored:
            possibleNode = []
            if maze[nodeBackward[1]][nodeBackward[0]-1] == "-":
                possibleNode.append((nodeBackward[0]-1,nodeBackward[1]))
            if maze[nodeBackward[1]][nodeBackward[0]+1] == "-":
                possibleNode.append((nodeBackward[0]+1,nodeBackward[1]))
            if maze[nodeBackward[1]-1][nodeBackward[0]] == "-":
                possibleNode.append((nodeBackward[0],nodeBackward[1]-1))  
            if nodeBackward[1] != (len(maze)-1):   
                if maze[nodeBackward[1]+1][nodeBackward[0]] == "-":
                    possibleNode.append((nodeBackward[0],nodeBackward[1]+1))
            for x in possibleNode:
                nodes += 1
                new_path = list(pathBackward)
                new_path.append(x)
                queueBackward.append(new_path)
            backwardExplored.append(nodeBackward)

def maze_visited(visited,maze):
    for i in range(len(visited)):
        maze[visited[i][1]][visited[i][0]] = "x"
    joinVisited = []
    for i in range(len(maze)):
        joinVisited.append(' '.join(maze[i]))
    f = open("Visited-Nodes.txt", "w")
    f.write('\n'.join(joinVisited))

def maze_solution(path,maze):
    for i in range(len(path)):
        maze[path[i][1]][path[i][0]] = "x"
    joinVisited = []
    for i in range(len(maze)):
        joinVisited.append(' '.join(maze[i]))
    f = open("maze-solution.txt", "w")
    f.write('\n'.join(joinVisited))

bi_directional_breadth_first_search("maze-Medium")
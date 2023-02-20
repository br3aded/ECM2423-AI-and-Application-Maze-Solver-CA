import time

def depth_first_search(fileName):
    st =  time.time()
    f = open(fileName+".txt", "r")
    data = f.readlines()
    maze = []
    for x in data:
        if x.split != []:
            maze.append(x.split())
    startPosition = (maze[0].index('-'),0)
    goal = (maze[len(maze)-1].index('-'),len(maze)-1)
    nodes = 1
    depth_first_search_loop(maze,startPosition,goal,[startPosition],[startPosition],nodes)
    et = time.time()
    print(fileName + " took " + str(et-st) + " seconds to execute" )

def depth_first_search_loop(maze,currentNode,goal,path,visited,nodes):
    while True:
        if currentNode == goal:
            maze_solution(path,maze) # runs function that outputs a file that shows path on the maze
            print(path)
            print("steps in path : " + str(len(path)))
            print("nodes visited : " + str(nodes))
            break

        #calculate all possible directions from current node
        possibleNode = []
        if maze[currentNode[1]][currentNode[0]-1] == "-":
            possibleNode.append((currentNode[0]-1,currentNode[1]))
        if maze[currentNode[1]-1][currentNode[0]] != "-" and maze[currentNode[1]-1][currentNode[0]] != "#":
            print(maze[currentNode[1]-1][currentNode[0]])
        if maze[currentNode[1]][currentNode[0]+1] == "-":
            possibleNode.append((currentNode[0]+1,currentNode[1]))
        if maze[currentNode[1]-1][currentNode[0]] == "-":
            possibleNode.append((currentNode[0],currentNode[1]-1))    
        if maze[currentNode[1]+1][currentNode[0]] == "-":
            possibleNode.append((currentNode[0],currentNode[1]+1))

        #check if possible directions against visted
        newNodeFound =  False
        for x in possibleNode:
            if x not in visited:
                currentNode = x
                path.append(x)
                visited.append(x)
                nodes +=1
                newNodeFound = True
                break
        
        if newNodeFound != True:
            if (path == []):
                maze_visited(visited,maze)
            path.pop()
            currentNode = path[len(path)-1]

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

depth_first_search("maze-Medium")
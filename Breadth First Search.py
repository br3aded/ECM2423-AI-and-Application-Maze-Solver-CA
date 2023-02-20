import time

def breadth_first_search(fileName):
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
    breadth_first_search_loop(maze,startPosition,goal,[[startPosition]],[],nodes)
    et = time.time()
    print(fileName + " took " + str(et-st) + " seconds to execute" )

def breadth_first_search_loop(maze,currentNode,goal,queue,explored,nodes):
    if currentNode == goal:
            maze_solution(path,maze) # runs function that outputs a file that shows path on the maze
            print(path)
            print("steps in path : " + str(len(path)))
            print("nodes visited : " + str(nodes))
    
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node not in explored:
        #calculate all possible directions from current node
            possibleNode = []
            if maze[node[1]][node[0]-1] == "-":
                possibleNode.append((node[0]-1,node[1]))
            if maze[node[1]][node[0]+1] == "-":
                possibleNode.append((node[0]+1,node[1]))
            if maze[node[1]-1][node[0]] == "-":
                possibleNode.append((node[0],node[1]-1))    
            if maze[node[1]+1][node[0]] == "-":
                possibleNode.append((node[0],node[1]+1))
            for x in possibleNode:
                if possibleNode not in explored:
                    new_path = list(path)
                    new_path.append(x)
                    queue.append(new_path)
                    if x == goal:
                        print("path : " + str(new_path))
                        print("Path Length : " + str(len(path)))
                        maze_solution(new_path,maze)
                        return
            explored.append(node)
    print("no solution")

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

breadth_first_search("maze-VLarge")
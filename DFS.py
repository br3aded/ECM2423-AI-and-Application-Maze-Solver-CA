import time

def depth_first_search(file_name):
    st =  time.time()
    f = open(file_name+".txt", "r")
    data = f.readlines()
    maze = []
    for x in data:
        if x.split != []:
            maze.append(x.split())
    start_position = (maze[0].index('-'),0)
    goal = (maze[len(maze)-1].index('-'),len(maze)-1)
    depth_first_search_loop(maze,start_position,goal,[start_position],[start_position])
    et = time.time()
    print(file_name + " took " + str(et-st) + " seconds to execute" )

def depth_first_search_loop(maze,current_node,goal,path,visited):
    nodes = 1
    while True:
        if current_node == goal:
            maze_solution(path,maze) # runs function that outputs a file that shows path on the maze
            print(path)
            print("steps in path : " + str(len(path)))
            print("nodes visited : " + str(nodes))
            break

        #calculate all possible directions from current node
        possible_node = []
        if maze[current_node[1]][current_node[0]-1] == "-":
            possible_node.append((current_node[0]-1,current_node[1]))
        if maze[current_node[1]][current_node[0]+1] == "-":
            possible_node.append((current_node[0]+1,current_node[1]))
        if maze[current_node[1]-1][current_node[0]] == "-":
            possible_node.append((current_node[0],current_node[1]-1))    
        if maze[current_node[1]+1][current_node[0]] == "-":
            possible_node.append((current_node[0],current_node[1]+1))

        #check if possible directions against visted
        new_node_found =  False
        for x in possible_node:
            if x not in visited:
                current_node = x
                path.append(x)
                visited.append(x)
                nodes +=1
                new_node_found = True
                break
        
        if new_node_found != True:
            if (path == []):
                maze_visited(visited,maze)
            path.pop()
            current_node = path[len(path)-1]

def maze_visited(visited,maze):
    for i in range(len(visited)):
        maze[visited[i][1]][visited[i][0]] = "x"
    join_visited = []
    for i in range(len(maze)):
        join_visited.append(' '.join(maze[i]))
    f = open("Visited-Nodes.txt", "w")
    f.write('\n'.join(join_visited))

def maze_solution(path,maze):
    for i in range(len(path)):
        maze[path[i][1]][path[i][0]] = "x"
    join_visited = []
    for i in range(len(maze)):
        join_visited.append(' '.join(maze[i]))
    f = open("maze-solution.txt", "w")
    f.write('\n'.join(join_visited))

depth_first_search("maze-Medium")
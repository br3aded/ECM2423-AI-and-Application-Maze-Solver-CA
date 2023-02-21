import time

def depth_first_search(file_name):
    st =  time.time() #stores the time when the search starts
    f = open(file_name+".txt", "r") #opens maze file 
    data = f.readlines() #splits the maze file lines into individual elements
    maze = []
    for x in data: #splits each line into individual elements in the maze (# , -)
        if x.split != []:
            maze.append(x.split())
    start_position = (maze[0].index('-'),0) # finds the start position of the maze
    goal = (maze[len(maze)-1].index('-'),len(maze)-1) # finds the end position of the maze
    depth_first_search_loop(maze,start_position,goal,[start_position],[start_position])  # calls the loop for the dfs giving it the maze , start position , goal, a path with start position already in and a list of nodes which have been visited
    et = time.time() #stores the end time of the search
    print(file_name + " took " + str(et-st) + " seconds to execute" ) #calculates total time for search to complete and outputs

def depth_first_search_loop(maze,current_node,goal,path,visited):
    while True:
        if current_node == goal:#checks to see if the current node is the goal
            maze_solution(path,maze) # runs function that outputs a file that shows the path on the maze
            print(path) # outputs path coordiantes into the terminal
            print("steps in path : " + str(len(path))) # outputs length of path into terminal
            print("nodes visited : " + str(len(visited))) # outputs number of nodes visited into the terminal
            return # ends search

        #calculate all possible directions from current node and stores in possible_node
        possible_node = []
        if maze[current_node[1]][current_node[0]-1] == "-":
            possible_node.append((current_node[0]-1,current_node[1]))
        if maze[current_node[1]][current_node[0]+1] == "-":
            possible_node.append((current_node[0]+1,current_node[1]))
        if maze[current_node[1]-1][current_node[0]] == "-":
            possible_node.append((current_node[0],current_node[1]-1))    
        if maze[current_node[1]+1][current_node[0]] == "-":
            possible_node.append((current_node[0],current_node[1]+1))

        
        new_node_found =  False
        for x in possible_node: # checks against each node in possible_node
            if x not in visited: # checks if node hasn't been visited
                current_node = x # sets node to current node
                path.append(x) # adds node to the path
                visited.append(x) # adds node to visited
                new_node_found = True # used to check if a unvisited node has been found
                break # ends loop after a new node has been found
        
        if new_node_found != True: # this section of code runs if a new node hasn't been found from current node 
            path.pop() # removes most recent node from the path
            current_node = path[len(path)-1] #sets current node as last node in path so the search can backtrack

#this is an extra function that outputs the path onto the maze-solution.txt text file
def maze_visited(visited,maze):
    for i in range(len(visited)):
        maze[visited[i][1]][visited[i][0]] = "x"
    join_visited = []
    for i in range(len(maze)):
        join_visited.append(' '.join(maze[i]))
    f = open("Visited-Nodes.txt", "w")
    f.write('\n'.join(join_visited))

#this is an extra function that outputs all the nodes visited onto the Visted-Nodes.txt text file
def maze_solution(path,maze):
    for i in range(len(path)):
        maze[path[i][1]][path[i][0]] = "x"
    join_visited = []
    for i in range(len(maze)):
        join_visited.append(' '.join(maze[i]))
    f = open("maze-solution.txt", "w")
    f.write('\n'.join(join_visited))

#add the maze file name here to carry out the search
depth_first_search("maze-Medium")
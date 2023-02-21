import time

def breadth_first_search(file_name):
    st =  time.time() #stores the time when the search starts
    f = open(file_name+".txt", "r") #opens maze file 
    data = f.readlines() #splits the maze file lines into individual elements
    maze = []
    for x in data: #splits each line into individual elements in the maze (# , -)
        if x.split != []:
            maze.append(x.split())
    start_position = (maze[0].index('-'),0) # finds the start position of the maze
    goal = (maze[len(maze)-1].index('-'),len(maze)-1) # finds the end position of the maze
    breadth_first_search_loop(maze,[[start_position]],[[goal]]) # runs the breadth first search by passing the maze array , a foward search queue with the start position already in and a backward search queue with the end position already in
    et = time.time()  #stores the end time of the search
    print(file_name + " took " + str(et-st) + " seconds to execute" ) #calculates total time for search to complete and outputs


def breadth_first_search_loop(maze,queue_foward,queue_backward):
    foward_explored = [] # creates variable foward_explored as an empty array (used to keep track of all nodes explored in the forward BFS)
    backward_explored = [] # creates variable backward_explored as an empty array (used to keep track of all nodes explored in the backward BFS)
    while True: #while loop to run until a path is found
        path_foward = queue_foward.pop(0) # removes the path at the top of the queue to be explored
        node_foward = path_foward[-1] # gets the last node in the path which is where we will check for new paths      
        if node_foward in backward_explored: # condition to check if the backward BFS has explored the foward node
            for i in range(len(backward_explored)): # used to check each possible path in the backward search for the node_foward
                if node_foward in queue_backward[-i]: #checks if foward_node is in each path in queue_backward (starts from the back as this is where it is most likely to be and helps reduce time of the program)
                    reverse_list = (queue_backward[-i])[::-1] # reverse the list that contains foward_node
                    path = path_foward + reverse_list # concatinates the foward and backward path together
                    for x in path: #removes any duplicate nodes from the path
                        if path.count(x) > 1:
                            path.remove(x)
                    print("path : " + str(path)) #outputs the path coordinates to the terminal
                    print("path length : " + str(len(path))) #outputs the length of the path to the terminal
                    print("nodes visited : " + str(len(foward_explored+backward_explored))) #outputs the number of explored nodes into the terminal
                    maze_visited(foward_explored+backward_explored,maze) #runs a function that outputs the explored nodes onto a text file of the map
                    maze_solution(path,maze) #runs a function that outputs the path onto the text file of the map
                    return # ends the search                   
        if node_foward not in foward_explored: #checks to see if the node_foward has already been explored
            #calculate all possible directions from current node and stores in possible_node
            possible_node = []
            if maze[node_foward[1]][node_foward[0]-1] == "-":
                possible_node.append((node_foward[0]-1,node_foward[1]))
            if maze[node_foward[1]][node_foward[0]+1] == "-":
                possible_node.append((node_foward[0]+1,node_foward[1]))
            if maze[node_foward[1]-1][node_foward[0]] == "-":
                possible_node.append((node_foward[0],node_foward[1]-1))    
            if maze[node_foward[1]+1][node_foward[0]] == "-":
                possible_node.append((node_foward[0],node_foward[1]+1))
            for x in possible_node: #for each possible node we create a new path and add to the back of the queue
                new_path = list(path_foward) #creates a new path that consists of path_foward and possible node added to the end
                new_path.append(x) #adds possible_node to the new_path
                queue_foward.append(new_path) #adds new_path to the queue
            foward_explored.append(node_foward) #adds node_forward to foward_explored

        #this is exactly the same functionality just going backward from the goal
        path_backward = queue_backward.pop(0)
        node_backward = path_backward[-1]
        if node_backward not in backward_explored:
            possible_node = []
            if maze[node_backward[1]][node_backward[0]-1] == "-":
                possible_node.append((node_backward[0]-1,node_backward[1]))
            if maze[node_backward[1]][node_backward[0]+1] == "-":
                possible_node.append((node_backward[0]+1,node_backward[1]))
            if maze[node_backward[1]-1][node_backward[0]] == "-":
                possible_node.append((node_backward[0],node_backward[1]-1))  
            if node_backward[1] != (len(maze)-1):   
                if maze[node_backward[1]+1][node_backward[0]] == "-":
                    possible_node.append((node_backward[0],node_backward[1]+1))
            for x in possible_node:
                new_path = list(path_backward)
                new_path.append(x)
                queue_backward.append(new_path)
            backward_explored.append(node_backward)

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
breadth_first_search("maze-Large")
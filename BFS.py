import time

def breadth_first_search(file_name):
    st =  time.time()
    f = open(file_name+".txt", "r")
    data = f.readlines()
    maze = []
    for x in data:
        if x.split != []:
            maze.append(x.split())
    start_position = (maze[0].index('-'),0)
    goal = (maze[len(maze)-1].index('-'),len(maze)-1)
    breadth_first_search_loop(maze,[[start_position]],[[goal]])
    et = time.time()
    print(file_name + " took " + str(et-st) + " seconds to execute" )


def breadth_first_search_loop(maze,queue_foward,queue_backward):
    nodes = 1
    foward_explored = []
    backward_explored = []
    while True:
        path_foward = queue_foward.pop(0)
        node_foward = path_foward[-1]      
        if node_foward in backward_explored:
            for i in range(len(backward_explored)):
                if node_foward in queue_backward[-i]:
                    reverse_list = (queue_backward[-i])[::-1]
                    if len(path_foward) > len(reverse_list):
                        for i in path_foward:
                            if i in reverse_list:
                                path_foward.remove(i)
                    else:
                        for i in reverse_list:
                            if i in path_foward:
                               reverse_list.remove(i)
                    path = path_foward + reverse_list
                    for x in path:
                        if path.count(x) > 1:
                            path.remove(x)
                            print("repeated node : " + str(x))
                    print("path : " + str(path))
                    print("path length : " + str(len(path)))
                    print("nodes visited : " + str(nodes))
                    maze_visited(foward_explored+backward_explored,maze)
                    maze_solution(path,maze)
                    return                    
        if node_foward not in foward_explored:
        #calculate all possible directions from current node
            possible_node = []
            if maze[node_foward[1]][node_foward[0]-1] == "-":
                possible_node.append((node_foward[0]-1,node_foward[1]))
            if maze[node_foward[1]][node_foward[0]+1] == "-":
                possible_node.append((node_foward[0]+1,node_foward[1]))
            if maze[node_foward[1]-1][node_foward[0]] == "-":
                possible_node.append((node_foward[0],node_foward[1]-1))    
            if maze[node_foward[1]+1][node_foward[0]] == "-":
                possible_node.append((node_foward[0],node_foward[1]+1))
            for x in possible_node:
                nodes += 1
                new_path = list(path_foward)
                new_path.append(x)
                queue_foward.append(new_path)
            foward_explored.append(node_foward)
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
                nodes += 1
                new_path = list(path_backward)
                new_path.append(x)
                queue_backward.append(new_path)
            backward_explored.append(node_backward)

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

breadth_first_search("maze-Medium")
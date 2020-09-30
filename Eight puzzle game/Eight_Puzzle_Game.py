import numpy as np
import copy

''' User inputs the initial state and displaying the initial and goal states. Also initializing all the variables used in
    various parts of the code '''
count = 0
mk = 1

i_state = list(map(int, input("Enter the initial state you want for the puzzle, seperated by space").split()))
init_state = np.array(i_state).reshape(3, 3)
print("The initial state is: \n", init_state)

goal_state = np.array([[1, 2, 3],
                       [4, 5, 6],
                       [7, 8, 0]])
print("The goal state is: \n", np.array(goal_state).reshape(3, 3))

parent_node = []
all_nodes = []
list.append(all_nodes, init_state)
list.append(parent_node, 0)
left = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
right = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
up = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
down = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
p = 0


# Check if the puzzle is solvable
def check_if_solvable(puz):
    puzzle = []
    c = 0
    for i in range(3):
        for j in range(3):
            if not (puz[i][j] == 0):
                puzzle.append(puz[i][j])
    for i in range(7):
        while (j <= 7):
            if (puzzle[i] > puzzle[j]).all():
                c = c + 1
            j += 1
    return c


def check():
    global mk
    check = check_if_solvable(init_state)
    if (check % 2):
        print("This is not solvable")
        return 0
    else:
        if(mk == 1):
            print("This is solvable")
            mk = 0
        return 1


# Search for the blank space/zero location in the matrix
def pos_of_zero(pos0):
    pos0 = np.argwhere(pos0 == 0)
    i = pos0[0][0]
    j = pos0[0][1]
    # print(" The position of 0 in the initial state of the puzzle is ", i,j)
    return i, j


# Function to move the blank space/zero by one space right
def swap_right(state, row, col):
    init_state_copy = copy.copy(state)
    if (col != 2):
        temp = init_state_copy[row][col]
        init_state_copy[row][col] = init_state_copy[row][col + 1]
        init_state_copy[row][col + 1] = temp
        return init_state_copy
    else:
        return state


# Function to move the blank space/zero by one space left
def swap_left(state, row, col):
    init_state_copy = copy.copy(state)
    if (col != 0):
        temp = init_state_copy[row][col]
        init_state_copy[row][col] = init_state_copy[row][col - 1]
        init_state_copy[row][col - 1] = temp
        return init_state_copy
    else:
        return state


# Function to move the blank space/zero by one space up
def swap_up(state, row, col):
    init_state_copy = copy.copy(state)
    if (row != 0):
        temp = init_state_copy[row][col]
        init_state_copy[row][col] = init_state_copy[row - 1][col]
        init_state_copy[row - 1][col] = temp
        return init_state_copy
    else:
        return state


# Function to move the blank space/zero by one space down
def swap_down(state, row, col):
    init_state_copy = copy.copy(state)
    if (row != 2):
        temp = init_state_copy[row][col]
        init_state_copy[row][col] = init_state_copy[row + 1][col]
        init_state_copy[row + 1][col] = temp
        return init_state_copy
    else:
        return state


# Function to call all the above functions to make the necessary movements
def movements(new_node):
    global count
    count += 1

    sol = check()
    if (sol == True):
        a, b = pos_of_zero(new_node)
        # print(a,b)

        left = swap_left(new_node, a, b)
        # print(left)
        unique_append(left)

        up = swap_up(new_node, a, b)
        # print(up)
        unique_append(up)

        right = swap_right(new_node, a, b)
        # print(right)
        unique_append(right)

        down = swap_down(new_node, a, b)
        # print(down)
        unique_append(down)

    return left, up, right, down


# Function to check if the new nodes are unique and append them to the all nodes array
def unique_append(current_node):
    global all_nodes
    global p
    global delete
    # print("Yes")
    uni = True
    for mat in all_nodes:
        if np.array_equal(mat, current_node):
            uni = False
    if (uni == True):
        list.append(parent_node, count)
        list.append(all_nodes, current_node)


# Code snippet to solve the puzzle and obtain the goal state
n = 0
while (not ((right == goal_state).all() or (left == goal_state).all() or (up == goal_state).all() or (
        down == goal_state).all())):
    left, up, right, down = movements(all_nodes[n])
    n = n + 1

# Code Snippet for backtracking the obtained goal state to determine the path
size = len(all_nodes)
gs_i = size - 1
is_i = 0
path = []

path.append(gs_i + 1)

while (gs_i != is_i):
    path.append(parent_node[gs_i])
    gs_i = (parent_node[gs_i] - 1)

path.sort()

# Code snippet to find the element in the path
path_print = path.copy()
visited_nodes = []
i = 0
for ele in path:
    path_print[i] = path[i] - 1
    i = i + 1

print(path)

for element in path_print:
    visited_nodes.append(all_nodes[element])

# Write all the details in the respective text files
Nodes_txt = open("Nodes.txt", "w+")
for Nodes in all_nodes:
    for r in range(3):
        for c in range(3):
            Nodes_txt.write(str(Nodes[c][r]))
            Nodes_txt.write(" ")
    Nodes_txt.write("\n")
Nodes_txt.close()

# Write all the combinations in the shortest path
nodes_path = open("nodePath.txt", "w+")
for np in visited_nodes:
    for r in range(3):
        for c in range(3):
            nodes_path.write(str(np[c][r]))
            nodes_path.write(" ")
    nodes_path.write("\n")
nodes_path.close()

# Write all the elements and their corresponding parent nodes
nodes_info = open("NodesInfo.txt", "w+")
start = 1
for iterate in parent_node:
    nodes_info.write(str(start))
    nodes_info.write(" ")
    nodes_info.write(str(iterate))
    nodes_info.write("\n")
    start += 1
nodes_info.close()
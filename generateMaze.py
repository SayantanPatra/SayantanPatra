import maze
import random

# Create maze using Pre-Order DFS maze creation algorithm
def createDfs(m):
    # TODO: Implement create_dfs
    stack = []
    # choose a cell index at random from the grid to be current cell
    current_cell = random.randint(0, m.total_cells - 1)
    # set visited cells to 1
    visited_cells = 1

    while visited_cells < m.total_cells:
    	# get unvisited neighbors using cell_neighbors
    	unvisited_neighbors = m.cell_neighbors(current_cell)
    	# if at least one neighbor
    	if len(unvisited_neighbors) >= 1:
    		# choose random neighbor to be new cell
    		new_cell_index = random.randint(0, len(unvisited_neighbors) - 1)
    		new_cell, compass_index = unvisited_neighbors[new_cell_index]
    		# knock down wall between it and current cell using connect_cells
    		m.connect_cells(current_cell, new_cell, compass_index)
            # push current cell to stack
    		stack.append(current_cell)
    		# set current cell to new cell
    		current_cell = new_cell
    		# add 1 to visited cells
    		visited_cells +=1
    	else:
    		# pop from stack to current cell
    		current_cell = stack.pop()
    	# call refresh_maze_view to update visualization
    	m.refresh_maze_view()
    m.state = "solve"
#            print(m.x_y(current_cell), m.x_y(new_cell), compass_index)




    """
create a stack for backtracking
choose a cell index at random from the grid to be current cell
set visited cells to 1
while visited cells < total cells
    get unvisited neighbors using cell_neighbors
    if at least one neighbor
        choose random neighbor to be new cell
        knock down wall between it and current cell using connect_cells
        push current cell to stack
        set current cell to new cell
        add 1 to visited cells
    else
        pop from stack to current cell
    call refresh_maze_view to update visualization
set state to 'solve'"""


    
def main():
    currentMaze = maze.Maze('create')
    createDfs(currentMaze)
    while 1:
        maze.check_for_exit()
    return

if __name__ == '__main__':
    main()
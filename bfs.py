from queue import Queue

class BFS:
    def __init__(self, graph, start,goal):
        self.graph = graph
        self.start = start
        self.goal = goal
        n = len(self.graph)
        m = len(self.graph[0])
        self.visited = [[False for j in range(m)] for i in range(n)]
        self.queue = Queue()
        self.path = []

    # Function to reconstruct the path from the start cell to the destination cell
    # using the parent dictionary
    def reconstructPath(self, parent, start, goal):
        # create a list to store the path
        path = []
        # start at the goal and work backwards
        current = goal
        while current != start:
            path.append(current)
            current = parent[current]
        # add the start cell to the front of the path
        path.append(start)
        # reverse the path to get the correct order
        path.reverse()
        return path

    # Function to check if a cell (x, y) is valid
    # i.e., it is within the grid and has not been visited yet
    def __is_valid(self, x, y, n, m, visited):
        return x >= 0 and x < n and y >= 0 and y < m and not visited[x][y]

    # Function to get the path from the start cell to the destination cell
    # using BFS
    def get_path(self, graph,start, goal):
        sx, sy = start
        ex, ey = goal
        n = len(graph)
        m = len(graph[0])
        # Initialize the visited array
        visited = [[False for j in range(m)] for i in range(n)]

        # Dictionary to store the parent of each cell
        parent = {(sx,sy): None}

        # Queue to store the cells to be explored
        queue = Queue()

        # Add the starting cell to the queue and mark it as visited
        queue.put((sx, sy))
        visited[sx][sy] = True

        # Array to store the path from the start cell to the destination cell
        path = []

        # Explore the cells in the queue until it becomes empty
        while not queue.empty():
            # Remove the first cell from the queue
            x, y = queue.get()

            # If the current cell is the destination cell, return the path
            if x == ex and y == ey:
                return path

            # For each of the four possible moves , do the following:
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                # Calculate the destination cell
                nx, ny = x + dx, y + dy

                # If the destination cell is valid, mark it as visited and add it to the queue
                if self.__is_valid(nx, ny, n, m, visited) and graph[nx][ny] != '#' :
                    queue.put((nx, ny))
                    visited[nx][ny] = True
                    parent[(nx, ny)] = (x,y)

                    # Add the destination cell to the path
                    path.append((nx, ny))
                    # If the destination cell is reached, return the path and the reconstructed short path
                    if nx == ex and ny == ey:
                        return path,self.reconstructPath(parent, (sx, sy), (ex, ey))
        # Return an empty list if the destination cell could not be reached
        return [],[]

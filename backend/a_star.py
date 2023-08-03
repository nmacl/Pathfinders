import math
from queue import PriorityQueue

def heuristic(node1, node2):
    # Assuming node1 and node2 are tuples of (x, y) coordinates
    dx = node1[0] - node2[0]
    dy = node1[1] - node2[1]
    return math.sqrt(dx * dx + dy * dy)

def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.insert(0, current)
    return path

def a_star(G, start, goal):
    # Get coordinates of nodes
    start_coords = (G.nodes[start]['x'], G.nodes[start]['y'])
    goal_coords = (G.nodes[goal]['x'], G.nodes[goal]['y'])

    open_set = PriorityQueue()
    open_set.put((0, start))
    came_from = {}
    g_score = {node: float("inf") for node in G.nodes()}
    f_score = {node: float("inf") for node in G.nodes()}

    g_score[start] = 0
    f_score[start] = heuristic(start_coords, goal_coords)

    while not open_set.empty():
        current = open_set.get()[1]

        if current == goal:
            return reconstruct_path(came_from, current)

        for neighbor in G.neighbors(current):
            # Use get_edge_data to get the distance between current and neighbor
            tentative_g_score = g_score[current] + G.get_edge_data(current, neighbor).get('length', 1)
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                neighbor_coords = (G.nodes[neighbor]['x'], G.nodes[neighbor]['y'])
                f_score[neighbor] = g_score[neighbor] + heuristic(neighbor_coords, goal_coords)
                open_set.put((f_score[neighbor], neighbor))

    return None

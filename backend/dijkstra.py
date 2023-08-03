def dijkstra(G, start, goal):
    dist = {node: float('inf') for node in G.nodes}
    prev = {node: None for node in G.nodes}
    unvisited_set = set(G.nodes)

    dist[start] = 0

    while unvisited_set:
        # Node with the smallest distance will be chosen first
        current = min(unvisited_set, key=lambda node: dist[node])

        if current == goal:
            path = []
            while current is not None:
                path.insert(0, current)
                current = prev[current]
            return path

        unvisited_set.remove(current)

        for neighbor in G.neighbors(current):
            if G.has_edge(current, neighbor):
                alt = dist[current] + min(data['length'] for data in G.get_edge_data(current, neighbor).values())
                if alt < dist[neighbor]:
                    dist[neighbor] = alt
                    prev[neighbor] = current
            else:
                continue  # Skip to the next neighbor if there's no edge to the current neighbor

    # No path was found
    return None

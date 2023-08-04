import os
import osmnx as ox
from flask import Flask, request, jsonify
from time import time
from networkx import NetworkXNoPath
from dijkstra import dijkstra 
from a_star import a_star  
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
def calculate_path_length(G, path):
    return sum(G.edges[path[i], path[i + 1], 0]['length'] for i in range(len(path) - 1))

def nodes_to_coords(G, path):
    return [[G.nodes[node]['y'], G.nodes[node]['x']] for node in path]

# Check if the graph has been saved to disk
if not os.path.isfile('graph.graphml'):
    # If not, download it and save it to disk
    G = ox.graph_from_place('Gainesville, Florida, USA', network_type='drive')
    ox.save_graphml(G, 'graph.graphml')
else:
    # If it has, load it from disk
    G = ox.load_graphml('graph.graphml')

@app.route('/shortest_path/dijkstra', methods=['POST'])
def shortest_path_dijkstra():
    data = request.get_json()
    start_address = data['start']
    end_address = data['end']

    try:
        start_coords = ox.geocode(start_address)
        end_coords = ox.geocode(end_address)
    except ox._errors.InsufficientResponseError:
        return jsonify({'error': 'Could not geocode the provided addresses.'}), 400

    start_node = ox.distance.nearest_nodes(G, start_coords[1], start_coords[0])
    end_node = ox.distance.nearest_nodes(G, end_coords[1], end_coords[0])

    try:
        time_start = time()
        shortest_path_nodes = dijkstra(G, start_node, end_node)  
        if shortest_path_nodes is None:
            raise NetworkXNoPath
        execution_time = time() - time_start
    except NetworkXNoPath:
        return jsonify({'error': 'No path found between start and end addresses.'}), 400

    shortest_path_coords = nodes_to_coords(G, shortest_path_nodes)
    path_length = calculate_path_length(G, shortest_path_nodes)

    return jsonify({'path': shortest_path_coords, 'executionTime': execution_time, 'pathLength': path_length})

@app.route('/shortest_path/a_star', methods=['POST'])
def shortest_path_a_star():
    data = request.get_json()
    start_address = data['start']
    end_address = data['end']

    try:
        start_coords = ox.geocode(start_address)
        end_coords = ox.geocode(end_address)
    except ox._errors.InsufficientResponseError:
        return jsonify({'error': 'Could not geocode the provided addresses.'}), 400

    start_node = ox.distance.nearest_nodes(G, start_coords[1], start_coords[0])
    end_node = ox.distance.nearest_nodes(G, end_coords[1], end_coords[0])

    try:
        time_start = time()
        shortest_path_nodes = a_star(G, start_node, end_node) 
        if shortest_path_nodes is None:
            raise NetworkXNoPath
        execution_time = time() - time_start
    except NetworkXNoPath:
        return jsonify({'error': 'No path found between start and end addresses.'}), 400

    shortest_path_coords = nodes_to_coords(G, shortest_path_nodes)
    path_length = calculate_path_length(G, shortest_path_nodes)

    return jsonify({'path': shortest_path_coords, 'executionTime': execution_time, 'pathLength': path_length})

if __name__ == '__main__':
    app.run(port=3001)

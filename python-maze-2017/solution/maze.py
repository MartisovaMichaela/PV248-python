#!/usr/bin/env python3

"""
Tomas Meszaros - 422336
"""

import flask
import dijkstar

from pprint import pprint as pp

maze = flask.Flask(__name__)

@maze.route('/', methods = ['GET', 'POST'])
def handle():
    if flask.request.method == 'GET':
        return flask.Response(status=200)

    if flask.request.method == 'POST':
        maze_data = flask.request.get_json()
        corridors = maze_data['corridors']
        end = maze_data['end']
        rooms = maze_data['rooms']
        start = maze_data['start']
        pp(maze_data)

        graph = dijkstar.Graph()
        for edge in corridors:
            graph.add_edge(edge[0], edge[1], {'cost': 1})
            graph.add_edge(edge[1], edge[0], {'cost': 1})
        cost_fun = lambda u, v, e, prev_e: e['cost']

        # Invalid input
        flat_corridors = [i[0] for i in corridors] + [i[1] for i in corridors]
        if start not in rooms or end not in rooms or \
           (len(flat_corridors) == 0 and len(rooms) == 2):
            return flask.jsonify({"solution": None, "length": None,
                                  "error": "Invalid input"}), 200

        # Path does not exist
        try:
            solution = dijkstar.find_path(graph, start, end, cost_func=cost_fun)
        except dijkstar.algorithm.NoPathError:
            return flask.jsonify({"solution": None, "length": None,
                                  "status": "No solution found"}), 200

        # Correct solution
        return flask.jsonify({"solution": solution.nodes,
                              "length": len(solution.nodes),
                              "status": "OK"}), 200
if __name__ == "__main__":
    maze.run(host='localhost', port=5000)

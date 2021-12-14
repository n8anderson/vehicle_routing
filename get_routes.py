import math
from typing import List
from classes import Node, Vehicle


def generate_grid():
    route_map = []
    for i in range(10):
        route_map.append(['_', '_', '_', '_', '_', '_', '_', '_', '_', '_'])

    return route_map


def populate_map():

    location = (4, 4)
    depot = Node(0, location, 0, True)

    route_map = generate_grid()

    route_map[depot.location[0]][depot.location[1]] = depot

    list_of_locs = [[1, 2], [2, 3], [1, 4], [2, 5], [2, 6],
                    [6, 2], [8, 1], [8, 3], [7, 4], [6, 6]]

    list_of_vals = [8, 3, 2, 9, 7, 2, 4, 10, 6, 7]
    nodes = []
    count = 0
    for i in range(len(list_of_vals)):
        count += 1
        temp_node = Node(count, (list_of_locs[i][0], list_of_locs[i][1]), list_of_vals[i])
        if count > 5:
            temp_node.vehicle_id = 1
        nodes.append(temp_node)

    for node in nodes:
        node.__toString__()
        route_map[node.location[1]][node.location[0]] = node

    return route_map, list_of_locs

def print_route_map(route_map: List[List]):
    for i in route_map:
        for c in i:
            if type(c) == Node:
                if c.is_depot:
                    print('D', end=" ")
                else:
                    print('N', end=" ")
            else:
                print(c, end=" ")
        print()

def run_vehicle():
    stops, locs = populate_map()

    print_route_map(stops)
    depot = stops[4][4]
    depot_loc = depot.location

    vehicle1 = Vehicle(depot_loc, 0)
    vehicle2 = Vehicle(depot_loc, 1)

    vehicle1_route = []
    vehicle2_route = []

    for loc in locs:
        if stops[loc[1]][loc[0]].vehicle_id == 0:
            vehicle1_route.append(stops[loc[1]][loc[0]])
        else:
            vehicle2_route.append(stops[loc[1]][loc[0]])

    calc_first_node(vehicle1, vehicle1_route)

def calc_first_node(vehicle: Vehicle, v_nodes: List):
    v_pos = vehicle.current_pos
    dis_to_val = 0
    saved_dist = 0
    saved_node = None

    for node in v_nodes:
        delta_y = v_pos[0] - node.location[0]
        delta_x = v_pos[1] - node.location[1]

        distance = math.sqrt(delta_x ** 2 + delta_y ** 2)

        temp_val = node.value / distance
        if temp_val > dis_to_val:
            saved_dist = distance
            dis_to_val = temp_val
            saved_node = node

    print(saved_node.node_id, saved_node.value, saved_dist)

run_vehicle()


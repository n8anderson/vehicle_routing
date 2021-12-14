import math
import sys
from typing import List
from classes import Node, Vehicle
import gui
import random as r


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

    list_of_locs = []
    while len(list_of_locs) < 10:
        temp_loc = [r.randint(0, 9), r.randint(0, 9)]
        if temp_loc[0] != 4 and temp_loc[1] != 4 and temp_loc not in list_of_locs:
            list_of_locs.append(temp_loc)

    print(list_of_locs)


    list_of_vals = []
    while len(list_of_vals) < 10:
        list_of_vals.append(r.randint(10, 50))

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
        route_map[node.location[0]][node.location[1]] = node

    return route_map, list_of_locs


def print_route_map(route_map: List[List]):
    formatted_string = ""
    for i in range(len(route_map)):
        for c in range(len(route_map[i])):
            if type(route_map[c][i]) == Node:
                if route_map[c][i].is_depot:
                    formatted_string += 'D\t'
                else:
                    formatted_string += 'N\t'
            elif route_map[c][i] == 'V0' or route_map[c][i] == 'V1':
                formatted_string += f"{route_map[c][i]}\t"
            else:
                formatted_string += "_\t"
        formatted_string += '\n'

    return formatted_string


def run_vehicle(window: gui.StandardWindow):
    stops, locs = populate_map()

    print_route_map(stops)
    depot = stops[4][4]
    depot_loc = depot.location

    vehicle1 = Vehicle(depot_loc, 0)
    vehicle2 = Vehicle(depot_loc, 1)

    vehicle1_route = []
    vehicle2_route = []

    for loc in locs:
        if stops[loc[0]][loc[1]].vehicle_id == 0:
            vehicle1_route.append(stops[loc[0]][loc[1]])
        else:
            vehicle2_route.append(stops[loc[0]][loc[1]])

    # vehicle2.move_to_node(calc_first_node(vehicle2, vehicle2_route))

    vehicle1 = calc_subs_nodes(vehicle1, vehicle1_route, depot, window, stops)
    vehicle2 = calc_subs_nodes(vehicle2, vehicle2_route, depot, window, stops)

    totals = f"Vehicle 1 Info:\tDistance: {vehicle1.distance_traveled}\tValue: {vehicle1.total_revenue}\nVehicle 2 Info:\tDistance: {vehicle2.distance_traveled}\tValue: {vehicle2.total_revenue}\n"
    window.totals_display.setText(totals)


def calc_subs_nodes(vehicle: Vehicle, v_nodes: List, depot: Node, window: gui.StandardWindow, stops):
    display_route = print_route_map(stops)
    window.route_display.setText(display_route)
    #print(display_route)
    if vehicle.vehicle_ID == 1:
        window.print_text += "\n--------------------------------VEHICLE 2--------------------------------"
    window.print_text += ("\n" + vehicle.__toString__())
    vehicle.move_to_node(calc_first_node(vehicle, v_nodes))
    if vehicle.vehicle_ID == 0:
        stops[vehicle.nodes_visited[0].location[0]][vehicle.nodes_visited[0].location[1]] = 'V0'
    else:
        stops[vehicle.nodes_visited[0].location[0]][vehicle.nodes_visited[0].location[1]] = 'V1'
    final_node = None
    count = 0
    while len(vehicle.nodes_visited) < len(v_nodes):
        display_route = print_route_map(stops)
        window.route_display.setText(display_route)
        window.print_text += ("\n" + vehicle.__toString__())
        window.display.setText(window.print_text)
        v_pos = vehicle.current_pos
        shortest_distance = sys.maxsize
        saved_node = None
        for node in v_nodes:
            if node not in vehicle.nodes_visited:
                print("COUNT #", count)

                delta_y = v_pos[1] - node.location[1]
                delta_x = v_pos[0] - node.location[0]
                distance = math.sqrt((delta_x ** 2) + (delta_y ** 2))
                print("Current Pos", v_pos, "Node Pos", node.location, "Distance", distance)
                if distance < shortest_distance:
                    shortest_distance = distance
                    saved_node = node
                print("SHORTEST DISt", shortest_distance)
        count += 1
        print()
        window.handleStart()
        vehicle.move_to_node(saved_node)
        if vehicle.vehicle_ID == 0:
            stops[saved_node.location[0]][saved_node.location[1]] = 'V0'
        else:
            stops[saved_node.location[0]][saved_node.location[1]] = 'V1'
        final_node = saved_node
        # window.print_text += ("\n" + vehicle.__toString__())

    if vehicle.vehicle_ID == 0:
        stops[final_node.location[0]][final_node.location[1]] = 'V0'
    else:
        stops[final_node.location[0]][final_node.location[1]] = 'V1'
    display_route = print_route_map(stops)
    window.route_display.setText(display_route)
    window.print_text += ("\n" + vehicle.__toString__())
    window.display.setText(window.print_text)
    vehicle.move_to_node(depot)
    window.print_text += ("\nFinal Total: " + vehicle.__toString__())


    return vehicle


def check_press():
    return True


def calc_first_node(vehicle: Vehicle, v_nodes: List):
    v_pos = vehicle.current_pos
    dis_to_val = 0
    saved_node = None

    for node in v_nodes:
        delta_x = v_pos[0] - node.location[0]
        delta_y = v_pos[1] - node.location[1]

        distance = math.sqrt((delta_x ** 2) + (delta_y ** 2))

        temp_val = node.value / distance
        if temp_val > dis_to_val:
            dis_to_val = temp_val
            saved_node = node

    return saved_node

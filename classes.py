import math
from typing import List


class Node:
    def __init__(self, nodeID, location=(0, 0), value=0, depot=False):
        self.node_id = nodeID
        self.location = location
        self.value = value
        self.is_depot = depot
        self.vehicle_id = 0

    def __toString__(self):
        print("NodeID:", self.node_id, "\tLocation:", self.location, "\tValue:", self.value, "\tDepot:",
              self.is_depot, "\tVehicleID:", self.vehicle_id)

class Vehicle:
    def __init__(self, depot_pos, v_id=0):
        self.current_pos = depot_pos
        self.vehicle_ID = v_id
        self.total_revenue = 0
        self.distance_traveled = 0
        self.nodes_visited: List[Node] = []

    def move_to_node(self, node: Node):
        delta_y = self.current_pos[1] - node.location[1]
        delta_x = self.current_pos[0] - node.location[0]

        distance = math.sqrt((delta_x**2) + (delta_y**2))

        self.current_pos = [node.location[0], node.location[1]]
        self.distance_traveled += distance
        self.total_revenue += node.value
        self.nodes_visited.append(node)

        #self.__toString__()

    def __toString__(self):
        ids = []
        for node in self.nodes_visited:
            ids.append(node.node_id)

        toString = f"VehicleID: {self.vehicle_ID} \tCurrent Postion: {self.current_pos} \tTotal Revenue: {self.total_revenue} \tDistance Traveled {self.distance_traveled} \tNodes Visited: {ids}"

        return toString

    def print_pos(self):
        print("Vehicle ID:", self.vehicle_ID, "Vehicle Position:", self.current_pos)


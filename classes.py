from typing import List


class Vehicle:
    def __init__(self):
        self.total_revenue = 0
        self.distance_traveled = 0
        self.nodes_visited: List[Node] = []


class Node:
    def __init__(self):
        self.location = [0,0]
        self.value = 0
        self.linked_nodes = []
        self.is_depot = False



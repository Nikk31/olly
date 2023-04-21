# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 10:03:16 2023

@author: kusha
"""
"""
#Uniform Cost Search
# Have to store/find path and cost
# Currently like Best First, need to consider previous link costs too
from queue import PriorityQueue
graph={'S': [['1', 2], ['3', 5]], '1': [['G', 1]], '3': [['1', 5], ['G', 6],['4',2]], 'G': [['4', 7]], '2': [['1', 4]], '4': [['2', 4],['5',3]], '5': [['G', 3],['2',6]]}

def UCS(src,goal):
    close=[]
    pq=PriorityQueue()
    pq.put((0,src))
    close.append(src)
    
    while pq.empty()==False:
        u=pq.get()[1]
        print(u,end=" ")
        if u==goal:
            break
        for v,c in graph[u]:
            if v not in close:
                close.append(v)
                pq.put((c,v))
    print()

print(graph)
s=input("Enter Source Node: ")
g=input("Enter Goal Node: ")
UCS(s,g)
"""
import heapq

def tsp_uniform_cost_search(graph, start):
    """Find the shortest path that visits each city exactly once and returns to the starting city."""
    visited = set()  # Set of visited cities
    heap = [(0, start, [start])]  # Heap queue of paths (cost, current city, path)
    while heap:
        (cost, current, path) = heapq.heappop(heap)  # Pop the cheapest path from the heap
        if current not in visited:  # Check if the current city has been visited
            visited.add(current)
            if len(visited) == len(graph):  # Check if all cities have been visited
                return (cost, path + [start])  # Return the shortest path
            for neighbor, weight in graph[current].items():  # Add possible next paths to the heap
                if neighbor not in visited:
                    heapq.heappush(heap, (cost + weight, neighbor, path + [neighbor]))

# Example usage
graph = {
    'A': {'B': 10, 'C': 15, 'D': 20},
    'B': {'A': 10, 'C': 35, 'D': 25},
    'C': {'A': 15, 'B': 35, 'D': 30},
    'D': {'A': 20, 'B': 25, 'C': 30},
}
start = 'A'
print(tsp_uniform_cost_search(graph,start))
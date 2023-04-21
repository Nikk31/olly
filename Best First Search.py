# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 09:14:45 2023

@author: kusha
"""
from queue import PriorityQueue
graph={}

def addedge(x,y,cost):
    if x in graph:
        graph[x].append([y,cost])
    else:
        graph[x]=[[y,cost]]
    if y in graph:
        graph[y].append([x,cost])
    else:
        graph[y]=[[x,cost]]

n=int(input("How many edges to add: "))

for i in range(n):
    x=input("Enter node 1: ")
    y=input("Enter node 2: ")
    cost=int(input("Enter cost: "))
    addedge(x,y,cost)
"""
n=13
graph={'S': [['A', 5], ['B', 4], ['C', 9]], 'A': [['S', 5], ['G', 0]], 'B': [['S', 4], ['D', 2], ['E', 6]], 'C': [['S', 9]], 'G': [['A', 0]], 'D': [['B', 2]], 'E': [['B', 6]]}
"""
def Best_First_Search(src,goal,n):
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
Best_First_Search(s,g,n+1)
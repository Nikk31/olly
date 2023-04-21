# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

graph={'0':['1','2','3'],'1':['4','5'],'2':['6',],'3':[],'4':[],'5':[],'6':[]}

queue=[]
visited=[]
node=input("Enter starting node: ")
queue.append(node)
goal=input("Enter goal node: ")
while queue:
    i=queue.pop(0)
    visited.append(i)
    print(i)
    if i==goal:
       print("Element found")
       break
    for n in graph[i]:
        if n not in visited:    
            queue.append(n)
else:
    print("Element not found")
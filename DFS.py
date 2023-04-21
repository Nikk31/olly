# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 09:53:17 2023

@author: kusha
"""

graph={'0':['1','2','3'],'1':['4','5'],'2':['6',],'3':[],'4':[],'5':[],'6':[]}

stack=[]
visited=[]
node=input("Enter starting node: ")
stack.append(node)
goal=input("Enter goal node: ")
while stack:
    i=stack.pop()
    visited.append(i)
    print(i)
    if i==goal:
       print("Element found")
       break
    for n in graph[i][::-1]:
        if n not in visited:
            stack.append(n)
    '''for n in reversed(graph[i]):
        if n not in visited:
            stack.append(n)'''
else:
    print("Element not found")
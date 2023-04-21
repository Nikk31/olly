# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 09:41:33 2023

@author: kusha
"""

n=int(input("Number of jugs: "))
L=eval(input("Enter a list with the capacity of all jugs: "))
aim=eval(input("Enter goal state(as a list): "))
visited=[]
def nWaterJug(K):
    if(K==aim):
        print(K)
        return True
    if K not in visited:
        print(K)
        visited.append(K)
        for i in range(len(K)):
            
        return (nWaterJug(K))
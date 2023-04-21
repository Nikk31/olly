# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 10:19:53 2023

@author: kusha
"""

cur=[[1,2,3],[4,5,6],[7,0,8]]
goal=[[1,2,3],[4,5,6],[7,8,0]]
n=3
def misplaced(cur,goal):
    hur=0
    for i in range(n):
        for j in range(n):
            if cur[i][j]!=goal[i][j]:
                hur+=1
    return hur

def find_empty(t):
    for i in range(n):
        for j in range(n):
            if t[i][j]==0:
                return (i,j)

def move_up(t,x,y):
    temp=t[x-1][y]
    t[x-1][y]=t[x][y]
    t[x][y]=temp
    return t

def move_left(t,x,y):
    temp=t[x][y-1]
    t[x][y-1]=t[x][y]
    t[x][y]=temp
    return t
    
def move_right(t,x,y):
    temp=t[x][y+1]
    t[x][y+1]=t[x][y]
    t[x][y]=temp
    return t

def move_down(t,x,y):
    temp=t[x+1][y]
    t[x+1][y]=t[x][y]
    t[x][y]=temp
    return t

def simple_hill(cur,nex):
    if nex==goal:
        print("Goal State found!")
        return True
    
    if misplaced(cur,goal)<=misplaced(nex,goal):
        return False
    else:
        return True
    
    x,y=find_empty(cur)
    if x==0:
        if y==0:
            return (simple_hill(cur,move_right(cur,x,y)) or simple_hill(cur,move_down(cur,x,y)))
        elif y==1:
            return(simple_hill(cur,move_right(cur,x,y)) or simple_hill(cur,move_down(cur,x,y)) or simple_hill(cur,move_left(cur,x,y)))
        else:
            return(simple_hill(cur,move_left(cur,x,y)) or simple_hill(cur,move_down(cur,x,y)))
    elif x==2:
        if y==0:
            return (simple_hill(cur,move_right(cur,x,y)) or simple_hill(cur,move_up(cur,x,y)))
        elif y==1:
            return(simple_hill(cur,move_right(cur,x,y)) or simple_hill(cur,move_up(cur,x,y)) or simple_hill(cur,move_left(cur,x,y)))
        else:
            return(simple_hill(cur,move_left(cur,x,y)) or simple_hill(cur,move_up(cur,x,y)))
    else:
        if y==0:
            return(simple_hill(cur,move_right(cur,x,y)) or simple_hill(cur,move_down(cur,x,y)) or simple_hill(cur,move_up(cur,x,y)))
        elif y==1:
            return(simple_hill(cur,move_right(cur,x,y)) or simple_hill(cur,move_up(cur,x,y)) or simple_hill(cur,move_left(cur,x,y)) or simple_hill(cur,move_down(cur,x,y)))
        else:
            return(simple_hill(cur,move_left(cur,x,y)) or simple_hill(cur,move_up(cur,x,y)) or simple_hill(cur,move_down(cur,x,y)))
     
x,y=find_empty(cur)

if x==0:
    if y==0:
        simple_hill(cur,move_right(cur,x,y)) or simple_hill(cur,move_down(cur,x,y))
    elif y==1:
        simple_hill(cur,move_right(cur,x,y)) or simple_hill(cur,move_down(cur,x,y)) or simple_hill(cur,move_left(cur,x,y))
    else:
        simple_hill(cur,move_left(cur,x,y)) or simple_hill(cur,move_down(cur,x,y))
elif x==2:
    if y==0:
        simple_hill(cur,move_right(cur,x,y)) or simple_hill(cur,move_up(cur,x,y))
    elif y==1:
        simple_hill(cur,move_right(cur,x,y)) or simple_hill(cur,move_up(cur,x,y)) or simple_hill(cur,move_left(cur,x,y))
    else:
        simple_hill(cur,move_left(cur,x,y)) or simple_hill(cur,move_up(cur,x,y))
else:
    if y==0:
        simple_hill(cur,move_right(cur,x,y)) or simple_hill(cur,move_down(cur,x,y)) or simple_hill(cur,move_up(cur,x,y))
    elif y==1:
        simple_hill(cur,move_right(cur,x,y)) or simple_hill(cur,move_up(cur,x,y)) or simple_hill(cur,move_left(cur,x,y)) or simple_hill(cur,move_down(cur,x,y))
    else:
        simple_hill(cur,move_left(cur,x,y)) or simple_hill(cur,move_up(cur,x,y)) or simple_hill(cur,move_down(cur,x,y))
print(cur)


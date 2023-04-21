jug1=int(input("Enter Jug 1 capacity: "))
jug2=int(input("Enter Jug 2 capacity: "))
aim=int(input("Enter the desired quantity: "))
visited=[] 
def waterJug(amt1, amt2):
    if (amt1 == aim and amt2 == 0) or (amt2 == aim and amt1 == 0):
        print(amt1, amt2)
        return True
     
    if [amt1, amt2] not in visited:
        print(amt1, amt2)
     
        visited.append([amt1, amt2])
     
        return (waterJug(0, amt2) or waterJug(amt1, 0) or waterJug(jug1, amt2) or 
                waterJug(amt1, jug2) or 
                waterJug(amt1 + min(amt2, (jug1-amt1)),amt2 - min(amt2, (jug1-amt1))) 
                or waterJug(amt1 - min(amt1, (jug2-amt2)),amt2 + min(amt1, (jug2-amt2))))
    else:
        return False
print("Steps: ")
waterJug(0,0)

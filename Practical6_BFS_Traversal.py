#6. Write Python program for checking whether a given graph G has simple path from source s to 
#destination d. Assume the graph G is represented using adjacent matrix.

Adj_List={
    "A":["B","D"],
    "B":["C","A"],
    "C":["B"],
    "D":["A","E","F"],
    "E":["D","F","G"],
    "F":["D","E","H"],
    "G":["E","H"],
    "H":["G","F"]
}
#BFS program
visited={}
level={}#Dictionary for distance 
parent={}#Dictionary for find path from source to any another node in the graph
BFS_Traversal_Output=[]#List to store order of Traversal node
Queue=[]

for node in Adj_List.keys():
    visited[node]= False
    parent[node]= None
    level[node]=-1 #infinity
"""
print(visited)
print(level)
print(parent)
"""
s="A"
visited[s]=True 
level[s]=0
Queue.append(s)

while Queue:# Queue is not empty
    u=Queue.pop(0)#pop up first element in queue
    BFS_Traversal_Output.append(u)

    #Explore all the adjacent vertex of u
    for v in Adj_List[u]:
        if not visited[v]:
            visited[v]=True
            parent[v]=u 
            level[v]=level[u]+1
            Queue.append(v)

print(BFS_Traversal_Output)

#Printing shortest distance of node from root node
print(level)
print(level["G"])

#Printing shortest path from source to given node
v="G"
path=[]

while v is not None:
    path.append(v)
    v=parent[v]
path.reverse()
print(path)







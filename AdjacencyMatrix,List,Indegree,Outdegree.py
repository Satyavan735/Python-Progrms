"""
adj_list={"A":["B","C"],
          "B":["A","D","E"],
          "C":["A","D"],
          "D":["C","B","E"],
          "E":["B","D"]

    }
print(adj_list["B"])

#Adding edge between two node
adj_list["A"].append("D")
adj_list["D"].append("A")
print(adj_list)
"""

#Program To Print Adjacency Matrix ,AdjacencyList,Indegree and Outdegree of the Node
Edges=[("A","B"),("A","C"),("B","C"),("B","D"),("B","E"),("C","D"),("D","E")]

class Graph:
    def __init__(self,Node,Directed=False):
        self.node=Node
        self.ADJ_List={} #Initilize dictionary as empty
        self.Directed=Directed

        for node in self.node:
            self.ADJ_List[node]=[]
    def Print_Node(self):
        for node in self.node:
            print(node,":",self.ADJ_List[node])
    
    #Adding edges bet Nodes
    def ADD_Edge(self,vertex,edge):
        self.ADJ_List[vertex].append(edge)
        if not self.Directed:
             self.ADJ_List[edge].append(vertex)
    
    def degree_V(self,vertex):
        Degree=len(self.ADJ_List[vertex])
        return Degree

#Taking User input for nodes of the graph
nodes=[]
No_of_Nodes=int(input("Enter Number of vertex present in the graph:"))
for i in range(No_of_Nodes):
    nodes.append(str(input("Enter Node:")))

print("\n Graph nodes are :",nodes)
print("\n Enter 1 for directed graph or 0 for undirected graph")
G_D=int(input("Enter type of graph:"))
if G_D==1:
    Directed=True
else:
    Directed=False
        

graph=Graph(nodes,Directed)
#graph.ADD_Edge("A","B")
edges=[]
no_of_edges=int(input("Enter number of edges:"))
for i in range(no_of_edges):
    edges.append((input("Edge from vertex:"),input("\tTo vertex:")))
    #V1,V2 =input("Edge from Vertex:").split(",")
    #edges.append((V1,V2))

print(edges)

   
for v,e in edges:
    graph.ADD_Edge(v,e)
graph.Print_Node()
print("\nPrinting degree of particular Node:")
D_Node=str(input("Enter a node for degree:"))
print(f"Degree of {D_Node} is:",graph.degree_V(D_Node))














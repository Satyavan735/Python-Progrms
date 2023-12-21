#Printing Indegree And Outdegree Of The Given Node:

class Graph:
    def __init__(self,Node,Directed=False):
        self.nodes=Node
        self.directed=Directed
        self.Adj_List={}

        for node in self.nodes:
            self.Adj_List[node]=[]
    
    def Print_Adj(self):
        for node in self.nodes:
            print(node,"-->>",self.Adj_List[node])

    def Node_Edge(self,vertex1,vertex2):
        self.Adj_List[vertex1].append(vertex2)
        if not self.directed:
            self.Adj_List[vertex2].append(vertex1)

    def Degree_Vertex(self,V):
        Degree=len(self.Adj_List[V])
        return Degree
        
#Creating an object
Node=[]
#Taking input from user to add node
Max_NO_Node=int(input("Enter number of nodes:"))
for i in range(Max_NO_Node):
    Node.append(input("Enter node value:"))
print("\n Graph nodes are:",Node)
print("\n Enter 1 for directed graph or 0 for undirected graph")
G_D=int(input("Enter type of graph:"))
if G_D==1:
    Directed=True
else:
    Directed=False
        
G=Graph(Node,Directed)

Node_Edge=[]
No_Of_Edges=int(input("\nEnter number of the edges:"))
for i in range(No_Of_Edges):
    Node_Edge.append((input("Enter edge from vertex:"),input("\tTo vertex ")))

for v,e in Node_Edge:
    G.Node_Edge(v,e)   
G.Print_Adj()
Deg_N=str(input("\nEnter vertex for degree:"))
print(f"Degree of {Deg_N} vertex is:",G.Degree_Vertex(Deg_N))
#print(G.In_Degree("A"))

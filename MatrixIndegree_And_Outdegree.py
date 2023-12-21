import numpy as np
Nodes=[]
R=int(input("Enter number of nodes present in graph"))
for i in range(R):
    Nodes.append(str(input(f"Enter{i+1} node Value:")))
print("\nGraph nodes are:",Nodes)

Mat=[]
R=len(Nodes)

for i in range(R):
    a=[]
    for j in range(R):
        a.append(int(input("\n Edge presernt then enter 1 otherwise enter 0")))
    Mat.append(a)

print(np.matrix(Mat))

def outdegree(Mat):
    count=0
    for i in range(R):
        count=0
        for j in range(R):
            if Mat[i][j]==1:
                count=count+1
        print(i,"==",count)

outdegree(Mat)




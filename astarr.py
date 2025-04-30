from heapq import heappop,heappush

n=int(input("Enter number of edges:"))
graph={}
print("Enter edges(node1 node2 cost):")
for _ in range(n):
    u,v,c=input().split()
    graph.setdefault(u,{})[v]=int(c)
    
nodes=set(graph)|{v for nbrs in graph.values() for v in nbrs}
heuristic={node:int(input(f"Heuristic for {node}:"))for node in nodes}

start=input("Start node:")
goal=input("Goal node:")

def astar(graph,start,goal,h):
    q=[(h[start],0,start,[])]
    while q:
        f,g,node,path=heappop(q)
        if node==goal:
            return path+[node]
        for nbr,cost in graph.get(node,{}).items():
            heappush(q,(g+cost+h[nbr],g+cost,nbr,path+[node]))
    return None    
 
path=astar(graph,start,goal,heuristic)
print("Path:",path) 
    
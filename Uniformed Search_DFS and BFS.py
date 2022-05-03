#Declaring the class for Graph

class Graph:
  def __init__(self, V):
    self.V = V
    self.adj = {}
    for i in range(self.V):
      self.adj[i] = []

  #Function for adding edge in the graph
  def add_edge(self, src, dest, isundir=True):
    self.adj[src].append(dest)
    if isundir:
      self.adj[dest].append(src)


  #Function for printing the adjacant edge in the result
  def print_adj_list(self):
    for i in range(self.V):
      print(i, end=" : ")
      for j in self.adj[i]:
        print(j , end=" ")
      print()


  #Function for BFS
  def bfs(self, src, goal):
    q = [src]
    visited = [False]*self.V
    visited[src] = True
    while(len(q)):
      f = q[0]
      print(f, end=" ")
      q.pop(0)
      if(f==goal): return
      for i in self.adj[f]:
        if visited[i]==False:
          q.append(i)
          visited[i] = True
  
  
  def util(self, src, goal, visited):
    if visited[goal]==True: return
    visited[src] = True
    print(src, end=" ")
    for i in self.adj[src]:
      if visited[i]==False:
        self.util(i, goal, visited)
    return

 #Function for DFS
  def dfs(self, src, goal):
    visited = [False]*self.V
    self.util(src, goal, visited)
    return

#Driver Code

#Creating the Graph and adding the edge
my_graph = Graph(6)
my_graph.add_edge(0, 2)
my_graph.add_edge(1, 2)
my_graph.add_edge(1, 4)
my_graph.add_edge(2, 3)
my_graph.add_edge(4, 5)
my_graph.add_edge(5, 3)


#Final Results

print("The DFS of the graph is:    ", end="")
my_graph.dfs(1, 0)
print("\n\n\nThe BFS of the graph is:    ", end="")
my_graph.bfs(1, 0)
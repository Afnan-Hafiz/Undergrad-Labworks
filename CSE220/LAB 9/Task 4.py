def convert_undirected_list(self):
  for i in range(self.size):
    current = self.adj_list[i]
    while current!=None:
      a,b,c=current.source, current.destination, current.weight
      reverse = self.vertex_index[b]
      reverseCurrent = self.adj_list[reverse]
      directed=False
      while reverseCurrent!=None:
        if reverseCurrent.destination==a:
          directed=True
          break
        reverseCurrent=reverseCurrent.next

      if directed==False:
        self.add_edge(b, a, c)
      current= current.next
  self.directed = False

def convert_undirected_matrix(self):
  if self.directed==True:
    for i in range(self.size):
      for j in range(self.size):
        if self.adj_matrix[i][j] != 0:
          self.adj_matrix[j][i] = self.adj_matrix[i][j]
  self.directed = False


#Driver Code
demo = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
matrix_Graph= Graph(demo,True)
list_Graph= AdjacencyListGraph(demo,True)

number_of_edges=[('A', 'B', 1), ('A', 'C', 1),  ('A', 'G', 1),
                  ('B', 'C', 1), ('B', 'D', 2), ('B', 'E', 2), ('C', 'D', 5),
                  ('C', 'F', 2), ('D', 'E', 4), ('D', 'G', 3),
                  ('E', 'G', 1), ('F', 'G', 1), ('B', 'F', 3)]

for i,j,k in number_of_edges:
  matrix_Graph.add_edges(i,j,k)
  list_Graph.add_edges([(i,j,k)])

print("For Matrix---")
convert_undirected_matrix(matrix_Graph)
matrix_Graph.print_matrix()

print()

print("For List---")
convert_undirected_list(list_Graph)
list_Graph.print_list()
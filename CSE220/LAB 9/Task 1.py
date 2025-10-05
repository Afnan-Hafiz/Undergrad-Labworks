def max_degree_list(self):
      max=0
      for i in self.num_vertices:
        degree_count= self.get_degree(i)
        if degree_count> max:
          max=degree_count
          maxvertex=i
      return (max,maxvertex)

def max_degree_matrix(self):
      max=0
      vertex=None
      for i in self.num_vertices:
        degree_count= self.get_degree(i)
        if degree_count> max:
          max=degree_count
          maxvertex=i
      return (max,maxvertex)



#Driver Code
demo = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
matrix_Graph= Graph(demo)
list_Graph= AdjacencyListGraph(demo)

number_of_edges=[('A', 'B', 0), ('A', 'C', 0),  ('A', 'G', 0),
                  ('B', 'C', 0), ('B', 'D', 0), ('B', 'E', 0), ('C', 'D', 0),
                  ('C', 'F', 0), ('D', 'E', 0), ('D', 'G', 0),
                  ('E', 'G', 0), ('F', 'G', 0), ('B', 'F', 0)]

for i,j,k in number_of_edges:
  matrix_Graph.add_edges(i,j)
  list_Graph.add_edges([(i,j,k)])


print("For Matrix---")
print("Vertex:", max_degree_matrix(matrix_Graph)[1] )
print("Degree:", max_degree_matrix(matrix_Graph)[0])
print()

print("For List---")
print("Vertex:", max_degree_list(list_Graph)[1])
print("Degree:", max_degree_list(list_Graph)[0])
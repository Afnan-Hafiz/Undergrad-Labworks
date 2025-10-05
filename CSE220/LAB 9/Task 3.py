def max_weight_list(self):
      max=0
      for i in self.num_vertices:
        weight= self.get_weight_list(i)
        if weight> max:
          max=weight
          maxvertex=i
      return (max,maxvertex)

def max_weight_matrix(self):
      max=0
      for i in self.num_vertices:
        count= self.get_weight_matrix(i)
        if count> max:
          max=count
          maxvertex=i
      return (max,maxvertex)

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
matrix_Graph= Graph(demo,True)
list_Graph= AdjacencyListGraph(demo,True)

number_of_edges=[('A', 'B', 1), ('A', 'C', 1),  ('A', 'G', 1),
                  ('B', 'C', 1), ('B', 'D', 2), ('B', 'E', 2), ('C', 'D', 5),
                  ('C', 'F', 2), ('D', 'E', 4), ('D', 'G', 3),
                  ('E', 'G', 1), ('F', 'G', 1), ('B', 'F', 3)]

for i,j,k in number_of_edges:
  matrix_Graph.add_edges(i,j,k)
  list_Graph.add_edges([(i,j,k)])

print("FOR DIRECTED WEIGHTED GRAPH")
print()
print("For Matrix---")
print("Vertex:", max_weight_matrix(matrix_Graph)[1] )
print("Weight:", max_weight_matrix(matrix_Graph)[0])
print("Degree:", max_degree_matrix(matrix_Graph)[0])

print()

print("For List---")
print("Vertex:", max_weight_list(list_Graph)[1])
print("Weight:", max_weight_list(list_Graph)[0])
print("Degree:", max_degree_list(list_Graph)[0])
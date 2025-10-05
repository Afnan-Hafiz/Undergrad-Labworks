#Adjacency matrix for Undirected Unweighted Graph
import numpy as np
class Graph:
    def __init__(self, num_vertices):
        self.size = len(num_vertices)
        self.num_vertices = num_vertices
        self.adj_matrix = np.zeros((self.size,self.size), dtype=int)
        self.vertex_index = {}
        self.maxvertex=None
        for i in range(self.size):
          self.vertex_index[num_vertices[i]] = i

    def add_edges(self, i, j):
        m = self.vertex_index[i]
        n = self.vertex_index[j]
        self.adj_matrix[m][n] = 1
        self.adj_matrix[n][m] = 1

    def print_matrix(self):
        print("Adjcaency Matrix:")
        for row in self.adj_matrix:
            print(row)

    def get_degree(self, num_vertices):
        u = self.vertex_index[num_vertices]
        degree = 0
        for k in range(self.size):
            if u==k:
              continue
            if self.adj_matrix[u][k] != 0:
                degree += 1
        return degree

    def max_degree_matrix(self):
      max=0
      vertex=None
      for i in self.num_vertices:
        degree_count= self.get_degree(i)
        if degree_count> max:
          max=degree_count
          self.maxvertex=i
      return (max,self.maxvertex)



#Adjacency list for Undirected Unweighted graph
class Edge:
    def __init__(self, source, destination, next_node=None):
        self.source = source
        self.destination = destination
        self.next = next_node

class AdjacencyListGraph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.size = len(num_vertices)
        self.adj_list = [None] * self.size
        self.vertex_index = {}
        for i in range(len(num_vertices)):
          self.vertex_index[num_vertices[i]] = i
        self.maxvertex=None


    def add_edges(self, edges):
        for source, destination in edges:
            self.add_edge(source, destination)
            self.add_edge(destination, source)

    def add_edge(self, source, destination):
        new_edge = Edge(source, destination)
        new_edge.next = self.adj_list[self.vertex_index[source]]
        self.adj_list[self.vertex_index[source]] = new_edge

    def print_list(self):
        print("Adjacency List:")
        for i in range(self.size):
            print(f"{i}: ", end="")
            current = self.adj_list[i]
            while current:
                print(f"{current.destination}", end=" ")
                current = current.next
            print()

    def get_degree(self, num_vertices):
        a = self.vertex_index[num_vertices]
        degree = 0
        current = self.adj_list[a]
        while current!=None:
            degree += 1
            current = current.next
        return degree

    def max_degree_list(self):
      max=0
      for i in self.num_vertices:
        degree_count= self.get_degree(i)
        if degree_count> max:
          max=degree_count
          self.maxvertex=i
      return (max,self.maxvertex)



#Driver Code
demo = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
matrix_Graph= Graph(demo)
list_Graph= AdjacencyListGraph(demo)

number_of_edges=[('A', 'B'), ('A', 'C'),  ('A', 'G'),
                  ('B', 'C'), ('B', 'D'), ('B', 'E'), ('C', 'D'),
                  ('C', 'F'), ('D', 'E'), ('D', 'G'),
                  ('E', 'G'), ('F', 'G'), ('B', 'F')]

for i,j in number_of_edges:
  matrix_Graph.add_edges(i,j)
  list_Graph.add_edges([(i,j)])

print("For Matrix---")
print("Vertex:", matrix_Graph.max_degree_matrix()[1] )
print("Degree:", matrix_Graph.max_degree_matrix()[0])
print()

print("For List---")
print("Vertex:", list_Graph.max_degree_list()[1])
print("Degree:", list_Graph.max_degree_list()[0])
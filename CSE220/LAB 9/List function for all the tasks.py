#list function
class WEdge:
    def __init__(self, source, destination, weight, next_node=None):
        self.source = source
        self.destination = destination
        self.weight = weight
        self.next = next_node

class AdjacencyListGraph:
    def __init__(self, num_vertices, directed=False):
        self.num_vertices = num_vertices
        self.size = len(num_vertices)
        self.directed= directed
        self.adj_list = [None] * self.size
        self.vertex_index = {}
        for i in range(len(num_vertices)):
          self.vertex_index[num_vertices[i]] = i
        self.maxvertex=None


    def add_edges(self, edges):
        for source, destination, weight in edges:
            self.add_edge(source, destination, weight)
            if self.directed==False:
              self.add_edge(destination, source, weight)

    def add_edge(self, source, destination, weight=None):
        a=self.vertex_index[source]
        new_edge = WEdge(source, destination, weight)
        new_edge.next = self.adj_list[a]
        self.adj_list[a] = new_edge


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

    def get_weight_list(self, num_vertices):
        a = self.vertex_index[num_vertices]
        totalweight = 0
        current = self.adj_list[a]
        while current!=None:
          totalweight  += current.weight
          current = current.next
        return totalweight
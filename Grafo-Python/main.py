class Grafo:
  
  def __init__(self, vertices):
    self.vertices = vertices
    self.grafo = [[0] * vertices for i in range(vertices)]
    
  def add_aresta(self, u, v):
    self.grafo[u-1][v-1] = 1 
    self.grafo[v-1][u-1] = 1 
  
  def show(self):
    for i in self.grafo:
      for j in i:
        print(j, end=' ')
      print('')
    
  def bfs(self, v):
    
    visitados = [False] * self.vertices
    visitados[v-1] = True
    fila = [v-1]
    
    while len(fila) > 0:
      
      v = fila[0]
      for u in range(self.vertices):
        if self.grafo[v][u] == 1:
          if not visitados[u]:
            visitados[u] = True
            fila.append(u)
            print("%d" %(u+1))
            
      fila.pop(0)
      
      
      
      
      
g = Grafo(10)

g.add_aresta(8,9)
g.add_aresta(3,7)
g.add_aresta(1,4)
g.add_aresta(7,8)
g.add_aresta(0,5)
g.add_aresta(5,2)
g.add_aresta(3,8)
g.add_aresta(2,9)
g.add_aresta(0,6)
g.add_aresta(4,9)
g.add_aresta(2,6)
g.add_aresta(6,4)
g.bfs(0)

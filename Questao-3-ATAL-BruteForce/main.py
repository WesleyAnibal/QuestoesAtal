#coding: utf-8
saida = []
for i in range(10):
  codigo = ""
  codigo += "%d" %(i)
  for j in range(10):
    codigo+= "%d" %(j)
    for k in range(10):
      codigo+= "%d" %(k)
      for l in range(10):
        codigo += "%d" %(l)
        saida.append(codigo)
        codigo = ("%d%d%d" %(i, j, k))
      codigo = ("%d%d" %(i, j))
    codigo = ("%d" %(i))
  codigo = ""
  
print(saida)
      
        
        
    


def maior_soma(lista):
  lis = [0 for i in range(len(lista))]
  lis[0] = lista[0]
  maior = lis[0]
  for q in range(len(lista)-1):
    if(lis[q] > 0):
      lis[q+1] = lis[q]+lista[q+1]
      if(lis[q+1] > maior):
        maior = lis[q+1]
    else:
      lis[q+1] = lista[q+1]
  return maior
  
    
     
    
print(maior_soma([40,-65,20,-15,30,-10,-30,25]))
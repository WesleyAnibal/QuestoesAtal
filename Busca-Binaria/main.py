#coding: utf-8

def buscaBinaria(array, target):
    lower = 0
    upper = len(array)
    while lower < upper:   # use < instead of <=
        x = lower + (upper - lower) // 2
        val = array[x]
        if target == val:
          while target == array[x]:
            x-=1 
          x+=1 
          return x
        elif target > val:
            if lower == x:   # this two are the actual lines
                break        # you're looking for
            lower = x
        elif target < val:
            upper = x

cont = 1
while(True):
  entrada = input().split()
  
  if entrada[0] == "0" and entrada[-1] == "0":
    break

  N, Q = int(entrada[0]), int(entrada[-1])

  lista = []

  for i in range(N):
    ent = int(input())
    lista.append(ent)
  lista = sorted(lista)
  print("CASE# %d:" %cont)
  for i in range(Q):
    num = int(input())
    index = buscaBinaria(lista, num)
    if(index == None):
      print("%d not found" %num)
    else:
      print("%d found at %d"%(num,index+1))
  cont+=1

    

   


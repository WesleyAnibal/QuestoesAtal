#coding: utf-8

entrada = int(input())
for i in range(entrada):
  ent = int(input())
  def fibPD(n):
  	lista = [0,1]
  	for i in range(2,n+1):
  		lista.append(lista[i-1] + lista[i-2])
  	return lista[n]
  
  def contagem(n):
    a = [0,0,2]
    for i in range(3,n+1):
      a.append(a[i-1]+a[i-2]+2)
    return a[n]
  print("fib(%d) = %d calls = %d"%(ent,contagem(ent), fibPD(ent)))
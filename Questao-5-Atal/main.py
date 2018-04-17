#coding: utf-8

while(True):
  entrada = int(input())
  if(entrada == 0): break
  lista,result= list(map(int, input().split(" "))), 0
  for i in range(1, len(lista)):
    if lista [i-1] < 0: 
      result = result + (-1 * lista[i-1])
    else: 
      result = result + lista[i-1]
    lista[i] = lista[i] + lista[i-1]
  print(result)
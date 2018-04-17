#coding: utf-8
import sys

saida = []

def f(elem, i, palavra):
  andei = []
  for i in range(i,len(palavra)):
    if(palavra[i] not in andei):
      andei.append(palavra[i])
      sequencia = elem + palavra[i]
      saida.append(sequencia)
      print(sequencia)
      f(sequencia,i+1, palavra)
    
while True:
  try:
    entrada = input()
    if entrada == "":
      break
    if len(entrada) <= 1000:
      f("",0 , entrada)
      for i in sorted(saida):
        print(i)
      print("")
      saida = []
  except EOFError:
    sys.exit()
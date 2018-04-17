# -*- coding: utf-8 -*-

def dfs(i,j, visitado, ma):
  x = [1,0,-1,0]
  y = [0,1,0,-1]
  visitado[i][j] = True
  if visitado[4][4]:
    return
  for k in range(4):
  	n_i = i + x[k]
  	n_j = j + y[k]
  	if n_i >= 0 and n_i <= 4 and n_j >= 0 and n_j <= 4:
  	  if ma[n_i][n_j] == "0":
  	    if not visitado[n_i][n_j]:
  		    dfs(n_i,n_j,visitado,ma)

n = int(input())
for j in range(n):
  visitado = [[False]*5 for i in range(5)]
  m = []
  input()
  for i in range(5):
  	entrada = input().split()
  	m.append(entrada)
  
  if m[0][0] == "1":
    print("ROBBERS")
  else:
    dfs(0,0,visitado,m)
    
    
    
    if visitado[4][4]:
    	print("COPS")
    else:
    	print("ROBBERS")
    




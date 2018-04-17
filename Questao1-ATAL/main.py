#coding: utf-8

palavra1 = input()
palavra2 = input()
count = 0
if len(palavra1) == len(palavra2):
  for i in range(len(palavra1)):
    if palavra1[i] != palavra2[i]:
      count+= 1 
  print(count <= 1)
elif len(palavra1) > len(palavra2):
  i = 0
  j = 0
  while i < len(palavra2) and j < len(palavra1):
    if palavra2[i] == palavra1[j]:
      i+=1 
      j+=1
    else:
      j+=1 
      count+=1 
  print(count<=1)
      
    
      
  
  
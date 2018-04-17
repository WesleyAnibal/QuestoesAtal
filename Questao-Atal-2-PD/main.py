def primeiraPassada(palavra):
  saida = ""
  for i in palavra:
    if(i.isalpha()):
      saida += chr(ord(i)+3)
    else:
      saida += i
  return saida
  

def segundaPassada(palavra):
  saida = ""
  for i in range(len(palavra)-1, -1, -1):
    saida += palavra[i]
  
  return saida
  
def terceiraPassada(palavra):
  saida = palavra[0:int(len(palavra)/2)]
  for i in range(int(len(palavra)/2), len(palavra)):
    saida+= chr(ord(palavra[i])-1)
  
  return saida
  
entrada = int(input())
for i in range(entrada):
  s = input()
  print(terceiraPassada(segundaPassada(primeiraPassada(s))))
    
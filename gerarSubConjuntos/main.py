def gerar_subconjuntos(S, vet, K, N, y, G):
  
  if K == N:
    if(vet.count(True) == y):
      t = ''
      for i in range(N):
        if vet[i] == True:
          t+= S[i]
      G.append(int(t))
  else:
    vet[K] = True
    gerar_subconjuntos(S,vet, K+1, N, y, G)
    vet[K] = False
    gerar_subconjuntos(S,vet, K+1, N, y, G)

while True:
  entrada = input().split()
  if entrada[0] == '0' and entrada[1] == '0':
    break
  S = input()
  G = []
  vet = [False for i in range(int(entrada[0]))]
  gerar_subconjuntos(S, vet, 0, int(entrada[0]),len(S) - int(entrada[1]),G)
  print(max(set(G)))
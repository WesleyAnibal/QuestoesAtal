#coding: utf-8

def maior_soma(lista):
    max_ate_agora = min(lista)
    for i in range(0, len(lista)):
        soma = 0.0
        for j in range(i, len(lista)):
            soma = soma + lista[j]
            max_ate_agora = max(max_ate_agora, soma)
    return max_ate_agora
    
print(maior_soma([10,5,-17, 20,50,-1,3, -30,10]))
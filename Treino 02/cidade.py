'''
Podemos usar um (multi) grafo para representar um mapa de uma cidade: 
cada nó representa um cruzamento e cada aresta uma rua.
Pretende-se que implemente uma função que calcula o tamanho de uma cidade, 
sendo esse tamanho a distância entre os seus cruzamentos mais afastados.
A entrada consistirá numa lista de nomes de ruas (podendo assumir que os 
nomes de ruas são únicos). Os identificadores dos cruzamentos correspondem a 
letras do alfabeto, e cada rua começa (e acaba) no cruzamento 
identificado pelo primeiro (e último) caracter do respectivo nome.
'''
import pprint  
def build(arestas):
    edges=sorted(arestas, key =lambda x : -len(x))
    adj = {}
    for rua in edges:
        if rua[0] not in adj:
            adj[rua[0]] = {}
        if rua[-1] not in adj:
            adj[rua[-1]] = {}
        
        adj[rua[0]][rua[-1]] = len(rua)
        adj[rua[-1]][rua[0]] = len(rua)
    return adj


def fw(adj):
    dist = {}
    for o in adj:
        dist[o] = {}
        for d in adj:
            if o == d:
                dist[o][d] = 0
            elif d in adj[o]:
                dist[o][d] = adj[o][d]
            else:
                dist[o][d] = float("inf")
    for k in adj:
        for o in adj:
            for d in adj:
                if dist[o][k] + dist[k][d] < dist[o][d]:
                    dist[o][d] = dist[o][k] + dist[k][d]
    return dist


def tamanho(ruas):
    arestas = build(ruas)
    arestas = fw(arestas)
    maior = 0
    for o in arestas:
        for d in arestas[o]:
            if arestas[o][d] > maior:
                maior = arestas[o][d]
    return maior
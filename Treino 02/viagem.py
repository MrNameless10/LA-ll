'''

Implemente uma função que calcula o preço mais barato para fazer uma viagem de
autocarro entre duas cidades. A função recebe (para além das duas cidades) uma
lista de rotas de autocarro, onde cada rota é uma sequência de cidades por onde
passa o autocarro, intercalada com o custo para viajar entre cada par de cidades.
Assuma que cada rota funciona nos dois sentidos.

'''

def build(rotas): 
   adj = {}
   
   
   for lista in rotas: 
       cont = 0
       while (cont < len(lista)):
         if lista[cont] not in adj: 
           adj[lista[cont]] = {} 
         if (cont +2) < len(lista):
           if lista[cont+2] not in adj: 
             adj[lista[cont+2]] = {}
         else:
            break
         adj[lista[cont]][lista[cont+2]]= lista[cont+1]
         adj[lista[cont+2]][lista[cont]]= lista[cont+1]
         cont+=2
         
   return adj


def bfs(adj,o): 
    pai = {} 
    vis = {o} 
    queue = [o] 
    dist = {}
    dist[o] = 0
    
 
    while queue: 
       v = queue.pop(0)
       for d in adj[v]: 
           if d not in vis: 
               vis.add(d) 
               pai[d] = v 
               dist[d] = dist[v] + adj[v][d]
               queue.append(d)

    return dist 
    


def viagem(rotas,o,d):
    if rotas==[]:
        return 0
    dist = bfs(build(rotas), o)
    r = dist[d]
    return r
'''80%'''


'''100%'''


'''
Implemente uma função que calcula o preço mais barato para fazer uma viagem de
autocarro entre duas cidades. A função recebe (para além das duas cidades) uma
lista de rotas de autocarro, onde cada rota é uma sequência de cidades por onde
passa o autocarro, intercalada com o custo para viajar entre cada par de cidades.
Assuma que cada rota funciona nos dois sentidos.
"Fuck grafos, all my homies hate grafos"
'''

def fixRotas(rotas):
    lista = []
    
    for rota in rotas:
        posOrigem = 0
        posDestino = 2
        posPreco = 1
        while posDestino + 1 <= len(rota):
            lista.append([rota[posOrigem],rota[posPreco],rota[posDestino]])
            posOrigem = posDestino
            posDestino += 2
            posPreco += 2
    
    return lista

def viagem(rotas,o,d):
    rotas = fixRotas(rotas)

    caminhos = {o:0} # { destino:preco }
    orla = [(o,0)] # [ (destino, preco) ]
    
    for cid, preco in orla:
        proximos = filter(lambda x: cid in x, rotas)
        for prox in proximos:
            if prox[0] == cid:
                proximoDestino = prox[2]
            else:
                proximoDestino = prox[0]
            novoPreco = preco + prox[1]
                
            if proximoDestino not in caminhos:
                caminhos[proximoDestino] = novoPreco
                orla.append((proximoDestino,novoPreco))
            elif novoPreco < caminhos[proximoDestino]:
                caminhos[proximoDestino] = novoPreco
                orla.append((proximoDestino,novoPreco))

    return caminhos[d]


'''100%'''

'''
Implemente uma função que calcula o preço mais barato para fazer uma viagem de
autocarro entre duas cidades. A função recebe (para além das duas cidades) uma
lista de rotas de autocarro, onde cada rota é uma sequência de cidades por onde
passa o autocarro, intercalada com o custo para viajar entre cada par de cidades.
Assuma que cada rota funciona nos dois sentidos.
'''

def dijkstra(adj,o):
    dist = {}
    dist[o] = 0
    orla = {o}
    while orla:
        v = min(orla,key=lambda x: dist[x])
        orla.remove(v)
        for d in adj[v]:
            if d not in dist:
                orla.add(d)
                dist[d] = float("inf")
            if dist[v] + adj[v][d] < dist[d]:
                dist[d] = dist[v] + adj[v][d]
                
    return dist


def viagem(rotas,o,d):
    grafo = {}
    
    if o == d:
        return 0
    # construção do grafo
    for rota in rotas:
        i = 0
        while i < len(rota)-1:
            if rota[i] not in grafo:
                grafo[rota[i]] = {}

            if rota[i+2] not in grafo:
                grafo[rota[i+2]] = {}
                
            grafo[rota[i]][rota[i+2]] = rota[i+1]
            grafo[rota[i+2]][rota[i]] = rota[i+1]
            i+= 2
    
    print(grafo)
    dist = dijkstra(grafo, o)
    print(dist)
    
    return dist[d]
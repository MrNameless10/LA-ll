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
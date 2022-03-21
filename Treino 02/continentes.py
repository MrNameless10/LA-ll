'''

O objectivo deste problema é determinar o tamanho do maior continente de um planeta.
Considera-se que pertencem ao mesmo continente todos os países com ligação entre si por terra. 
Irá receber uma descrição de um planeta, que consiste numa lista de fronteiras, onde cada fronteira
é uma lista de países que são vizinhos entre si. 
A função deverá devolver o tamanho do maior continente.

'''

def contamais(lista):
    if lista == []:
        return 0
    
    dic = {}
    for elem in lista:
        if elem not in dic:
            dic[elem] = 1
        else:
            dic[elem] += 1
    
    listar = [k for b,k in dic.items()]    
        
    return max(listar)
    
def build(vizinhos): 
   adj = {}

   for lista in vizinhos:
       for i in range(len(lista)):
         if lista == []:
             break
         if lista[i] not in adj:
            adj[lista[i]] = set()
         if (i+1)<(len(lista)):
            if lista[i+1] not in adj: 
              adj[lista[i+1]] = set()
            adj[lista[i]].add(lista[i+1])
            adj[lista[i+1]].add(lista[i])
        
    

   return adj
   
def bfs(adj,o, comp, c): 
    pai = {} 
    vis = {o} 
    queue = [o] 
    comp[o] = c
    
    
 
    while queue: 
       v = queue.pop(0)
       for d in adj[v]: 
           if d not in vis: 
               vis.add(d) 
               pai[d] = v 
               comp[d] = c
               queue.append(d)

    
def maior(vizinhos):
    if vizinhos==[]:
        return 0
    
   
    c = 1
    comp = {}
    vizinhos = sorted(vizinhos, key = lambda x : -len(x))
    for v in build(vizinhos):
        comp[v] = -1
        
    for v in build(vizinhos):
        if comp[v] == -1:
            bfs(build(vizinhos), vizinhos[0][0], comp, c)
        c+=1
        
    listar = [k for b,k in comp.items()]
    res = contamais(listar)
        
    return res
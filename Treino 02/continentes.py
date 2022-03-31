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

'''80%'''




'''100%'''
'''
O objectivo deste problema é determinar o tamanho do maior continente de um planeta.
Considera-se que pertencem ao mesmo continente todos os países com ligação entre si por terra. 
Irá receber uma descrição de um planeta, que consiste numa lista de fronteiras, onde cada fronteira
é uma lista de países que são vizinhos entre si. 
A função deverá devolver o tamanho do maior continente.
'''
vizinhos = [["Portugal","Espanha"],["Espanha","França"],["França","Bélgica","Alemanha","Luxemburgo"],["Canada","Estados Unidos"]]
            
def build (arestas):
    adj = {}
    for fronteira in arestas:
        for front1 in range(len(fronteira)):
            for front2 in range(front1+1,len(fronteira)):
                if fronteira[front1] not in adj:
                    adj[fronteira[front1]] = set()
                if fronteira[front2] not in adj:
                    adj[fronteira[front2]] = set()
                adj[fronteira[front1]].add(fronteira[front2])
                adj[fronteira[front2]].add(fronteira[front1])
    return adj
def bfs(adj,o):
    pai = {}
    vis = {o}
    queue = [o]
    while queue:
        v = queue.pop(0)
        for d in adj[v]:
            if d not in vis:
                vis.add(d)
                pai[d] = v
                queue.append(d)
    return pai

def maior(vizinhos):
    if vizinhos == []:
        return 0
    vizinhos = sorted(vizinhos, key = lambda x : -len(x))
    arestas = build(vizinhos)
    print(arestas)
    maior = 0
    for pais in arestas:
        maior = max(len(bfs(arestas,pais)),maior)
    
    return maior+1


'''100%'''
'''
O objectivo deste problema é determinar o tamanho do maior continente de um planeta.
Considera-se que pertencem ao mesmo continente todos os países com ligação entre si por terra. 
Irá receber uma descrição de um planeta, que consiste numa lista de fronteiras, onde cada fronteira
é uma lista de países que são vizinhos entre si. 
A função deverá devolver o tamanho do maior continente.
'''
def removePaisesVis(visitados, paises):
    r = []
    for pais in paises:
        if pais not in visitados:
            r.append(pais)
            
    return r

# depth first
def dfs(adj,o):
    return dfs_aux(adj,o,set())

def dfs_aux(adj,o,vis):
    vis.add(o)
    for d in adj[o]:
        if d not in vis:
            dfs_aux(adj,d,vis)
    return vis


#complexidade quadrática na construção do grafo,
#no entanto a parte da travessia está bastante otimizada, só faço 1 travessia por componente
# 100%
def maior(vizinhos):
    if(vizinhos == []):
        return 0
    
    paises = []
    for i in vizinhos:
        for j in i:
            if j not in paises:
                paises.append(j)
    
    mapa = {}
    #construção do grafo
    i=0
    while i < len(vizinhos):
        # caso em que se trata de uma ilha, ou seja, não tem fronteiras
        if(len(vizinhos[i]) == 1):
            mapa[vizinhos[i][0]] = []
        j = 0
        while j < len(vizinhos[i])-1:
            if(vizinhos[i][j] not in mapa):
                mapa[vizinhos[i][j]] = []
            
            if(vizinhos[i][j+1] not in mapa):
                mapa[vizinhos[i][j+1]] = []
            
            if(vizinhos[i][j+1] not in mapa[vizinhos[i][j]]):
                mapa[vizinhos[i][j]].append(vizinhos[i][j+1])
            
            if(vizinhos[i][j] not in mapa[vizinhos[i][j+1]]):
                mapa[vizinhos[i][j+1]].append(vizinhos[i][j])
            
            j+=1
        i+=1
     
    # travessias pelas diferentes componentes
    maior = 1
    for pais in mapa:
        if(pais in paises):
            vis = dfs(mapa, pais)
            if(len(vis) > maior):
                maior = len(vis)
            # removo os países visitados pq fazem parte da mesma componente/continente
            paises = removePaisesVis(vis, paises)
    
    return maior
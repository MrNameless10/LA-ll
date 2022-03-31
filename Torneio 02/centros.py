'''

Neste problema pertende-se calcular quais os vértices centrais
de um grafo pesado não orientado.

A excentricidade de um vértice é a distância desse vértice
ao vértice mais afastado. Os vértices centrais (ou centros) de
um grafo são os que tem excentricidade mínima.

Os vértices do grado são identificados por letras do alfabeto.
O grafo será descrito através de uma sequência de arestas. Cada
aresta é descrita por uma string onde o primeiro e último caracteres
identificam os vértices adjacentes e os digitos no meio o peso da 
respectiva aresta.

A função deverá devolver a lista com todos os centros ordenados
alfabeticamente.

Se o grafo não for ligado deve devolver None.

'''

def build(arestas):
    adj = {}
    for string in arestas:
        o = string[0]
        d = string[-1]
        p = int(string[1:-1])
        if o not in adj:
            adj[o] = {}
        if d not in adj:
            adj[d] = {}
        adj[o][d] = p
        adj[d][o] = p
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

def centros(arestas):
    if arestas == []:
        return None
    adj = build(arestas)
    
    dists = fw(adj)
    
    for x in dists:
        for y in dists[x]:
            if dists[x][y] == float("inf"):
                return None
    
    exc = [(x, max(dists[x].values())) for x in dists]
    
    m = min([x[1] for x in exc])
    
    exc = [x for x,x1 in exc if x1 == m]
    
    exc.sort()
    
    return exc


def build(arestas): 
    adj = {} 
    contador = 1
 
    for string in arestas:
       if string[0] not in adj: 
          adj[string[0]] = {} 
       if string[-1] not in adj: 
          adj[string[-1]] = {}
        
       p = int(string[1:-1])
           

       adj[string[0]][string[-1]] = p  
       adj[string[-1]][string[0]] = p

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

'''
Another solution
'''

def centros(arestas):
    if arestas==[]:
        return []
        
    grafo = build(arestas)
    
    dist = fw(grafo)
    
    l = []
    
    for vertice in dist:
        for verticedois in dist[vertice]:
            if dist[vertice][verticedois] == float("inf"):
                return None
        
        
    l = [(v, max(dist[v].values())) for v in dist]
    
    l.sort(key = lambda t: (t[1],t[0]))
    
    r = [n for n,m in l if m==l[0][1]]

    return r 
    


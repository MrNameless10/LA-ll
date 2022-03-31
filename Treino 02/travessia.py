def adjacentes(ponto, mapa):
    x = ponto[0]
    y = ponto[1]
    l = [(x,y+1), (x,y-1), (x+1,y), (x-1,y)]
    
    return filter(lambda t: t[0]>=0 and t[0]<len(mapa) and t[1]>=0 and t[1]<len(mapa[0]) and abs(int(mapa[t[0]][t[1]])-int(mapa[x][y]))<=2,l)
    

def build(mapa): 
    adj = {} 
 
    for x in range(len(mapa)): 
        for y in range(len(mapa[0])):
            if (x,y) not in adj: 
               adj[(x,y)] = {} 
            for d in adjacentes((x,y), mapa):
               if d not in adj:
                  adj[d] = {}
               adj[(x,y)][d] = 1 + abs(int(mapa[x][y]) - int(mapa[d[0]][d[1]]))
               adj[d][(x,y)] = 1 + abs(int(mapa[x][y]) - int(mapa[d[0]][d[1]]))

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




     
     
def travessia(mapa):
    grafo = build(mapa)
    
    tam = len(mapa)-1
    
    l = []
  
    dist = fw(grafo)
  
    for y in range(len(mapa[0])):
        for p in range(len(mapa[0])):
                l.append((y,  dist[(0,y)][(tam,p)]))
                  
    
    l.sort(key = lambda t: (t[1], t[0]))
    
    return l[0]

'''80 %'''



'''100%'''
   
'''
Implemente uma função que calcula o menor custo de atravessar uma região de
Norte para Sul. O mapa da região é rectangular, dado por uma lista de strings,
onde cada digito representa a altura de cada ponto. Só é possível efectuar 
movimentos na horizontal ou na vertical, e só é possível passar de um ponto
para outro se a diferença de alturas for inferior ou igual a 2, sendo o custo 
desse movimento 1 mais a diferença de alturas. O ponto de partida (na linha
mais a Norte) e o ponto de chegada (na linha mais a Sul) não estão fixados à
partida, devendo a função devolver a coordenada horizontal do melhor
ponto para iniciar a travessia e o respectivo custo. No caso de haver dois pontos
com igual custo, deve devolver a coordenada mais a Oeste.
         MMMM
mapa = ["4563", N
        "9254", N
        "7234", N
        "3231", N
        "3881"] N
travessia(mapa) > (2,10)
         MMMMM
mapa = ["90999", N
        "00000", N
        "92909", N
        "94909"] N
                    
travessia(mapa) > (1,5)
'''

def movimentos(mapa, y, x, N, M, mov, inicio):
    lista = []
    
    dx = [0,-1,1, 0]
    dy = [1, 0,0,-1]
    
    for i in range(4):
        newX = x + dx[i]
        newY = y + dy[i]
        if newX < M and newY < N and newX >= 0 and newY >= 0:
            dif = abs(int(mapa[y][x]) - int(mapa[newY][newX]))
            if dif <= 2:
                lista.append( (newY, newX, mov + 1 + dif, inicio) )
    
    return lista

def travessia(mapa):
    N = len(mapa)
    M = len(mapa[0])
    vis = {}
    orla = []
    for k in range(M):
        orla.append( (0,k,0,k) )
        vis[k] = set()
    result = []
    short = (0, N*M)
    
    for y,x,m,inicio in orla:
        if (x,y) in vis[inicio]:
            continue
        
        vis[inicio].add( (x,y) )
        if y == N-1 and m < short[1]:
            short = (inicio, m)
            
        orla += movimentos(mapa, y, x, N, M, m, inicio)
        
    return short

##########################################################################################
# Exemplo alternativo usando o algoritmo de dijkstra (em teoria deve ser mais eficiente) #
#                         Função movimentos mantém-se igual                              #
##########################################################################################
    
def insert(orla, p): # insert ordenado -> Mete elemento com menor peso (e mais a esquerda) no fim
    y,x,m,inicio = p
    i = 0
    added = False
    
    while i < len(orla) and not added:
        if m > orla[i][2]:
            added = True
            orla.insert(i,p)
        elif m == orla[i][2] and inicio > orla[i][3]:
            added = True
            orla.insert(i,p)
        i+=1
    if not added:
        orla.append(p)
    

def travessia(mapa):
    N = len(mapa)
    M = len(mapa[0])
    vis = {}
    orla = []
    for k in range(M):
        orla.append( (0,k,0,k) )
        vis[k] = set()
    result = []
    short = (0, N*M)
    
    while orla:
        y,x,m,inicio = orla.pop()
        if (x,y) in vis[inicio]:
            continue
        
        vis[inicio].add( (x,y) )
        if y == N-1 and m < short[1]:
            return (inicio, m)
            
        lista = movimentos(mapa, y, x, N, M, m, inicio)
        
        for x in lista:
            insert(orla, x)
        
    return short


'''100%'''

'''
Implemente uma função que calcula o menor custo de atravessar uma região de
Norte para Sul. O mapa da região é rectangular, dado por uma lista de strings,
onde cada digito representa a altura de cada ponto. Só é possível efectuar 
movimentos na horizontal ou na vertical, e só é possível passar de um ponto
para outro se a diferença de alturas for inferior ou igual a 2, sendo o custo 
desse movimento 1 mais a diferença de alturas. O ponto de partida (na linha
mais a Norte) e o ponto de chegada (na linha mais a Sul) não estão fixados à
partida, devendo a função devolver a coordenada horizontal do melhor
ponto para iniciar a travessia e o respectivo custo. No caso de haver dois pontos
com igual custo, deve devolver a coordenada mais a Oeste.
'''
def verifica(mapa, i, j):
    return (0<=i<len(mapa[0]) and 0<=j<len(mapa))

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


def travessia(mapa):
    grafo = {}
    
    for j in range(len(mapa)):
        for i in range(len(mapa[0])):
            if (i,j) not in grafo:
                grafo[(i,j)] = {}
            
            #esquerda
            if(verifica(mapa, i-1, j) == True and abs(int(mapa[j][i]) - int(mapa[j][i-1])) <= 2):
                grafo[(i,j)][(i-1,j)] = 1 + abs(int(mapa[j][i]) - int(mapa[j][i-1]))
            #direita
            if(verifica(mapa, i+1, j) == True and abs(int(mapa[j][i]) - int(mapa[j][i+1])) <= 2):
                grafo[(i,j)][(i+1,j)] = 1 + abs(int(mapa[j][i]) - int(mapa[j][i+1]))
            #cima
            if(verifica(mapa, i, j-1) == True and abs(int(mapa[j][i]) - int(mapa[j-1][i])) <= 2):
                grafo[(i,j)][(i,j-1)] = 1 + abs(int(mapa[j][i]) - int(mapa[j-1][i]))
            #baixo
            if(verifica(mapa, i, j+1) == True and abs(int(mapa[j][i]) - int(mapa[j+1][i])) <= 2):
                grafo[(i,j)][(i,j+1)] = 1 + abs(int(mapa[j][i]) - int(mapa[j+1][i]))
            
    print(grafo)
    
    r = (0,0)
    dists = []
   
    for k in range(len(mapa[0])):
        custos = dijkstra(grafo, (k,0))
        for i in range(len(mapa[0])):
            if (i, len(mapa)-1) in custos:
                dists.append( (k, custos[(i,len(mapa)-1)])  )
        
    
    dists.sort(key = lambda x: (x[1],x[0]))
    print(dists)


    
    return dists[0]

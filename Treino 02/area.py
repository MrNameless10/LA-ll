'''

Implemente uma função que calcula a área de um mapa que é acessível por
um robot a partir de um determinado ponto.
O mapa é quadrado e representado por uma lista de strings, onde um '.' representa
um espaço vazio e um '*' um obstáculo.
O ponto inicial consistirá nas coordenadas horizontal e vertical, medidas a 
partir do canto superior esquerdo.
O robot só consegue movimentar-se na horizontal ou na vertical. 

'''

def adjacentes(ponto, mapa):
    x = ponto[0]
    y = ponto[1]
    tam = len(mapa)
    lista = [(x+1,y), (x-1,y), (x,y-1), (x,y+1)]
    
    
    return filter(lambda t: t[0]>=0 and t[1]>=0 and t[0]<tam and t[1]<tam and mapa[t[1]][t[0]] == '.', lista)
     

def bfs(o,mapa): 
    pai = {} 
    vis = {o} 
    queue = [o] 
 
    while queue: 
       v = queue.pop(0)
       for d in adjacentes(v,mapa): 
           if d not in vis: 
               vis.add(d) 
               pai[d] = v 
               queue.append(d)

    return len(vis)
    
def area(p,mapa):
    r = bfs(p,mapa)
    return r
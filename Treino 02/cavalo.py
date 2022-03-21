'''

O objectivo deste problema é determinar quantos movimentos são necessários para 
movimentar um cavalo num tabuleiro de xadrez entre duas posições.
A função recebe dois pares de coordenadas, que identificam a origem e destino pretendido,
devendo devolver o número mínimo de saltos necessários para atingir o destino a partir da origem.
Assuma que o tabuleiro tem tamanho ilimitado.

'''

def posicoes(ponto):
    return [(ponto[0]+1,ponto[1]+2), (ponto[0]-1,ponto[1]+2), 
            (ponto[0]-2,ponto[1]+1), (ponto[0]-2,ponto[1]-1), 
            (ponto[0]-1,ponto[1]-2), (ponto[0]+1,ponto[1]-2),
            (ponto[0]+2,ponto[1]-1), (ponto[0]+2,ponto[1]+1)]

def bfs(o,k): 
    pai = {} 
    vis = {o} 
    queue = [o] 
    dist = {}
    dist[o] = 0
    
    
    while queue: 
       v = queue.pop(0)
       for d in posicoes(v): 
           if d not in vis: 
               vis.add(d) 
               pai[d] = v 
               dist[d] = dist[v] + 1
               if(d == k):
                   return dist
               queue.append(d)
       

    return dist

def saltos(o,d):
    if(o==d):
        return 0
    dist = bfs(o,d)
    return dist[d]
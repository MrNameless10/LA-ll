'''

Implemente uma função que calcula um dos caminhos mais curtos para atravessar
um labirinto. O mapa do labirinto é quadrado e representado por uma lista 
de strings, onde um ' ' representa um espaço vazio e um '#' um obstáculo.
O ponto de entrada é o canto superior esquerdo e o ponto de saída o canto
inferior direito. A função deve devolver uma string com as instruções para
atravesar o labirinto. As instruções podem ser 'N','S','E','O'.

'''

def adjacentes(ponto, mapa):
    x = ponto[0]
    y = ponto[1]
    
    lista = [(x+1,y), (x-1,y),(x,y+1),(x,y-1)]
    
    return filter(lambda t: t[0] >= 0 and t[1] >= 0 and t[0] < len(mapa) and t[1] < len(mapa) and mapa[t[1]][t[0]] == ' ', lista)
    
    
def bfs(o, mapa): 
    pai = {} 
    vis = {o} 
    queue = [o] 
 
    while queue: 
       v = queue.pop(0)
       for d in adjacentes(v, mapa): 
           if d not in vis: 
               vis.add(d) 
               pai[d] = v 
               queue.append(d)
               

    return pai
    
def caminho(mapa):
    pai = bfs((0,0), mapa) 
    d= (len(mapa)-1, len(mapa)-1)
    caminho = [d] 
    listar = ""
 
    while d in pai: 
       d = pai[d] 
       caminho.insert(0,d)  # 0: posiçao onde quero inserir, d: o que quero inserir 
       
    i = 0
    
    while i<(len(caminho)-1):
        if caminho[i][0] < caminho[i+1][0]:
            listar = listar + "E"
        elif caminho[i][0] > caminho[i+1][0]:
            listar = listar + "O"
        elif caminho[i][1] < caminho[i+1][1]:
            listar = listar + "S"
        elif caminho[i][1] > caminho[i+1][1]:
            listar = listar + "N"
        i+=1
            
    
    return listar
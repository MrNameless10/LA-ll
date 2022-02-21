def tabela(jogos):
    pontos={}
    gols={}
    for e1,g1,e2,g2 in jogos:
        if e1 not in pontos:
            pontos[e1]= 0
            gols[e1]= 0
        if e2 not in pontos:
            pontos[e2]= 0
            gols[e2]= 0
        gols[e1] += (g1-g2)
        gols[e2] += (g2-g1)
        if g1 > g2:
            pontos[e1]+=3
        elif g1 < g2:
            pontos[e2]+=3
        else:
            pontos[e1]+=1
            pontos[e2]+=1

    resultado = list(pontos.items())
    resultado.sort(key = lambda x: (-pontos[x[0]],-gols[x[0]],x[0]))
  
    return resultado
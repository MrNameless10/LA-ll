'''

Implemente uma função que calcula a tabela classificativa de um campeonato de
futebol. A função recebe uma lista de resultados de jogos (tuplo com os nomes das
equipas e os respectivos golos) e deve devolver a tabela classificativa (lista com 
as equipas e respectivos pontos), ordenada decrescentemente pelos pontos. Em
caso de empate neste critério, deve ser usada a diferença entre o número total
de golos marcados e sofridos para desempatar, e, se persistir o empate, o nome
da equipa.

'''

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

def main():
    print("<h3>tabela</h3>")
    jogos = [("Benfica",3,"Porto",2),("Benfica",0,"Sporting",0),("Porto",4,"Benfica",1),("Sporting",2,"Porto",2)]
    print("in:",jogos)
    print("out:",tabela(jogos))

if __name__ == '__main__':
    main()
'''
Podemos usar um (multi) grafo para representar um mapa de uma cidade:
cada nó representa um cruzamento e cada aresta uma rua.
Pretende-se que implemente uma função que lista os cruzamentos de uma cidade
por ordem crescente de criticidade: um cruzamento é tão mais crítico quanto
maior o número de ruas que interliga.
A entrada consistirá numa lista de nomes de ruas (podendo assumir que os nomes de ruas são únicos).
Os identificadores dos cruzamentos correspondem a letras do alfabeto, e cada rua começa (e acaba) no cruzamento
identificado pelo primeiro (e último) caracter do respectivo nome.
A função deverá retornar uma lista com os nomes dos cruzamentos por ordem crescente de criticidade,
listando para cada cruzamento um tuplo com o respectivo identificador e o número de ruas que interliga.
Apenas deverão ser listados os cruzamentos que interliguem alguma rua, e os cruzamentos com o mesmo
nível de criticidade deverão ser listados por ordem alfabética.
'''

def cruzamentos(ruas) :
    crosses = {}

    for street in ruas :
        if street[-1] not in crosses :
            crosses[street[-1]] = 0
        crosses[street[-1]] += 1

        if (street[0] != street[-1]) :
            if street[0] not in crosses :
                crosses[street[0]] = 0
            crosses[street[0]] += 1

    l = list(crosses.items())
    l.sort(key = lambda x : (x[1],x[0]))

    return l

def main():
    print("<h3>cruzamentos</h3>")
    ruas = ["raio","central","liberdade","chaos","saovictor","saovicente","saodomingos","souto","capelistas","anjo","taxa"]
    print("in:",ruas)
    print("out:",cruzamentos(ruas))

if __name__ == '__main__':
    main()
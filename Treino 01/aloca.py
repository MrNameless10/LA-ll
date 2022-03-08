"""

Implemente uma função que dado um dicionário com as preferências dos alunos
por projectos (para cada aluno uma lista de identificadores de projecto, 
por ordem de preferência), aloca esses alunos aos projectos. A alocação
é feita por ordem de número de aluno, e cada projecto só pode ser feito
por um aluno. A função deve devolver a lista com os alunos que não ficaram
alocados a nenhum projecto, ordenada por ordem de número de aluno.

"""

def aloca(prefs):
  alocados=[]
  repetidos = []
  numeros = [x for x in prefs.keys()]
  numeros.sort()
  for aluno in numeros:
    preferencias = prefs[aluno]
    alocado= False
    for p in preferencias:
      if p not in alocados:
        alocados.append(p)
        alocado = True
        break
    if not alocado:
        repetidos.append(aluno)
  return repetidos


def main():
    print("<h3>aloca</h3>")
    prefs = {10885:[1,5],40000:[5],10000:[1,2]}
    print("in:",prefs)
    print("out:",aloca(prefs))

if __name__ == '__main__':
    main()
'''
Implemente uma função que calcula o horário de uma turma de alunos.
A função recebe dois dicionários, o primeiro associa a cada UC o
respectivo horário (um triplo com dia da semana, hora de início e
duração) e o segundo associa a cada aluno o conjunto das UCs em
que está inscrito.
A função deve devolver uma lista com os alunos que
conseguem frequentar todas as UCs em que estão inscritos, indicando
para cada um desses alunos o respecto número e o número total de horas
semanais de aulas.
Esta lista deve estar ordenada por ordem decrescente
de horas e, para horas idênticas, por ordem crescente de número.

@carricossauro
'''

def cabe(hora, uc): # 1 aula, outra aula
    res = True
    a = (hora[1],hora[1]+hora[2])
    b = (uc[1],uc[1]+uc[2])
    
    if a[0] <= b[0] < a[1]: # b começa a meio de a 
        res = False
    elif b[0] <= a[0] < b[1]: # a começa a meio de b
        res = False
    
    return res

def horario(ucs,alunos):
    result = []
    horarios = {}
    
    for aluno in alunos:
        if aluno not in horarios:
            horarios[aluno] = []
            
        for cad in alunos[aluno]:
            possivel = True
            if cad not in ucs:
                possivel = False
            
            for hora in horarios[aluno]:
                if cad in ucs and hora[0] == ucs[cad][0]: # dia da semana
                    if not cabe(hora, ucs[cad]):
                        possivel = False
            if possivel:
                horarios[aluno].append((ucs[cad][0],ucs[cad][1],ucs[cad][2]))
                
        if len(horarios[aluno]) == len(alunos[aluno]):
            result.append(aluno)
    
    resultado = []
    for aluno in result:
        horas = 0
        for x in horarios[aluno]:
            horas+=x[2]
        resultado.append((aluno, horas))
    
    resultado.sort(key=lambda x: (-x[1], x[0]))
    
    return resultado


def main():
    print("<h4>horario</h4>")
    ucs = {"la2": ("quarta",16,2), "pi": ("terca",15,1), "cp": ("terca",14,2),"so": ("quinta",9,3)}
    alunos = {5000: {"la2","cp"}, 2000: {"la2","cp","pi"},3000: {"cp","poo"}, 1000: {"la2","cp","so"}}
    print(horario(ucs,alunos))

if __name__ == '__main__':
    main()

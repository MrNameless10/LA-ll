'''
Pretende-se que implemente uma função que detecte códigos ISBN inválidos. 
Um código ISBN é constituído por 13 digitos, sendo o último um digito de controlo.
Este digito de controlo é escolhido de tal forma que a soma de todos os digitos, 
cada um multiplicado por um peso que é alternadamente 1 ou 3, seja um múltiplo de 10.
A função recebe um dicionário que associa livros a ISBNs,
e deverá devolver a lista ordenada de todos os livros com ISBNs inválidos.
'''

def isbn(livros):
    l = []
        
    for livro in livros:
        i = 0
        soma = 0
        for digito in livros[livro]:
            if(i%2 == 0):
                soma += int(digito)
            else:
                soma += int(digito) * 3
            i += 1
        if (soma%10 != 0):
            l.append(livro)
              
        
    return sorted(l)

def main():
    print("<h3>isbn</h3>")
    livros = {
        "Todos os nomes":"9789720047572",
        "Ensaio sobre a cegueira":"9789896604011",
        "Memorial do convent":"9789720046711",
        "Os cus de Judas":"9789722036757"
    }
    print("in:",livros)
    print("out:",isbn(livros))

if __name__ == '__main__':
    main()
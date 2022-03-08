"""

Implemente uma função que formata um programa em C.
O código será fornecido numa única linha e deverá introduzir
um '\n' após cada ';', '{', ou '}' (com excepção da última linha).
No caso do '{' as instruções seguintes deverão também estar identadas
2 espaços para a direita.

"""

def formata(codigo):
    tempArray=[]
    previous = "s"
    between=False
    for i in range(len(codigo)):
        if((previous!=" " and codigo[i]!=" ") or (previous==" " and codigo[i]!=" ") or (previous!=" " and codigo[i]==" " and codigo[i+1]!=" ")):
            tempArray.append(codigo[i])
        previous=codigo[i]
        if((codigo[i]=="{")):
            between=True
            tempArray.append("\n")
            tempArray.append("  ")
        if(codigo[i]=="}"):
            between=False
            break
        if((codigo[i]==";")):
            if((i)!=(len(codigo))):
                if((i+1==len(codigo))):
                    break
                tempArray.append("\n")
            if(between and codigo[i+1]!="}"):
                tempArray.append("  ")
    return (''.join(tempArray))


def main():
    print("<h4>formata</h4>")
    codigo = "int x;x=0;x=x+1;"
    print(formata(codigo))

if __name__ == '__main__':
    main()


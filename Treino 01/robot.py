'''
Neste problema prentede-se que implemente uma função que calcula o rectângulo onde se movimenta um robot.

Inicialmente o robot encontra-se na posição (0,0) virado para cima e irá receber uma sequência de comandos numa string.
Existem quatro tipos de comandos que o robot reconhece:
  'A' - avançar na direcção para o qual está virado
  'E' - virar-se 90º para a esquerda
  'D' - virar-se 90º para a direita 
  'H' - parar e regressar à posição inicial virado para cima
  
Quando o robot recebe o comando 'H' devem ser guardadas as 4 coordenadas (minímo no eixo dos X, mínimo no eixo dos Y, máximo no eixo dos X, máximo no eixo dos Y) que definem o rectângulo 
onde se movimentou desde o início da sequência de comandos ou desde o último comando 'H'.

A função deve retornar a lista de todas os rectangulos (tuplos com 4 inteiros)
'''


def robot(comandos):
    lista = []
    virado = 0
    pos = [0,0]
    caminho = []
    
    for comando in comandos:
        caminho.append(tuple(pos))
        if comando == 'A':
            if virado == 0:
                pos[1] = pos[1] + 1
            elif virado == 1:
                pos[0] = pos[0] + 1
            elif virado == 2:
                pos[1] = pos[1] - 1
            else:
                pos[0] = pos[0] - 1
                
            
        elif comando == 'E':
            if virado == 0:
                virado = 3
            else:
                virado -= 1
            
            
        elif comando == 'D':
            if virado == 3:
                virado = 0
            else:
                virado += 1
            
        
        elif comando == 'H':
            pos = [0,0]
            virado = 0
            lista.append((min([x[0] for x in caminho]),
                          min([x[1] for x in caminho]),
                          max([x[0] for x in caminho]),
                          max([x[1] for x in caminho])))
            caminho = []
                   
    return lista


def main():
    print("<h3>robot</h3>")
    cs = "EEAADAAAAAADAAAADDDAAAHAAAH"
    print("in:",cs)
    print("out:",robot(cs))

if __name__ == '__main__':
    main()
'''

O objectivo deste problema é descobir um quadrado latino. Um quadrado latino
de dimensão N é preenchido com número entre 1 e N, não podendo ter números
repetidos em nenhuma linha nem em nenhuma coluna.
Irá receber um quadrado parcialmente preenchido, representado como uma lista
de linhas, onde um 0 representa uma posição ainda não preenchida.
A função deverá prencher as posições com 0 por forma a obter um quadrado
latino. Assuma que tal é sempre possível.
Se houver mais do que um quadrado possível então deverá devolver o menor em
ordem lexicográfica.

'''
def complete(quadrado, N, linha, coluna):
    return linha > N - 1
    
def valid(quadrado, N):
    for i in range(N):
        l = quadrado[i]
        s = set(l)
        if len(l) != len(set(s)):
            return False
        c = [x[i] for x in quadrado]
        s = set(c)
        if len(c) != len(set(s)):
            return False
    return True
    
def extensions(quadrado, linha, coluna, N):
    listaLinha = quadrado[linha]
    listaColuna = [l[coluna] for l in quadrado]
    
    return [x for x in range(1, N+1) if x not in listaLinha and x not in listaColuna]

def proxPos(N, linha, coluna):
    if coluna == N - 1:
        return linha+1, 0
    return linha, coluna + 1

def aux(quadrado, linha, coluna, N):
    if complete(quadrado, N, linha, coluna):
        return valid(quadrado, N)
    l, c = proxPos(N, linha, coluna)
    
    if quadrado[linha][coluna] != 0:
        return aux(quadrado, l, c, N)
        
    for x in extensions(quadrado, linha, coluna, N):
        quadrado[linha][coluna] = x
        if aux(quadrado, l, c, N):
            return True
        quadrado[linha][coluna] = 0
        
    return False
    

def quadrado(q):
    aux(q, 0, 0, len(q))
    return q


'''
##
# Main function of the Python program.
#
##

from quadrado import quadrado

def mostra(q):
    return '\n'.join(map(str,q))

def main():
    print("<h3>quadrado</h3>")
    q = [[3,0,0],[0,0,0],[0,1,0]]
    print("in:\n"+mostra(q))
    print("out:\n"+mostra(quadrado(q)))

    
if __name__ == '__main__':
    main()
'''

'''
##
#
# All tests in the folder "test" are executed
# when the "Test" action is invoked.
#
##

from Root.src.quadrado import quadrado
import unittest

class quadradoTest(unittest.TestCase):

    def test_quadrado_1(self):
        with test_timeout(self,1):
            q = [[3,0,0],[0,0,0],[0,1,0]]
            self.assertEqual(quadrado(q),[[3, 2, 1], [1, 3, 2], [2, 1, 3]])

    def test_quadrado_2(self):
        with test_timeout(self,1):
            q = [[0,1],[0,0]]
            self.assertEqual(quadrado(q),[[2, 1], [1, 2]])

            
if __name__ == '__main__':
    unittest.main()

import time
import signal

class TestTimeout(Exception):
    pass

class test_timeout:
  def __init__(self, test, seconds, error_message=None):
    if error_message is None:
      error_message = 'test timed out after {}s.'.format(seconds)
    self.seconds = seconds
    self.error_message = error_message
    self.test = test

  def handle_timeout(self, signum, frame):
    raise TestTimeout(self.error_message)

  def __enter__(self):
    signal.signal(signal.SIGALRM, self.handle_timeout)
    signal.alarm(self.seconds)

  def __exit__(self, exc_type, exc_val, exc_tb):
    signal.alarm(0)
    if exc_type is not None and exc_type is not AssertionError:
        self.test.fail("execution error")

'''
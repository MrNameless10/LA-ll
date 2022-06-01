'''

Suponha que tem um baralho de cartas onde cada carta tem duas palavras, uma
escrita na parte de cima da carta, outra na parte de baixo. Assuma que tem
um stock infinito de cada carta. Implemente uma função que dado um baralho,
descrito como uma lista de pares de strings, determine a menor sequência de 
cartas tal que, quando colocadas lado a lado, a frase na parte de cima seja
igual à frase na parte de baixo. A sequência de cartas deve ser identificada
pelas respectivas posições no baralho. Caso haja mais do que uma sequência
óptima deve devolver a menor em ordem lexicográfica (ou seja, dando preferência
às cartas que aparecem primeiro).

Por exemplo se o baralho tiver as cartas

a    ab   bba
---  ---  ---
baa  aa   bb

a melhor solução seria

bba  ab   bba  a
---  ---  ---  ---
bb   aa   bb   baa

correspondente à frase bbaabbbaa. 

Este baralho ser´á representado pela lista [('a','baa'),('ab','aa'),('bba','bb')]
e a solução pela lista das posições das cartas no baralho, ou seja, [3,2,3,1].

'''


#######
# 50% #
#######
def valid(cartas, sequencia):
    s1 = ""
    s2 = ""
    for x in sequencia:
        a, b = cartas[x]
        s1 += a
        s2 += b
    return s1 == s2
    
def complete(cartas, sequencia, k):
    return len(sequencia) == k
    
def extensions(cartas, sequencia, ordenada):
    return ordenada
    
def aux(cartas, sequencia, k, ordenada):
    if complete(cartas, sequencia, k):
        return valid(cartas, sequencia)
    for x in extensions(cartas, sequencia, ordenada):
        sequencia.append(x)
        if aux(cartas, sequencia, k, ordenada):
            return True
        sequencia.pop()
    return False

def jogo(cartas):
    ordenada = [x for x in range(len(cartas))]
    ordenada.sort()
    sequencia = []
    k = 1
    if cartas == []:
        return []
    while 1:
        if aux(cartas, sequencia, k, ordenada):
            res = [x+1 for x in sequencia]
            return res
        k += 1


'''
##
# Main function of the Python program.
#
##

from jogo import jogo

def main():
    print("<h3>jogo</h3>")
    cartas = [('a','baa'),('ab','aa'),('bba','bb')]
    print("in:",cartas)
    print("out:",jogo(cartas))

    
if __name__ == '__main__':
    main()


##
#
# All tests in the folder "test" are executed
# when the "Test" action is invoked.
#
##

from Root.src.jogo import jogo
import unittest

class jogoTest(unittest.TestCase):

    def test_jogo_1(self):
        with test_timeout(self,1):
            cartas = [('a','baa'),('ab','aa'),('bba','bb')]
            self.assertEqual(jogo(cartas),[3, 2, 3, 1])

    def test_jogo_2(self):
        with test_timeout(self,1):
            cartas = [('c','bc'),('bb','b'),('ab','ba')]
            self.assertEqual(jogo(cartas),[2, 1])

            
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
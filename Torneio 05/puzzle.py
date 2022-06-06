'''

Num popular puzzle aritmético é dada uma expressão onde onde letras 
aparecem em vez de digitos, sendo o objectivo descobrir qual os números
envolvidos. Cada letra corresponde a um digito diferente e os digitos mais
significativos não podem ser 0. Por exemplo se a expressão for TO+GO=OUT,
a expressão pode ser 21+81=102, correspondente a substituir o T por 2, 
o O por 1, o G por 8 e o U por 0. Obviamente, no máximo a expressão terá 10
letras diferentes.
Implemente uma função que dado uma string com a expressão do puzzle
devolva a sequência de digitos correspondente à sequência ordenada de letras
do puzzle. No caso acima, a string ordenada 
com todas as letras é "GOTU", pelo que deverá ser devolvida a string "8120".
Se houver mais do que um possível resultado, deverá devolver o menor.

'''

def complete(ipt, dic):
    for number in dic.values():
        if number == -1:
            return False
    return True

def extensions(ipt, dic):
    nextLetter = [x for x in sorted(dic.keys()) if dic[x] == -1][0]
    return [(nextLetter, str(x)) for x in range(10) if str(x) not in dic.values()]

def valid(ipt, dic):
    numbers = []
    res = -1
    string = ""
    for pos, c in enumerate(ipt):
        if c == "+":
            numbers.append(int(string))
            string = ""
        elif c == "=":
            numbers.append(int(string))
            res = int("".join(map(lambda x: dic[x],ipt[pos+1:])))
            break
        else:
            string += dic[c]
            
    return sum(numbers) == res

def aux(ipt, dic):
    if complete(ipt, dic):
        return valid(ipt, dic)
    for i,x in extensions(ipt, dic):
        dic[i] = x
        if aux(ipt, dic):
            return True
        dic[i] = -1
    
    return False

def puzzle(p):
    dic = {}
    for c in p:
        if c not in ["+", "="]:
            dic[c] = -1
    res = aux(p, dic)
    print(dic.items())
    return "".join(map(lambda x: dic[x], sorted(dic.keys())))

##
# Main function of the Python program.
#
##

from puzzle import puzzle

def main():
    print("<h3>puzzle</h3>")
    p = "TO+GO=OUT"
    print("in: ",p)
    print("out:",puzzle(p))
    
if __name__ == '__main__':
    main()

##
#
# All tests in the folder "test" are executed
# when the "Test" action is invoked.
#
##

from Root.src.puzzle import puzzle
import unittest

class puzzleTest(unittest.TestCase):

    def test_puzzle_0(self):
        with test_timeout(self,1):
            self.assertEqual(puzzle("TO+GO=OUT"), "8120")

    def test_puzzle_1(self):
        with test_timeout(self,1):
            self.assertEqual(puzzle("AB+BA=CC"), "123")

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

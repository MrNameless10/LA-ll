'''

Neste problema pretende-se que implemente uma função que calcula quantas
ilhas existem num mapa.

O mapa é rectangular e definido por uma lista de strings de igual comprimento,
onde um caracter '#' marca uma quadrícula com terra e um ' ' uma quadrícula com 
mar. A função deve devolver o n´úmero de ilhas no mapa.

'''

def adjacentes(ponto, mapa):
    x = ponto[0]
    y = ponto[1]
    lista = [(x+1,y), (x,y-1), (x-1,y), (x, y+1)]
    
    return list(    filter(lambda t: (t[0] >= 0 and t[1] >= 0 and t[0] < len(mapa) and t[1] < len(mapa[0]) and mapa[t[0]][t[1]] == '#')    ,lista))
    

def individuais(mapa):
    
    
    cont = 0
    
    for x in range(len(mapa)): 
        for y in range(len(mapa[0])):
            if mapa[x][y] == '#' and adjacentes((x,y),mapa) == []:
                cont+=1
                
    
    return cont
                
                

def build(mapa): 
   adj = {}
   
   

   for x in range(len(mapa)): 
        for y in range(len(mapa[0])):
            if mapa[x][y] == '#':
                for adjacente in adjacentes((x,y), mapa):
                  if (x,y) not in adj: 
                    adj[(x,y)] = set()  #set() cria um conjunto vazio 
                  if adjacente not in adj:
                    adj[adjacente] = set()
               
                  adj[(x,y)].add(adjacente) 
                  adj[adjacente].add((x,y))
            
      
   return adj
   
   
def bfs(adj,o, c, vis, comp): 
    pai = {} 
    vis.add(o)
    queue = [o] 
    comp[o] = c
 
    while queue: 
       v = queue.pop(0)
       for d in adj[v]: 
           if d not in vis: 
               vis.add(d) 
               pai[d] = v 
               queue.append(d)
               comp[d] = c

    return pai 

   
def ilhas(mapa):
    
    adj = build(mapa)
  
    c = 1
    vis = set()
    comp = {}
    
    for vertice in adj:
        if vertice not in vis:
            bfs(adj, vertice, c, vis, comp)
            c+=1
    
    c-=1
    
    inc = individuais(mapa)
    c += inc
    
  
    
    return c

##
# Main function of the Python program.
#
##

from ilhas import ilhas

def main():
    print("<h3>ilhas</h3>")
    mapa = ["## ###",
            "## #  ",
            "#  #  ",
            "      ",
            "   ###"]
    print("in:")
    print('\n'.join(mapa))
    print("out:",ilhas(mapa))
    
if __name__ == '__main__':
    main()

##
#
# All tests in the folder "test" are executed
# when the "Test" action is invoked.
#
##

from Root.src.ilhas import ilhas
import unittest

class ilhasTest(unittest.TestCase):

    def test_ilhas_0(self):
        with test_timeout(self,1):
            mapa = ["## ###",
                    "## #  ",
                    "#  #  ",
                    "      ",
                    "   ###"]
            self.assertEqual(ilhas(mapa), 3)

    def test_ilhas_1(self):
        with test_timeout(self,1):
            mapa = ["## ###",
                    "####  ",
                    "#  #  ",
                    "###   ",
                    "   ###"]
            self.assertEqual(ilhas(mapa), 2)


            
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

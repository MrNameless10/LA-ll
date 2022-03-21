def diferentes(frases):
    d = {}
    
    for string in frases:
       aux = []
       for caracter in string:
           if caracter not in aux:
               aux.append(caracter)
       d[string] = len(aux)   
               
    frases.sort(key = lambda x: (-d[x], x ))           
    return frases
def formula1(log):
    d = {} 
    l = []
    minn = {}
    
    if log==[]:
        return []
        
    log.sort(key=lambda x: (x[1], x[0]))
    
    for (tempo,nome) in log:
        d[nome] = []
    
    for (tempo,nome) in log:
        
        d[nome].append(tempo)
    
    
    for pessoa in d:
        if(len(d[pessoa]) == 1):
           minn[pessoa] = d[pessoa][0]
        else:
           minn[pessoa] = 100
           for i in range(len(d[pessoa])-1):
              if(   ((d[pessoa][i+1]) - d[pessoa][i]) < minn[pessoa]):
                 minn[pessoa] = (d[pessoa][i+1] - d[pessoa][i])
  
   
   
   
    minval = min(minn.values())
    l = [k for k,v in minn.items() if v==minval]
        

    return sorted(l)
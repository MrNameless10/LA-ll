def aloca(prefs):
  alocados=[]
  repetidos = []
  numeros = [x for x in prefs.keys()]
  numeros.sort()
  for aluno in numeros:
    preferencias = prefs[aluno]
    alocado= False
    for p in preferencias:
      if p not in alocados:
        alocados.append(p)
        alocado = True
        break
    if not alocado:
        repetidos.append(aluno)
  return repetidos
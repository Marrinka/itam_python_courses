slovar = {}
def function(l):
    for el in l:
        if type(el) is list:
            slovar.update(function(el))
        else:
            for s in el:
                if s in slovar:
                    slovar[s] += 1
                else:
                    slovar[s] = 1
    return slovar


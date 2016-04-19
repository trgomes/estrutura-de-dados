def calcular_frequencias(s):
    dic={}
    for a in s:
        if a in dic.keys():
            dic[a]+=1
        else:
            dic[a]=1
    return dic

s = 'aaabbc'
print(calcular_frequencias(s))


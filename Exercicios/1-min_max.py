# -*- coding: utf-8 -*-

def max_min(seq):

    if(len(seq) == 1):
        maior = seq[0]
    else:

        maior = max_min(seq[0:len(seq)-1])

        if maior > seq[len(seq)-1]:
            maior = maior
        else:
            maior = seq[len(seq)-1]

    return maior


seq = [5,2,4,8,3,15,6,20]

print (len(seq))

print('\n')


#tpl = (seq, len(seq))

#max, min = max_min(*tpl)

#print(max, min)

print(max_min(seq))














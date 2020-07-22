#!/usr/bin/python3

txt = '''PBFPVYFBQXZTYFPBFEQJHDXXQVAPTPQJKTOYQWIPBVWLXTOXBTFXQWAXBVCXQWAXFQJVWLEQN
TOZQGGQLFXQWAKVWLXQWAEBIPBFXFQVXGTVJVWLBTPQWAEBFPBFHCVLXBQUFEVWLXGDPEQVPQGV
PPBFTIXPFHXZHVFAGFOTHFEFBQUFTDHZBQPOTHXTYFTODXQHFTDPTOGHFQPBQWAQJJTODXQHFOQ
PWTBDHHIXQVAPBFZQHCFWPFHPBFIPBQWKFABVYYDZBOTHPBQPQJTQOTOGHFQAPBFEQJHDXXQVAV
XEBQPEFZBVFOJIWFFACFCCFHQWAUVWFLQHGFXVAFXQHFUFHILTTAVWAFFAWTEVOITDHFHFQAITI
XPFHXAFQHEFZQWGFLVWPTOFFA'''
letterFrequency = {'E' : 12.0, 'T' : 9.10, 'A' : 8.12, 'O' : 7.68, 'I' : 7.31,
'N' : 6.95, 'S' : 6.28, 'R' : 6.02, 'H' : 5.92, 'D' : 4.32, 'L' : 3.98, 'U' : 2.88,
'C' : 2.71, 'M' : 2.61, 'F' : 2.30, 'Y' : 2.11, 'W' : 2.09, 'G' : 2.03, 'P' : 1.82,
'B' : 1.49, 'V' : 1.11, 'K' : 0.69, 'X' : 0.17, 'Q' : 0.11, 'J' : 0.10, 'Z' : 0.07 }
dct = {}
for i in txt:
    dct[i] = dct.get(i, 0) + 1
    
lst_txt = [(v, k) for k, v in dct.items()]
lst_fr_en_lett = [(v, k) for k, v in letterFrequency.items()]
lst_txt.sort(reverse = True)    
lst_fr_en_lett.sort(reverse = True)

#for i in lst_txt:
#    print(i)
#for f in lst_fr_en_lett:
#    print(f)

n = 1
lst_ltr = []
for fr, let in lst_txt:
    #print(let, lst_fr_en_lett[n-1][1])
    n +=1
    lst_ltr.append((let, lst_fr_en_lett[n-1][1]))
#for i in lst_ltr:
#    print(i)
dct_ltr ={}

for k, v in lst_ltr:
    dct_ltr[k] = v
    
for i in txt:
    i = dct_ltr[i]
    print(i)

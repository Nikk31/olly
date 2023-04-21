# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 09:29:06 2023

@author: kusha
"""

data=[['Sunny','Warm','Normal','Strong','Warm','Same','Yes'],
      ['Sunny','Warm','High','Strong','Warm','Same','Yes'],
      ['Rainy','Cold','High','Strong','Warm','Change','No'],
      ['Sunny','Warm','High','Strong','Cool','Change','Yes']]



gen_hypo=[['?' for i in range(len(data[0])-1)] for j in range(len(data[0])-1)]
spec_hypo=['Null' for i in range(len(data[0])-1)]

for i in range(len(data)):
    if data[i][-1]=='Yes':
        for j in range(len(data[i])-1):
            if spec_hypo[j]=='Null':
                spec_hypo[j]=data[i][j]
            elif spec_hypo[j]==data[i][j]:
                pass
            else:
                spec_hypo[j]='?'
    else:
        for j in range(len(gen_hypo)):
            if spec_hypo[j]!=data[i][j]:
                gen_hypo[j][j]=spec_hypo[j]
            else:
                gen_hypo[j][j]='?'
            

    print(spec_hypo)
    print(gen_hypo)
    print()

for k in range(len(gen_hypo)):
    if gen_hypo[k][k]!=spec_hypo[k]:
        gen_hypo[k][k]='?'


indices = [i for i, val in enumerate(gen_hypo) if val == ['?' for j in range(len(data[0])-1)]]
for i in indices:
    gen_hypo.remove(['?' for i in range(len(data[0])-1)])

print("Final values: ")
print("\nSpecific hypothesis:")
print(spec_hypo)
print("\nGeneral hypothesis:")
print(gen_hypo)

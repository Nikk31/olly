# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 10:10:54 2023

@author: kusha
"""

data=[['Sunny','Warm','Normal','Strong','Warm','Same','Yes'],
      ['Sunny','Warm','High','Strong','Warm','Same','Yes'],
      ['Rainy','Cold','High','Strong','Warm','Change','No'],
      ['Sunny','Warm','High','Strong','Cool','Change','Yes']]

gen_hypo=[['?' for i in range(len(data[0])-1)] for j in range(len(data))]
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
    print(spec_hypo)
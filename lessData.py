from random import *

n = 0
c = 0
meuArquivo = open('0.02_ENEM.csv', 'w')

with open('ENEM_data_for_modeling_3.csv',encoding="utf-8") as f:
    for line in f:
        if n == 0:
            meuArquivo.write(line)
            n = 1
        elif(random()>0.90):
            meuArquivo.write(line)
            c += 1

meuArquivo.close()

print(c)
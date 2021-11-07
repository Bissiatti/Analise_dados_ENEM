import lightgbm as lgb
import sys


model1 = lgb.Booster(model_file='modelMean.txt')
model2 = lgb.Booster(model_file='modelRedacao.txt')


x = sys.argv[1]

x = x.split(',')

i = 0
while i < len(x):
    x[i] = float(x[i])
    i += 1


#x = [21, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0.2, 0, 0, 0, 0, 0, 0, 0.2, 0, 0, 0, 0, 0, 0, 0, 0] #exemplo do vetor x de entrada.

y1 = model1.predict([x])

y2 = model2.predict([x])

y= [y1[0],y2[0]]
print(y)

import numpy as np
import matplotlib.pyplot as plt

x = "Yab Gab to Trab Yab Yab Aeiouz"

y = x.lower()
print('Y: ' + y)
const = len(y)
print('const: ' + str(const))
print('range: ' + str(list(range(const-1,-1,-1))))
for i in range(const-1,-1,-1):
  print('iteration: ' + str(i))
  print('y(i): ' + y[i])
  if y[i] in "aeiou":
    print('Detected! ')
    y = y.replace(y[i],'')
    print('New y: ' + y)

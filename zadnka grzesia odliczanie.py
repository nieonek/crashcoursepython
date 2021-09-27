
import sys
import time
from IPython.display import clear_output

y=x
for i in range (0,101):
    y=y*2
    clear_output(wait=True)
    for j in range(0,i):
        print('*', end='') #end='' powoduje ze nie przechodzimy do nastepnej linii
    for j in range(i,100):
        print('_', end='')
    print(f" {i}%")
    time.sleep(0.01)
print("Done!")
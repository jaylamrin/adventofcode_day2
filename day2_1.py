import numpy as np

fn = './day2 1202.txt'
x = np.loadtxt(fn, delimiter=',')
print(x)

for i in range(0, len(x), 4):
    #    print(x[i], len(x))
    a, b, c, y = 0, 0, 0, 0
    if x[i] == 1:
        a = x[int(x[i+1])]
        b = x[int(x[i+2])]
        c = int(a + b)
        y = int(x[i+3])
        x[y] = c
#        print(f'1 : {x[y]}')
    elif x[i] == 2:
        a = x[int(x[i+1])]
        b = x[int(x[i+2])]
        c = int(a * b)
        y = int(x[i+3])
        x[y] = c
#        print(f'2 : {x[y]}')
    elif x[i] == 99:
        break
print(x.astype(int))

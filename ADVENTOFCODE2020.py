import numpy

data = numpy.loadtxt("day1a.txt", delimiter=",")

for price in data:
    if (2020 - price) in data:
        print(price * (2020-price))
        break


#czesc druga teraz 3 a nie 2 liczby
data = numpy.sort(data)

# data = [1721,979,366,299,675,1456]

x =0
y =0
z =0
for i in range(len(data)-1):
    x=data[i]
    for j in range(len(data)-1):
        y=data[j]
        for k in range(len(data)-1):
            z = data[k]
            if k != i and k != j and i != j:
                if x+y+z == 2020:
                    print(x*y*z)
                    break

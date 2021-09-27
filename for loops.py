for x in range (5):
    print(x)

def square(n):
    return n*n
def sum_squares(x):
    sum = 0
    for n in range(x):
        sum += square(n)
    return sum

print(sum_squares(10))

friends = ['Janek' , 'Zenek', 'Misiek']
for friend in friends:
    print('Hi ' + str(friends))

values = [23, 52, 59, 37, 48]
sum = 0
length = 0
for value in values:
    sum += value
    length += 1
print ('total sum: ' + str(sum) + '-Average: ' + str(sum/length))

for y in range(8):
    if (y > 2) and (y<6):
        print (y)

        #test quiz for loops

#def factorial(n):
#result = 1
#for i in ___:
#    __
#return result
#
#print(factorial(4)) # should return 24
#print(factorial(5)) # should return 120

def factorial(n):
    result = 1
    for i in range(1,n+1):
        result = result * i
    return result

print(factorial(4)) # should return 24
print(factorial(5)) # should return 120



def to_celsius(x):
    return (x-32)*5/9

# 3cia liczba in range to "co ile/skok" increment
for x in range(0,101,10):
    print(x, to_celsius(x))


for left in range(7):
    for right in range (left,7):
        print("[" + str(left) + "|" + str(right) + "]", end=" ") #o co kaman z tym END?

teams = ['wilki', 'pandy', 'misie', 'koale']
for home_team in teams:
    for away_team in teams:
        if home_team != away_team:
            print (home_team + " vs " + away_team)

for x in range(25):
    print(x)

def koledzy(imie):              #caly czas nie lapie do konca jak idzie logika 73->74-->75
    for kolega in imie:
        print ("czesc " + kolega)

koledzy(['Jan', 'Ania', 'Zenek'])
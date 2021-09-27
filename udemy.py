print('How many cats do you have?')
numbercats=input()
try:
    if int(numbercats)>=4:
        print('A lot of cats')
    elif int(numbercats)>=0:
        print('Not that many cats')
    else:
        print('You cant have negative amount of cats')
except ValueError:
    print('enter a number in digits')
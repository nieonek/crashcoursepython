
print("Chcesz dodac, odjac, pomnozyc czy podzielic?")
print("jesli chcesz dodawac wybierz 1")
print("jesli chcesz odejmowac wybierz 2")
print("jesli chcesz mnozyc wybierz 3")
print("jesli chcesz dzielic wybierz 4")
input():
    if input==1:
        znak="+"
    if input==2:
        znak="-"
    if input==3:
        znak="*"
    if input==4:
        znak="/"
    else:
        print("wybierz jeszcze raz")
        input()
print("Pierwsza liczba to: ")
    input(liczba1)
print("Druga liczba to: ")
    input(liczba2)
print("Twoj wynik to: " + (liczba1 + int(znak) + liczba2))

import shutil
import psutil

print(psutil.cpu_percent(0.1))
print(psutil.cpu_percent(1))

def check_disk_usage(disk):
    diskusage = shutil.disk_usage(disk)
    free = diskusage.free / diskusage.total * 100
    return free > 20

def check_cpu_usage():
    usage = psutil.cpu_percent(1)
    return usage < 75

if not check_disk_usage("/") or check_cpu_usage():
    print("ERROR!")
else:
    print("everything is ok")

print(file.readline())  #czyta 1 linijke(za kazdym razem kolejna)
print(file.read())  #czyta cala zawartosc pliku read zaczyna od aktualnej linijki tak jak readline
file.close()   #dobrze zamknac plik, bo jest np limit dost file descriptorow

with open("plik.txt") as file:
    print(file.readline())        #uzywaja WITH python automatycznie CLOSEuje plik


#Iterowanie po plikach

with open("tekst.txt") as file:
    for line in file:
        print(line.upper())   #teraz wydrukuje z linijka przerwy pomiedzy linijami

with open("tekst.txt") as file:
    for line in file:
        print(line.strip().upper())   #tak usunelismy puste linijki

file = open("text.txt")    #tak z linesow robimy liste line-ow
lines = file.readlines()
file.close()
lines.sort()
print(lines)


with open("text.txt", "w") as file:         # W oznacza write only np R to read only(i jest defaultowe)
    file.write("It was a dar and stormy night")   # w tworzy plik jesli go nie ma, otworzenie pliku za pomoca w gdy juz istnieje kasuje jego stara zawartosc
                                                    # a append  r+ read-write

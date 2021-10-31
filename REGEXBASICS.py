log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
index = log.index ("[")
print(log[index+1:index+6])
#>>>>>12345

import re
regex = r"\[(\d+)\]"
result = re.search(regex, log)
print(result[1])

result=re.search(r"aza", "plaza")
print(result)    # r - RAWSTRING

result=re.search(r"^x", "xenon")
print(result)

result=re.search(r"n$", "xenon")
print(result)

result=re.search(r"p..g", "penguin")
print(result)

print(re.search(r"^x", "Xenon", re.IGNORECASE))  #IGNORECASE zbey nie rozroznial duzych i malych

print(re.search(r"[aA-zZ]ython", "Is python or Python worth it?"))   # To co jest w [] to character class

print(re.search(r"[aA-zZ]way", "This is the end of the highway"))  # => <re.Match object; span=(26, 30), match='hway'>

print(re.search(r"[aA-zZ]way", "This is the end of the way"))  # => None

print(re.search(r"cloud[A-Za-z0-9]", "cloud76"))
print(re.search(r"cloud[aA0-zZ9]", "cloud76"))


print(re.search(r"[^aA-zZ ]", "To jest zdanie z przecinkiem, ale bez kropki")) #UWAGA bo zZ ] jest spacja dzieki temu
                                                                             # wypluwa , a nie odstepy miedzy slowami
print(re.search(r"cat|dog", "is this a good doggo?"))

def check_punctuation (text):
  result = re.search(r"^[A-Z].*[.!?]$", text)
  return result != None

print(check_punctuation("This is a sentence that ends with a period.")) # True
print(check_punctuation("This is a sentence fragment without a period")) # False
print(check_punctuation("Aren't regular expressions awesome?")) # True
print(check_punctuation("Wow! We're really picking up some steam now!")) # True
print(check_punctuation("End of the line")) # False


# FUNKCJE RE:
#  re.search - szuka 1wszego matcha
#  re.findall

#RESERVED CHARACTERS:
#   . - dowolny znak  tzw WILDCARD
#   .* - dowolna ilosc dowolnych znakow np pomiedzy ^[A-Z].*[!?.]$ - to ma sie zaczac z
#                                   duzej litery, cokolwiek w srodku i zakonczyc ! ? lub .
#   ^ - poczatek stringa szukanego np ^fruit   >>>>> fruitcakes, fruits, fruitstore itd itp
#   $ - koniec stringa szukanego np cat$ >>>>>>   tomcat, wildcat, bearcat itd itp
#   | - takie LUB np re.search(r"cat|dog", "is this a good doggo?")

#CHARACTER CLASS:
 # przyklady:
 #  [listaznakow] np [.!?]$ - string ma sie konczyc jednymz  tych 3 znakow
 #  [aA]ronia - duze a lub małe
 #  [A-Z]olo - zaczyna sie na dowolna litere od a do z
 #     jedno z drugim to np [aA-zZ]
 #  mozna łączyc dowolna ilość np re.search(r"cloud[A-Za-z0-9]", "cloud76")
 #  [^aA-zZ] - ma szukac czegos co nie jest tym co w nawiasie
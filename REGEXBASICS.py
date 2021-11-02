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

print(re.search(r"Py[aA-zZ]*n", "Python programming")) #to => Python bo szuka 1wszego matcha
print(re.search(r"Py.*n", "Python programming")) #to daje duzo dluzszy match bo szuka mozliwosci
                                                        # z najwieksza iloscia znakow

print(re.search(r"o+l+", "bolo is rolo")) # => <re.Match object; span=(1, 3), match='ol'>
print(re.search(r"o+l+", "woolly poolly"))  # => <re.Match object; span=(1, 5), match='ooll'>

print(re.search(r"p?each", "to each his own")) # w tym wypadku p ma byc 0 lub 1 raz inaczej no match

print(re.search(r"\w*", "jakies tam zdanie"))
print(re.search(r"\w*", "jakies_tam_zdanie"))

pattern = r"^[aA-zZ_][aA-zZ0-9_]*$"  # na pocz ma byc litera duza/mala lub podkreslnik
                                  # potem litera cyfra lub podkreslnik a potem cokolwiek
print(re.search(pattern, "_this_is_a_valid_variable_name"))
print(re.search(pattern, "this isnt a valid variable name")) # spacja nie jest w dop znakach

def check_punctuation (text):
  result = re.search(r"^[A-Z].*[.!?]$", text)
  return result != None

print(check_punctuation("This is a sentence that ends with a period.")) # True
print(check_punctuation("This is a sentence fragment without a period")) # False
print(check_punctuation("Aren't regular expressions awesome?")) # True
print(check_punctuation("Wow! We're really picking up some steam now!")) # True
print(check_punctuation("End of the line")) # False

# The repeating_letter_a function checks if the text passed includes the letter "a"
# (lowercase or uppercase) at least twice. For example, repeating_letter_a("banana")
# is True, while repeating_letter_a("pineapple") is False.
# Fill in the code to make this work.
import re
def repeating_letter_a(text):
  result = re.search(r"[a].*[a]", text, re.IGNORECASE)
  return result != None

print(repeating_letter_a("banana")) # True
print(repeating_letter_a("pineapple")) # False
print(repeating_letter_a("Animal Kingdom")) # True
print(repeating_letter_a("A is for apple")) # True

# FUNKCJE RE:
#  re.search - szuka 1wszego matcha
#  re.findall

#RESERVED CHARACTERS:
#   \ - ESCAPE CHARACTER, zeby szukac innych znakow jak np . czy $ a nie ich uzywac
#                             np re.search(r"\.com","welcome")=> None
#   \w - any alphanumeric characters
#   \d for matching digits
#   \s for matching whitespace characters like space, tab or new line
#   . - dowolny znak  tzw WILDCARD
#   .* - dowolna ilosc dowolnych znakow np pomiedzy ^[A-Z].*[!?.]$ - to ma sie zaczac z
#                                   duzej litery, cokolwiek w srodku i zakonczyc ! ? lub .
#   ^ - poczatek stringa szukanego np ^fruit   >>>>> fruitcakes, fruits, fruitstore itd itp
#   $ - koniec stringa szukanego np cat$ >>>>>>   tomcat, wildcat, bearcat itd itp
#   | - takie LUB np re.search(r"cat|dog", "is this a good doggo?")
#   + - np "o+b+" bedzie sprawdzac czy sa stringi o i b zaraz po sobie w dowolnej ilosci
#                                           np ooobbb ob W KOLEJNOSCI podanej w ("a+b+")
#   ? - It means either zero or one occurrence of the character before it troche taki OPTIONAL




#CHARACTER CLASS:
 # przyklady:
 #  [listaznakow] np [.!?]$ - string ma sie konczyc jednym z tych 3 znakow
 #  [aA]ronia - duze a lub małe
 #  [A-Z]olo - zaczyna sie na dowolna litere od a do z
 #     jedno z drugim to np [aA-zZ]
 #  mozna łączyc dowolna ilość np re.search(r"cloud[A-Za-z0-9]", "cloud76")
 #  [^aA-zZ] - ma szukac czegos co nie jest tym co w nawiasie
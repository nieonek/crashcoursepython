def replace_domain(email, old_domain, new_domain):
    if "@" + old_domain in email:
        index= email.index("@"+old_domain)
        new_email= email[:index]+"@"+new_domain
        return new_email
    return email

replace_domain("nieon@o2.pl", "o2.pl", "gmail.com")
print(replace_domain("nieon@o2.pl", "o2.pl", "gmail.com"))


zdanie= "Another great example".split()
print(zdanie)

zdanie2= "Another great example".split("t")
print(zdanie2)


#ROBIENIE SKRÓTU:

def initials(phrase):
    words = phrase.split()  #NAJPIERW SPLITUJE NA POJEDYNCZE SLOWA
    result = "" # tworze pusty result ale "" zeby juz byl stringiem
    for word in words:         #TWORZE WORD ze slow w WORDS
        result += word[0].upper() #+= po to aby powtorzyl dla kazdego słowa, .upper() zeby zmienial zawsze na wielkie
    return result              #ma zwracaac rezultat

print(initials("Universal Serial Bus"))

name="Janek"
ksywa="knypek"
print("Twoje imie to {}, pamietam, ze w szkole wolali na ciebie: {}. Hahahaha".format(name,ksywa))

name="Janek"
ksywa="knypek"
print("Twoje imie to {name}, pamietam, ze w szkole wolali na ciebie: {ksywa}. Hahahaha {ksywa}".format(name=name,ksywa=ksywa))

print("abcdefghijklmno"[-len(ksywa):])
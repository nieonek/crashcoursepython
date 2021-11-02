import re
# tak wyprintuje bez znakow . ? ! ktore sa separatorami
print(re.split(r"[.?!]", "Pierwsze zdanie. Drugie zdanie? Trzecie zdanie!"))

# zeby je uzwglednilo trzeba dodac capturing parentheses czyli ( )

print(re.split(r"([.?!])", "Pierwsze zdanie. Drugie zdanie? Trzecie zdanie!"))



# SUB substitute (Podobne do REPLACE w stringach)

print(re.sub(r"[\w.%+-]+@[\w.-]+", "[REDACTED]", "Recieved an email for go_nuts95@my.example.com"))

name_record = "Lovelace, Ada"
print(re.sub(r"^([\w .-]*), ([\w .-]*)$", r"\2 \1", name_record))
#to co w ( ) to sa catpure group liczone od lewej doprawej, za pomoca \2 \4 itd itp odnosimy
#                                                             sie do konkretnej capture group


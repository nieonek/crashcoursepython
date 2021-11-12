mynumber = input()
x=mynumber.isnumeric()

if x == True:
    print("Your number is: \n" + mynumber)

elif x == False:
    print("This is not a number.\nTry again.")
    mynumber=input()




# REGEX NA LOGACH


# #  KROK 1wszy SZUKAMY LINIJEK LOGOW GDZIE JAKIS USER odpalal CRONy
# import sys
#
# logfile = sys.argv[1]  # 1wsza linijka
# with open(logfile) as f:
#     for line in f:
#         if "CRON" not in line:
#             continue
#         print(line.strip())

#  KROK 2gi REGEX ZEBY WYLUSKAC USERNAMEy od CRONow

import re

pattern = r"USER \((\w+)\)$"
line = "JUL 6 14:04:45 computer.name CRON[29940]: USER (zly_admin)"
result = re.search(pattern,line)
print(result)
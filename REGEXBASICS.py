log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
index = log.index ("[")
print(log[index+1:index+6])
#>>>>>12345

import re
regex = r"\[(\d+)\]"
result = re.search(regex, log)
print(result[1])


#RESERVED CHARACTERS:
#   . - dowolny znak
#   ^ - poczatek stringa szukanego np ^fruit   >>>>> fruitcakes, fruits, fruitstore itd itp
#   $ - koniec stringa szukanego np cat$ >>>>>>   tomcat, wildcat, bearcat itd itp

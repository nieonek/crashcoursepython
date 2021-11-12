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



#
# We're using the same syslog, and we want to display the date, time, and process id that's inside the square brackets.
# We can read each line of the syslog and pass the contents to the show_time_of_pid function. Fill in the gaps to
# extract the date, time, and process id from the passed line, and return this format: Jul 6 14:01:23 pid:29440.
#
# PRZYKLADOWE LOGI
# Jul 6 14:02:08 computer.name jam_tag=psim[29187]: (UUID:006)
# Jul 6 14:01:23 computer.name CRON[29440]: USER (good_user)
# Jul 6 14:02:09 computer.name jam_tag=psim[29187]: (UUID:007)

import re
def show_time_of_pid(line):
  pattern = r"(\w+ \d+ \d+:\d+:\d+)+.*?\[(\d+)\]"
  result = re.findall(pattern, line)
  return "{} pid:{}".format(result[0][0], result[0][1])

print(show_time_of_pid("Jul 6 14:01:23 computer.name CRON[29440]: USER (good_user)")) # Jul 6 14:01:23 pid:29440

print(show_time_of_pid("Jul 6 14:02:08 computer.name jam_tag=psim[29187]: (UUID:006)")) # Jul 6 14:02:08 pid:29187

print(show_time_of_pid("Jul 6 14:02:09 computer.name jam_tag=psim[29187]: (UUID:007)")) # Jul 6 14:02:09 pid:29187

print(show_time_of_pid("Jul 6 14:03:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:03:01 pid:29440

print(show_time_of_pid("Jul 6 14:03:40 computer.name cacheclient[29807]: start syncing from \"0xDEADBEEF\"")) # Jul 6 14:03:40 pid:29807

print(show_time_of_pid("Jul 6 14:04:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:04:01 pid:29440

print(show_time_of_pid("Jul 6 14:05:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:05:01 pid:29440
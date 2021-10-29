# In this exercise, we will test your knowledge of reading and writing files
# by playing around with some text files.
# Let's say we have a text file containing current visitors at a hotel.
# We'll call it, guests.txt. Run the following code to create the file.
# The file will automatically populate with each initial guest's
# first name on its own line.

guests = open("guests.txt", "w")
initial_guests = ["Bob", "Andrea", "Manuel", "Polly", "Khalid"]

for i in initial_guests:
    guests.write(i + "\n")

guests.close()

# No output is generated for the above code cell.
# To check the contents of the newly created guests.txt file,
# run the following code.

with open("guests.txt") as guests:
    for line in guests:
        print(line)

# The output shows that our guests.txt file is correctly populated with
# each initial guest's first name on its own line. Cool!
# Now suppose we want to update our file as guests check in and out.
# Fill in the missing code in
# the following cell to add guests to the guests.txt file as they check in.

new_guests = ["Sam", "Danielle", "Jacob"]

with open("guests.txt", "a") as guests:
    for i in new_guests:
        guests.write(i + "\n")

guests.close()

# check znowu

with open("guests.txt") as guests:
    for line in guests:
        print(line)

# Now let's remove the guests that have checked out already.
# There are several ways to do this, however,
# the method we will choose for this exercise is outlined as follows:
#
# 1 Open the file in "read" mode.
# 2 Iterate over each line in the file and put each guest's name into
#   a Python list.
# 3 Open the file once again in "write" mode.
# 4 Add each guest's name in the Python list to the file one by one.

# Ready? Fill in the missing code in
# the following cell to remove the guests that have checked out already.

checked_out=["Andrea", "Manuel", "Khalid"]
temp_list=[]

with open("guests.txt", "r") as guests:
    for g in guests:
        temp_list.append(g.strip())

with open("guests.txt", "w") as guests:
    for name in temp_list:
        if name not in checked_out:
            guests.write(name + "\n")

# check

with open("guests.txt") as guests:
    for line in guests:
        print(line)

# Now let's check whether Bob and Andrea are still checked in.

guests_to_check = ['Bob', 'Andrea']
checked_in = []

with open("guests.txt","r") as guests:
    for g in guests:
        checked_in.append(g.strip())
    for check in guests_to_check:
        if check in checked_in:
            print("{} is checked in".format(check))
        else:
            print("{} is not checked in".format(check))


# OPERACJE NA PLIKACH

import os
os.remove("text.txt")

os.rename("text.txt", "nowytext.txt")

os.path #sub moduł OS do sprawdzania statusu plikow itp

os.path.exists("text.txt")

os.path.getsize("text.txt")

os.path.getmtime("text.txt")  #wynik to timestamp w s liczonych od 1.1.1970

import datetime
timestamp = os.path.getmtime("text.txt")
datetime.datetime.fromtimestamp(timestamp)

os.getcwd()  #???????????
os.path.abspath("text.txt")  #pokazuje sciezke pliku
print(os.getcwd())  #pokazuje current directory
os.mkdir("newfolder") #nowy folder
os.chdir("newfolder") #zmienia current directory
os.rmdir("newfolder")  #usuwa folder ale tlyko jak jest pusty, jak jest pelen daje rerror

os.listdir("website")  = wypluwa liste plikow jako stringi
#os.path.join()

dir = "website"
for name in os.listdir(dir):
    fullname = os.path.join(dir, name)
    if os.path.isdir(fullname):
        print("{} is a dircetory".format(fullname))
    else:
        print("{} is a file".format(fullname))


# The create_python_script function creates a new python script in the current working directory, adds the line of
# comments to it declared  by the 'comments' variable, and returns the size of the new file.
# Fill in the gaps to create a script called "program.py".
def create_python_script(filename):
  comments = "# Start of a new Python program"
  with ___:
    filesize = ___
  return(filesize)

print(create_python_script("program.py"))

# ROZWIAZANIE
import os
def create_python_script(filename):
  comments = "# Start of a new Python program"
  with open(filename, "w") as file:
    file.write(comments)
  filesize = os.path.getsize(filename)
  return(filesize)

print(create_python_script("program.py"))

# The new_directory function creates a new directory inside the current working directory, then creates a new
# empty file inside the new directory, and returns the list of files in that directory.
# Fill in the gaps to create a file "script.py" in the directory "PythonPrograms".

import os
def new_directory(directory, filename):
  # Before creating a new directory, check to see if it already exists
  if os.path.isdir(directory) == False:
    os.mkdir(directory)

  # Create the new file inside of the new directory
  os.chdir(directory)
  with open (filename, "w") as file:
    pass
  os.chdir("..")    #OCOKAMAN?>!!?!?!
  # Return the list of files in the new directory
  return os.listdir(directory)

print(new_directory("PythonPrograms", "script.py"))


# The file_date function creates a new file in the current working directory, checks the date that the file was modified
# , and returns just the date portion of the timestamp in the format of yyyy-mm-dd.
# Fill in the gaps to create a file called "newfile.txt" and check the date that it was modified.
import os
import datetime

def file_date(filename):
  # Create the file in the current directory
  ___
  timestamp = ___
  # Convert the timestamp into a readable format, then into a string
  ___
  # Return just the date portion
  # Hint: how many characters are in “yyyy-mm-dd”?
  return ("{___}".format(___))

print(file_date("newfile.txt"))
# Should be today's date in the format of yyyy-mm-dd

#ROZWIAZANIE

import os
import datetime

def file_date(filename):
  # Create the file in the current directory
  with open(filename, "w") as file:
      pass
  timestamp = os.path.getmtime(filename)
  # Convert the timestamp into a readable format, then into a string
  dt=datetime.datetime.fromtimestamp(timestamp)
  # Return just the date portion
  # Hint: how many characters are in “yyyy-mm-dd”?
  return ("{}".format(dt.strftime("%Y-%m-%d")))

print(file_date("newfile.txt"))
# Should be today's date in the format of yyyy-mm-dd
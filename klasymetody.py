class Piglet:
    name = "piglet"  # to jest default name
    def speak(self):
        print("Oink! I'm {}! Oink!".format(self.name))

hamlet = Piglet()
hamlet.name = "Hamlet"
hamlet.speak()
petunia = Piglet()
petunia.name = "Petunia"
petunia.speak()

class Piglet:
    years = 0
    def pig_years(self):
        return self.years * 18

piggy = Piglet()
piggy.years = 2
print(piggy.pig_years())



#CONSTRUCTOR
class Apple:
    def __init__(self,color,flavor):
        self.color = color
        self.flavor = flavor
    def __str__(self):
        return "This apple is {} and its flavor is {}".format(self.color,self.flavor)
    #__str__ pozwala nam pisza print(reneta) dostac jakiegos stringa a nie np x87%&VXBJKGH* - default
reneta = Apple("red","sweet")
print(reneta.color)
print(reneta.flavor)
print(reneta)

#przyklad z kursu:
class Person:
    def __init__(self, name):
        self.name = name
    def greeting(self):
        # Should return "hi, my name is " followed by the name of the Person.
        return "hi, my name is {}".format(self.name)

# Create a new instance with a name of your choice
some_person = Person("Janek")
# Call the greeting method
print(some_person.greeting())

help(Apple)  #lista komend nacisnij q by wyjsc

#docstring  krotki opis co cos robi

def to_seconds(hours,minutes,seconds):
    """returns the amount of seconds"""
    return hours*3600+minutes*60+seconds

print(to_seconds(12,30,44))
help(to_seconds)




# WINDA
class Elevator:
    def __init__(self, bottom, top, current):
        """Initializes the Elevator instance."""
        self.current= current
        self.bottom= bottom
        self.top= top
    def up(self):
        """Makes the elevator go up one floor."""
        self.current += 1
        if self.current > self.top:
            self.current = self.top
    def down(self):
        """Makes the elevator go down one floor."""
        self.current -= 1
        if self.current < self.bottom:
            self.current = self.bottom
    def go_to(self, floor):
        """Makes the elevator go to the specific floor."""
        self.current = floor
    def __str__(self):
        return "Current floor is {}".format(self.current)

elevator = Elevator(-1, 10, 0)

elevator.up()
elevator.current #should output 1

elevator.go_to(10)
elevator.current #should output 10

# Go to the top floor. Try to go up, it should stay. Then go down.
elevator.go_to(10)
elevator.up()
elevator.down()
print(elevator.current) # should be 9
# Go to the bottom floor. Try to go down, it should stay. Then go up.
elevator.go_to(-1)
elevator.down()
elevator.down()
elevator.up()
elevator.up()
print(elevator.current) # should be 1

#Now add the str method to your Elevator class definition above so that when printing
# the elevator using the print( ) method,
# we get the current floor together with a message.
# For example, in the 5th floor it should say "Current floor: 5"

elevator.go_to(5)
print(elevator)

#repozytorium klas?

class Repository:
    def __init__(self):
        self.packages = {}
    def add_package(self, package):
        self.packages[package.name] = package
    def total_size(self):
        result = 0
        for package in self.packages.values():
            result += package.size
        return result

# MODULES

import random
random.randint(1, 10)
import datetime
now = datetime.datetime.now()
type(now)
print(now)
print(now.year)
print(now+datetime.timedelta(days=28))


# TEST Z INHERITANCE

class Animal:
    name = ""
    category = ""

    def __init__(self, name):
        self.name = name

    def set_category(self, category):
        self.category = category

class Turtle(Animal):
    category = "reptile"

print(Turtle.category)

class Snake(Animal):
    category = "reptile"

class Zoo:
    def __init__(self):
        self.current_animals = {}

    def add_animal(self, animal):
        self.current_animals[animal.name] = animal.category

    def total_of_category(self, category):
        result = 0
        for animal in self.current_animals.values():
            if animal == category:
                result += 1
        return result

zoo = Zoo()

turtle = Turtle("Turtle") #create an instance of the Turtle class
snake = Snake("Snake") #create an instance of the Snake class

zoo.add_animal(turtle)
zoo.add_animal(snake)

print(zoo.total_of_category("reptile")) #how many zoo animal types in the reptile category


#GRADED ASSESMENT OMG

# Begin Portion 1#
import random


class Server:
    def __init__(self):
        """Creates a new server instance, with no active connections."""
        self.connections = {}

    def add_connection(self, connection_id):
        """Adds a new connection to this server."""
        connection_load = random.random() * 10 + 1
        if connection_id != None:
            self.connections[connection_id] = connection_load
        # Add the connection to the dictionary with the calculated load

    def close_connection(self, connection_id):
        if connection_id != None:
            del self.connections[connection_id]
        """Closes a connection on this server."""
        # Remove the connection from the dictionary

    def load(self):
        """Calculates the current load for all connections."""
        total = 0
        for user in self.connections:
            total += self.connections[user]
        # Add up the load for each of the connections
        return total

    def __str__(self):
        """Returns a string with the current load of the server"""
        return "{:.2f}%".format(self.load())

# End Portion 1#

server = Server()
server.add_connection("192.168.1.1")

print(server.load())

server.close_connection("192.168.1.1")
print(server.load())

#Begin Portion 2#
class LoadBalancing:
    def __init__(self):
        """Initialize the load balancing system with one server"""
        self.connections = {}
        self.servers = [Server()]

    def add_connection(self, connection_id):
        """Randomly selects a server and adds a connection to it."""
        server = random.choice(self.servers)
        self.connections[connection_id] = server
        server.add_connection(connection_id)
        self.ensure_availability()
        # Add the connection to the dictionary with the selected server
        # Add the connection to the server

    def close_connection(self, connection_id):
        """Closes the connection on the the server corresponding to connection_id."""
        # Find out the right server
        for connection in self.connections.keys():
            if connection == connection_id:
                server_of_connection=self.connections
        del self.connections[connection_id]
        # Close the connection on the server
        # Remove the connection from the load balancer

    def avg_load(self):
        loads=0
        result=0
        for server in self.servers:
            result += server.load()
            loads +=1
        """Calculates the average load of all servers"""
        # Sum the load of each server and divide by the amount of servers
        return result / loads

    def ensure_availability(self):
        """If the average load is higher than 50, spin up a new server"""
        if self.avg_load() > 50:
            self.servers.extend([Server()])

    def __str__(self):
        """Returns a string with the load for each server."""
        loads = [str(server) for server in self.servers]
        return "[{}]".format(",".join(loads))
#End Portion 2#

l = LoadBalancing()
l.add_connection("fdca:83d2::f20d")
print(l.avg_load())

l.close_connection("fdca:83d2::f20d")
print(l.avg_load())

for connection in range(20):
    l.add_connection(connection)
print(l)

print(l.avg_load())

#Awesome! If the average load is indeed less than 50%, you are all done with this assessment.
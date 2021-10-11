#INPUT:

# Atrybuty:
# Date
# User
# Machine
# Type

# Eventy:
#
# Login
# Logout

#OUTPUT:
# Date
# Type
# Machine
# User loggedin
# ---> rreport printed on the screen

# We need to process a list of Event objects using their attributes to generate a report that lists
# all users currently logged in to the machines.
#
# Listy trzeba bedzie posrotowac
# sort() ta modyfikuje liste ktora sortuja
# sorted() ta tworzy nowa posortowana liste
# bedziemy uzywac raczej sort()
# print(sorted(names, key=len)) tak np sortuje po dlugosci

# get_event_date

# BEDZIEMY CHCIELI:

# jak sie ktos zaloguje dodajemy go do machine_users=["janek"]
# jak sie wyloguje to wywalic
# bedziemy uzywac - set

# raport bedzie tworzony z dictionary

def get_event_date(event):
    return event.date

def current_users(events):
    events.sort(key=get_event_date)
    machines = {}
    for event in events:
        if event.machine not in machines:
            machines[event.machine] = set()
        if event.type = "login":
            machines[event.machine].add(event.user)
        elif event.type = "logout"
            machines[event.machine].remove(event.user)
    return machines

def generate_report(machines):
    for machine, users in machines.items():
        if len(users) > 0:
            user_list = ", ".join(users)
            print(F"{machine}: {user_list}")
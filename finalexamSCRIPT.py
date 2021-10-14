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
        if event.type == "login":
            machines[event.machine].add(event.user)
        elif event.type == "logout":
            machines[event.machine].remove(event.user)
    return machines

def generate_report(machines):
    for machine, users in machines.items():
        if len(users) > 0:
            user_list = ", ".join(users)
            print(F"{machine}: {user_list}")

class Event:
    def __init__(self,event_date, event_type, machine_name, user):
        self.date = event_date
        self.type = event_type
        self.machine = machine_name
        self.user = user

events = [
    Event('2020-01-21 12:45:56', 'login', 'myworkstation.local', 'Janek'),
    Event('2020-01-22 12:26:12', 'login', 'webserver.local', 'Zenek'),
    Event('2020-01-22 16:34:12', 'logout', 'webserver.local', 'Zenek'),
    Event('2020-01-21 14:02:07', 'login', 'mailserver.local', 'Benek'),
]

users = current_users(events)
print(users)

generate_report(users)


def licz_slowa(zdanie):
    lista = zdanie.split()  # [Ala, ma, kota, a, kot, to, alik]
    slownik = {}

    for slowo in lista:
        if slowo in slownik:
            slownik[slowo] += 1
        else:
            if len(slowo) >= 3:
                slownik[slowo] = 1

    return slownik


print(licz_slowa("Ala ma kot a kot to alik"))

text="""If we call childhood happy because it does not yet know sexual desire, we must not forget how abundant a source of disappointment and self-denial, and thus of dream stimulation, the other of the great life-impulses may become for it. Here is a second example showing this. My nephew of twenty-two months had been given the task of congratulating me upon my birthday, and of handing me, as a present, a little basket of cherries, which at that time of the year were not yet in season. It seemed difficult for him, for he repeated again and again: “Cherries in it,” and could not be induced to let the little basket go out of his hands. But he knew how to secure his compensation. He had, until now, been in the habit of telling his mother every morning that he had dreamt of the “white soldier,” an officer of the guard in a white cloak, whom he had once admired on the street. On the day after the birthday, he awakened joyfully with the information which could have had its origin only in a dream: “Her man eat up all the cherries!” 
What animals dream of I do not know. A proverb for which I am indebted to one of my readers claims to know, for it raises the question: “What does the goose dream of?” the answer being: “Of maize!” The whole theory that the dream is the fulfilment of a wish is contained in these sentences. We now perceive that we should have reached our theory of the hidden meaning of the dream by the shortest road if we had merely consulted colloquial usage. The wisdom of proverbs, it is true, sometimes speaks contemptuously enough of the dream—it apparently tries to justify science in expressing the opinion that “Dreams are mere bubbles;” but still for colloquial usage the dream is the gracious fulfiller of wishes. “I should never have fancied that in the wildest dream,” exclaims one who finds his expectations surpassed in reality."""

uninteresting_words=[]
file_contents=text.split()
freq={}
string=""

for word in file_contents:
    string2= (char for char in word if char.isalpha())
    string = "".join(string2)
    #string= "".join(char for char in word if char.isalpha())
    if string.lower() not in uninteresting_words:
        if string.lower() not in freq:
            freq[string.lower()]=1
        else:
            freq[string.lower()]+=1


print(freq)


# LAST EXAM

# !pip install wordcloud
# !pip install fileupload
# !pip install ipywidgets
# !jupyter nbextension install --py --user fileupload
# !jupyter nbextension enable --py fileupload
#
# import wordcloud
# import numpy as np
# from matplotlib import pyplot as plt
# from IPython.display import display
# import fileupload
# import io
# import sys

# This is the uploader widget

# def _upload():
#
#     _upload_widget = fileupload.FileUploadWidget()
#
#     def _cb(change):
#         global file_contents
#         decoded = io.StringIO(change['owner'].data.decode('utf-8'))
#         filename = change['owner'].filename
#         print('Uploaded `{}` ({:.2f} kB)'.format(
#             filename, len(decoded.read()) / 2 **10))
#         file_contents = decoded.getvalue()
#
#     _upload_widget.observe(_cb, names='data')
#     display(_upload_widget)
#
# _upload()

# def calculate_frequencies(file_contents):
#     # Here is a list of punctuations and uninteresting words you can use to process your text
#     punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
#     uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
#                            "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its",
#                            "they", "them", \
#                            "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be",
#                            "been", "being", \
#                            "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when",
#                            "where", "how", \
#                            "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very",
#                            "can", "will", "just"]
#
#     # LEARNER CODE START HERE
#     file_contents = file_contents.split()
#     wordfreq = {}
#     string = ""
#
#     for word in file_contents:
#         stringi = (char for char in word if char.isalpha())
#         string = "".join(stringi)
#         if string.lower() not in uninteresting_words:
#             if string.lower() not in wordfreq:
#                 wordfreq[string.lower()] = 1
#             else:
#                 wordfreq[string.lower()] += 1
#
#     # wordcloud
#     cloud = wordcloud.WordCloud()
#     cloud.generate_from_frequencies(wordfreq)
#     return cloud.to_array()

# # Display your wordcloud image
#
# myimage = calculate_frequencies(file_contents)
# plt.imshow(myimage, interpolation = 'nearest')
# plt.axis('off')
# plt.show()
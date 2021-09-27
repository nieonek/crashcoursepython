import random
print("Hi what's your name")
name=input()
secretnumber = random.randint(1,20)
print(("Hello ") + name + (" can you guess my number?"))

for guessesTaken in range(1,7):
    print("now guess")
    guess=(int(input()))
    if guess < secretnumber:
        print("too low.")
    elif guess > secretnumber:
        print("too much.")
    else:
        print("Yes! that was " + str(secretnumber))
        break
if guess == secretnumber:
    print ("Good job! You guessed the number in " + str(guessesTaken))
else:
    print("sorry. the secret number was " + str(secretnumber))
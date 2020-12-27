import random
words=[]
name=input("What is your name: ")
print("Good Luck",name)
f=input("Enter file name: ")
file=open(f)
file=file.read()
file=file.split()
for t in file:
    words.append(t)
#words=['rainbow','computer','science','programming','python','mathematics','condition','reverse','water','board','geeks']
#print(words)
word=random.choice(words)
print("Guess the character")
guesses=' '
turns=12
while turns>0:
    failed=0
    for char in word:
        if char in guesses:
            print(char)
        else:
            print("_")
            failed+=1
    if failed==0:
        print("You win")
        print("The word is : ",word)
        break
    guess=input("guess a character: ")
    guesses+=guess
    if guess not in word:
        turns-=1
        print("Wroung")
        print(f"You have {turns} more guesses")
        if turns==0:
            print("You Loose")
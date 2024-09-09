import random

words=['sanchit','sai','raj','pari']
lives=6
chooseword=random.choice(words)
print(chooseword)

placeholder=""
words_len=len(chooseword)
for position in range(words_len):
    placeholder+="_"
print(placeholder)

gameover=False
correctletter=[]
while not gameover:
    guess=input("Guess a letter:").lower()
    display=""
    for letter in chooseword:
        if letter==guess:
            display+=letter
            correctletter.append(guess)
        elif letter in correctletter:
            display+=letter
        else:
            display +="_"
    print(display)
    if guess not in chooseword:
        lives-=1
        if lives==0:
            gameover=True
            print("You lose!")

if "_" not in display:
    gameover=True
    print("You Win")
print(lives)
# This is a typing test program which will include 3 different levels.
# It will give a random word and control every input character and will mark every correct letters and mistakes. 
# It will record the time as well to print at the end of test. There may be effect of time for marking in the future.

import random, datetime, keyboard, colorama, numpy as np

blocked_keys = ["enter","caps lock","tab","shift","right shift","ctrl","right ctrl","home","end","insert","delete","page up","page down","up","down","right","left", "print screen"]

with open("word-list.txt") as file:
    wordList = file.read()
wordList = list(wordList.split("\n"))

# Excludes blocked keys from word list.
for word in blocked_keys:
    if word in wordList:
        wordList.remove(word)

colorama.init() # Starts colorama: a library colorizes outputs.
def analyzeInput(targetWord):
    inputWord, char_event, char = "", "", ""
    inputCharIndex, score, correctTypeScore, falseTypeScore = 0,0,0,0

    while True:
        char_event = keyboard.read_event(suppress=True)
        if char_event.event_type != keyboard.KEY_UP:
            continue

        char = char_event.name

        if char == "esc":
            return[-1, -1]
        elif char in blocked_keys:
            pass # Ignores the function buttons on the keyboard.
        elif char == "backspace":
            if inputWord:
                inputWord = inputWord[:-1]
                inputCharIndex -= 1
                print("\r{}{}".format(inputWord,colorama.Style.RESET_ALL), end="")
        else:
            if char == targetWord[inputCharIndex]:
                inputCharIndex += 1
                inputWord += char
                print("\r{}{}".format(inputWord,colorama.Style.RESET_ALL), end="")
                correctTypeScore += 1
            else:
                print("\r{}{}{}".format(colorama.Fore.RED,inputWord+char,colorama.Style.RESET_ALL), end="")
                falseTypeScore += 1
        if inputWord == targetWord:
            print("\r{}{}{}".format(colorama.Fore.GREEN,inputWord,colorama.Style.RESET_ALL), end="")
            return [correctTypeScore, falseTypeScore]
        char_event, char = "",""

chosenWord = ""
inputWord = ""
startTime, finishTime, wordStartTime, wordFinishTime, score, correctWords, wrongWords = 0,0,0,0,0,0,0
totalCorrectTypeScore, totalFalseTypeScore = 0,0

seed = input("Please provide a text or number (up to 10 character) to select random word choice pattern: ")

if len(seed) > 10: # If seed length is longer than 10 character reduces the seed to 10 character.
    seed = seed[0:9]
if seed.isdigit() == False: # If seed is text encodes it into numbers.
    seed = int(''.join(str(ord(c)) for c in seed))
random.seed(seed)

# Level System
minWordLength, maxWordLength, totalWordCount = 0, 0, 0
level = input("Please provide a level (1/2/3 or 0 to get info about levels): ")
corrTypeWeight, falseTypeWeight = 0, 0

while True:
    if (level.isdigit() == True) and (level in ["1","2","3"]): # If level var. does not numbers
        break
    elif level == "0":
        print("""Level\tWord Length Range\tTotal Word Count
    Level 1\t3-5\t10
    Level 2\t5-7\t20
    Level 3\t7-15\t20""")
    
    level = input("Please provide a level (1/2/3 or 0 to get info about levels): ")

if level == "1":
    minWordLength = 3
    maxWordLength = 5
    totalWordCount = 10
    corrTypeWeight = 1
    falseTypeWeight = 1

elif level == "2":
    minWordLength = 5
    maxWordLength = 7
    totalWordCount = 20
    corrTypeWeight = 0,7
    falseTypeWeight = 5

elif level == "3":
    minWordLength = 7
    maxWordLength = 15
    totalWordCount = 20
    corrTypeWeight = 0.5
    falseTypeWeight = 10


wordList = [word for word in wordList if (len(word) >= minWordLength) and (len(word) <= maxWordLength)]

startTime = datetime.datetime.now()
while totalWordCount > 0:
    chosenWord = random.choice(wordList)
    print("\n" + 10 * " " + chosenWord + 10 * " ")
    print("Please write the word above: ")
    outputs = analyzeInput(chosenWord)
    if outputs[0] == -1:
        break
    totalCorrectTypeScore += outputs[0]
    totalFalseTypeScore += outputs[1]
    totalWordCount -= 1
finishTime = datetime.datetime.now()

# Formula
# (total correct type * correct typing weight) / ((total correct type * correct typing weight) + (total false type * false typing weight))

score = (totalCorrectTypeScore * corrTypeWeight) / ((totalCorrectTypeScore * corrTypeWeight) + (totalFalseTypeScore * falseTypeWeight))
score = int(round(score, 4) * 100)

print("""\n\tRESULTS\n{}\nCorrect typing: {}
False Typing: {}
Test Completion Time: {}
Final Score: {} %""".format(25*"-",totalCorrectTypeScore, totalFalseTypeScore, finishTime-startTime, score))

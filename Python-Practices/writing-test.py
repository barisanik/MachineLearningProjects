# This is a writing test program which will include 3 different levels.
# It will give a random word and control every input character and will mark every correct letters and mistakes. 
# It will record the time as well to print at the end of test. There may be effect of time for marking in the future.

import random, datetime, keyboard

level = 0
wordCount = 3 # Word count will be standardized after having a enough word list.
chosenWord = ""
inputWord = ""
startTime, finishTime, wordStartTime, wordFinishTime, point, correctWords, wrongWords = 0,0,0,0,0,0,0

wordList = ["car","rain","building","comprehensive","time"]
startTime = datetime.datetime.now()
while wordCount > 0:
    chosenWord = random.choice(wordList)
    print(10*" " + chosenWord + 10 * " ")
    inputWord = input("Please write the word above: ")
    if inputWord != chosenWord:
        point -= 100
        wrongWords += 1
    else:
        point += 100
        correctWords += 1
    wordCount -= 1
finishTime = datetime.datetime.now()

print("You wrote {} correct words and {} false one. Final point: {}".format(correctWords, wrongWords, point))

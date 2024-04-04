# This is a typing test program which will include 3 different levels.
# It will give a random word and control every input character and will mark every correct letters and mistakes. 
# It will record the time as well to print at the end of test. There may be effect of time for marking in the future.

import random, datetime, keyboard, colorama
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
            return [-1, -1, -1]
        elif char in ["enter","caps lock","tab","shift","right shift","ctrl","right ctrl","home","end","insert","delete","page up","page down","up","down","right","left"]:
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
                score += 10
                correctTypeScore += 1
            else:
                print("\r{}{}{}".format(colorama.Fore.RED,inputWord+char,colorama.Style.RESET_ALL), end="")
                score -= 10
                falseTypeScore += 1
        if inputWord == targetWord:
            print("\r{}{}{}".format(colorama.Fore.GREEN,inputWord,colorama.Style.RESET_ALL), end="")
            return [score, correctTypeScore, falseTypeScore]
        char_event, char = "",""

level = 0 # Level var. will be used after having an enough word list.
wordCount = 3 # Word count will be standardized after having an enough word list.
chosenWord = ""
inputWord = ""
startTime, finishTime, wordStartTime, wordFinishTime, score, correctWords, wrongWords = 0,0,0,0,0,0,0
totalCorrectTypeScore, totalFalseTypeScore = 0,0

wordList = ["car","rain","time"]
startTime = datetime.datetime.now()
while wordCount > 0:
    chosenWord = random.choice(wordList)
    print("\n" + 10 * " " + chosenWord + 10 * " ")
    print("Please write the word above: ")
    outputs = analyzeInput(chosenWord)
    if outputs[0] == -1:
        break
    score += outputs[0]
    totalCorrectTypeScore += outputs[1]
    totalFalseTypeScore += outputs[2]
    wordCount -= 1
finishTime = datetime.datetime.now()

print("""\n\tRESULTS\n{}\nCorrect typing: {}
False Typing: {}
Test Completion Time: {}
Final Score: {}""".format(25*"-",totalCorrectTypeScore, totalFalseTypeScore, finishTime-startTime, score))

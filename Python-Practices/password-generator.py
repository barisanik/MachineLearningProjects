import random
randomCharacter,randomCharacter1,randomCharacter2,randomCharacter3,randomCharacterList = "","","","",""
generatedPass = ""

print("""[--- Password Generator ---]
Please provide the details for the required password.\n""")

length = int(input("Length: "))
specChar = input("Includes Special Characters (Y/N): ")
capChar = input("Includes Capitalized Characters (Y/N): ")
num = input("Includes Number Characters (Y/N): ")

alphabet = "abcdefghijklmnoprstuvyzxwq"
specCharList = ">£#$½{[]}\|/.;Ş€!'^+%&()"
numList = "0123456789"

while length > 0:
    if specChar == "Y":
        randomCharacter1 = random.choice(specCharList)
    if num == "Y":
        randomCharacter2 = random.choice(numList)
    randomCharacter3 = random.choice(alphabet)
    if capChar == "Y" and random.randint(0,11) > 5:
        randomCharacter3 = randomCharacter3.capitalize()

    randomCharacterList = [randomCharacter1,randomCharacter2,randomCharacter3]
    randomCharacterList = [x for x in randomCharacterList if x != ""]
    
    randomCharacter = random.choice(randomCharacterList)

    generatedPass += randomCharacter
    length -= 1

print("Generated Password: ", generatedPass)

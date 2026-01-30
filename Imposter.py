from os import system, listdir
from platform import system as os
from random import sample, choice

inputPlayers  = ''
imposterCount = 0
inputCount    = ''
dictList      = list(x[:-4] for x in listdir('dictionaries') if x[-4:] == '.txt')
index         = 0
indexSelector = ''
userIndex     = 0
currentFile   = ''
wordCount     = 0
imposters     = []
wordList      = []

class Player:
    playerCount = 0
    currentWord = ''
    playerList    = []

    def __init__(this, playerName):
        this.name = playerName
        this.isImposter = False
        this.score = 0
        this.playerId = Player.playerCount
        Player.playerCount += 1
        Player.playerList.append(this)
    
    def setImposter(this):
        this.isImposter = True
        return

    def reset(this):
        this.isImposter = False
        return
    
    def getId(this):
        return this.playerId
    
    def getWord(this):
        if this.isImposter:
            return "Imposter"
        else:
            return Player.currentWord
    
    def getName(this):
        return this.name
    
    @classmethod
    def setWord(cls, newWord):
        cls.currentWord = newWord
    
    @classmethod
    def getNameList(cls):
        returnList = []
        for x in cls.playerList:
            returnList.append(x.getName())
        return returnList

def clearScreen():
    if os() == 'Windows':
        system('cls')
    else:
        system('clear')

if __name__ == "__main__":
    clearScreen()

    # Get the player list
    inputPlayers = ''
    while inputPlayers != '!done':
        inputPlayers = input('Enter player name: ')
        if inputPlayers not in ['!done', ''] + Player.getNameList():
            Player(inputPlayers.strip())
        elif inputPlayers in Player.getNameList():
            print('You cannot have repeat names')
    clearScreen()

    # Get the imposter count
    while imposterCount <= 0 or imposterCount > len(Player.playerList) / 2:
        try:
            imposterCount = int(input(f'How many imposters do you want (player count: {len(Player.playerList)}): '))
            if imposterCount <= 0:
                print('You need more than 0 imposters!')
            if imposterCount > len(Player.playerList) / 2:
                print('You need less than half the player count as imposter!')
        except:
            print('Not a valid number!')
    clearScreen()

    # Get the category
    index         = 0
    indexSelector = ''
    userIndex     = -1
    print(dictList)
    print('Select a category.')
    for x in dictList:
        wordCount = len(open('dictionaries/' + x + '.txt', 'r').read().split('\n'))
        print(f" {index}) {x} ({wordCount})")
        index += 1
    while userIndex <= -1 or userIndex >= index:
        indexSelector = input(' >> ')
        try:
            userIndex = int(indexSelector)
        except:
            userIndex = -1
    currentFile = dictList[userIndex]
    clearScreen()

    # Select word
    wordList = open('dictionaries/' + currentFile + '.txt', 'r').read().split('\n')
    Player.setWord(choice(wordList))

    # Set imposters
    imposters = sample(Player.playerList, imposterCount)
    for x in imposters:
        x.setImposter()
    
    # Give players the word
    for x in Player.playerList:
        print(f'{x.getName()} {x.getWord()}')
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
votedImposter = []

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

def conjunction(nameList):
    joinedString = ''
    if len(nameList) == 0:
        return ''
    elif len(nameList) == 1:
        return nameList[0]
    elif len(nameList) == 2:
        return ' and '.join(nameList)
    else:
        return ', '.join(nameList[:-1]) + ', and ' + nameList[len(nameList) - 1]

if __name__ == "__main__":
    clearScreen()

    # Get the player list
    inputPlayers = ''
    print('Enter "!done" when finished.')
    while inputPlayers != '!done':
        inputPlayers = input('Enter player name: ')
        if inputPlayers not in ['!done', ''] + Player.getNameList():
            Player(inputPlayers.strip())
        elif inputPlayers in Player.getNameList():
            print('You cannot have repeat names')
    clearScreen()

    # Get the imposter count
    imposterCount = -1
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

    # Select the word
    clearScreen()
    wordList = open('dictionaries/' + currentFile + '.txt', 'r').read().split('\n')
    Player.setWord(choice(wordList))

    # Set the imposters
    for x in sample(Player.playerList, imposterCount):
        x.setImposter()
    
    # Give players the word
    for x in Player.playerList:
        clearScreen()
        print(f'{x.getName()}')
        input('Press enter to reveal the word...')
        print(f'{x.getWord()}')
        input('Press enter continue...')

    # Select first player
    clearScreen()
    print(f'{choice(Player.playerList).getName()} goes first.')
    input('Press Enter to Vote')

    # Vote Imposter
    votedImposter = []
    for x in range(imposterCount):
        clearScreen()
        index              = 0
        indexSelector      = ''
        userIndex          = -1
        remainingImposters = [z for z in Player.getNameList() if z not in votedImposter]
        print('Vote who is imposter.')
        for y in remainingImposters:
            print(f" {index}) {y}")
            index += 1
        while userIndex <= -1 or userIndex >= index:
            indexSelector = input(' >> ')
            try:
                userIndex = int(indexSelector)
            except:
                userIndex = -1
        votedImposter.append(remainingImposters[userIndex])

    # Reveal imposter
    clearScreen()
    input(f'{conjunction(votedImposter)} {"was" if imposterCount == 1 else "were"} voted imposter...')
    print(f'{conjunction([x.getName() for x in Player.playerList if x.isImposter])}, what is the word?')
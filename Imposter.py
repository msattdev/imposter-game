from os import system, listdir

inputPlayers  = ''
playerList    = []
imposterCount = 0
inputCount    = ''
dictList      = list(x[:-4] for x in listdir('dictionaries') if x[-4:] == '.txt')
index         = 0
indexSelector = ''

class player:
    name = ''
    isImposter = False
    score = 0
    def __init__(this, playerName):
        this.name = playerName

if __name__ == "__main__":

    inputPlayers = ''
    while inputPlayers != '!done':
        inputPlayers = input('Enter player name: ')
        if inputPlayers != '!done':
            playerList.append(player(inputPlayers.strip()))
    system('clear')

    while imposterCount <= 0 or imposterCount > len(playerList) / 2:
        try:
            imposterCount = int(input(f'How many imposters do you want (player count: {len(playerList)}): '))
            if imposterCount <= 0:
                print('You need more than 0 imposters!')
            if imposterCount > len(playerList) / 2:
                print('You need less than half the player count as imposter!')
        except:
            print('Not a valid number!')
    system('clear')

    index         = 0
    indexSelector = 0
    print('Select a category.')
    for x in dictList:
        print(f' {index}) {x}')
        index += 1
    while indexSelector <= 0 or indexSelector >= index:
        index = input(' >> ')
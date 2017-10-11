import random
import sounds
import pygame

def randSounds(sounds) :
    sounds = sounds + sounds
    random.shuffle(sounds)
    return sounds

rows = 4
cols = 6
unsolvedPairs = rows*cols/2
soundTable = []
statusTable = []
opened = 0
also_open = []

def initBoard() :
    global rows
    global cols
    #initiate soundTable
    doublesounds = randSounds(sounds.getSounds())
    for i in range(rows) :
        row = []
        for j in range(cols) :
            row.append(doublesounds.pop())
        soundTable.append(row)
    #initiate statusTable
    #[ ] means unopened
    #[o] means open, unsolved
    #[x] means open, solved
    for i in range(rows) :
        row = []
        for j in range(cols) :
            row.append(" ")
        statusTable.append(row)

def getRows() :
    return rows

def getCols() :
    return cols

def getUnsolvedPairs() :
    return unsolvedPairs

def printBoard() :
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's']
    printed = "  "
    r = 0
    for i in range(cols) :
        printed += " " + str(i) + " "
    printed += "\n"
    for row in statusTable :
        printed += alphabet[r] + " "
        for cell in row :
            printed += "[" + cell + "]"
        printed += "\n"
        r += 1
    print printed ,

def getStatus(row, col) :
    return statusTable[row][col]

def playSound(row, col) :
    sound = soundTable[row][col]
    channel = sound.play()
    while channel.get_busy() :
        pygame.time.delay(100)

def doAction(row, col, action) :
    old_status = getStatus(row, col)
    if action == 0 and old_status == ' ' :
        statusTable[row][col] = 'o'
        sound = soundTable[row][col]
        channel = sound.play()
        while channel.get_busy() :
            pygame.time.delay(100)
    elif action == 1 and old_status == 'o' :
        statusTable[row][col] = ' '
    elif action == 2 and old_status == 'o' :
        statusTable[row][col] = 'x'
    else :
        print "I can not do that."

def getSound(row, col) :
    return str(soundTable[row][col])

def openCard(row, col) :
    #open card and play sound
    return doAction(row, col, 0) 

def closeCard(row, col) :
    return doAction(row, col, 1) #False

def markSolved(row, col) :
    return doAction(row, col, 2) #False

def handleCard(row, col) :
    global opened
    global also_open
    global unsolvedPairs
    if statusTable[row][col] == 'x' :
        print "That card is already solved."
        return False
    if opened == 0 :
        openCard(row, col)
        also_open = [row, col]
        opened = 1
    elif opened == 1 :
        row2 = also_open[0]
        col2 = also_open[1]
        if not (row == row2 and col == col2) :

            openCard(row, col)
            printBoard()
            if getSound(row, col) == getSound(row2, col2) :
                markSolved(row, col)
                markSolved(row2, col2)
                print "Match found!"
                unsolvedPairs -= 1
                also_open = []
                opened = 0
            else :
                closeCard(row, col)
                closeCard(row2, col2)
                print "Not a pair. Turning over."
                raw_input("Press enter to proceed.")
                opened = 0
                also_open = []
        else :
            print "Repeated."
            playSound(row, col)
    return True
        

import board

board.initBoard()
board.printBoard()

round = 0

def validateCoordinates(string) :
    if len(string) == 2 :
        str0 = string[:1]
        str1 = string[1:]
        if str0.isalpha() and len(str0) == 1 and str1.isdigit() :
            return (ord(str0)-ord('a'), int(str1))
        else :
            return False
    else :
        return False

while board.getUnsolvedPairs() > 0 :
    print "Round: %d" % round
    coord = raw_input("> ")
    validatedCoord = validateCoordinates(coord)
    if validatedCoord :
        row = validatedCoord[0]
        col = validatedCoord[1]
        
        if 0 <= row and row < board.getRows() and col < board.getCols() :
            if board.handleCard(row, col) :
                round += 1
                board.printBoard()
        else :
            print "Out of bounds."
    else :
        print "Input not ok. Example: a0"

print "Congratulations! You found all the pairs in %d rounds!" % round

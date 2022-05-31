from pickle import FALSE
import gameboard
import player

print("Welcome to the game!")
print("Instructions: ")
print("To move up: w")
print("To move down: s")
print("To move left: a")
print("To move right: d")

print("Try to get to the end! Good Luck!")
print("-----------------------------")


# A new gameboard has been created
board = gameboard.GameBoard()
# A new player was created starting at position 3,2
player = player.Player(3,2)
move_check = board.checkMove
win_check = board.checkWin

while True:
    board.printBoard(player.rowPosition, player.columnPosition)
    selection = input("Make a move: ")
    
    # TODO
    # Move the player through the board
    
    if (selection == (str.lower("a"))):
        if move_check(player.rowPosition,player.columnPosition):
            player.moveLeft()
        if win_check(player.rowPosition,player.columnPosition):
            break
    elif (selection == (str.lower("d"))):
        if move_check(player.rowPosition,player.columnPosition):
            player.moveRight()
        if win_check(player.rowPosition,player.columnPosition):
            break
    elif (selection == (str.lower("w"))):
        if move_check(player.rowPosition,player.columnPosition):
            player.moveUp()
        if win_check(player.rowPosition,player.columnPosition):
            break
    elif (selection == (str.lower("s"))):
        if move_check(player.rowPosition,player.columnPosition):
            player.moveDown()
        if win_check(player.rowPosition,player.columnPosition):
            break
    # Check if the player has won, if so print a message and break the loop!
    else:
        continue

# ------------------------------------------------------------------------------------------------------------------------------------------------------    


# HINTS:

# The overall idea is every "turn" the player takes is one iteration through the infinite loop in the app.py. In this loop you will need to:

# Figure out what direction the user wants to move  --COMPLETE--
# Check to see if the user can move in that direction --NOT COMPLETE--
# Move the user if the move is valid  --COMPLETE--
# Check to see if the user has won --COMPLETE--a

# BONUS:
# Figure out how to change the game board. Make it bigger, add more walls
# Add "Coins" to collect on the game board. The game should keep track of all the coins collected and tell you your score at the end
# Add "Enemies" to the game board. If the player moves onto an enemy square they should die and the game should end
# Add logic to the enemies that allows them to randomly move around the board (also respecting the walls of the game)
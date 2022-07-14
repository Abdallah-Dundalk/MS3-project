# BATTLESHIPS - MAN V MACHINE

This is a Python terminal game which runs in a mock terminal on Heroku. The mock terminal was created by the Code Institute and allows the user to play the game through a web browser.
The game uses the traditional battleship rules where one player tries to guess the other players ship coordinates in order to sink the opposing players ships. The opposing player in this version of the game is the the computer.

The game can be played here - https://ms3-project-battle-ships.herokuapp.com/

![BATTLESHIPS - MAN V MACHINE Responsive mock up]((./assets/images/responsive-mock-up.jpeg)

## How to play:

Battleships - Man v Machine is based on the well known traditional Battleships game. In this version of the game, each player has a board respresenting a grid in which there are 4 ships, each occupying its own square within the grid. The game begins after the user enters their name. The objective for each player is to guess the location of the other players ships by entering a row number followed by a column number. If the coordinates entered by the player match the coordinates of the other players ships, then that ship will be destroyed and the player will score one point. The first player to score 4 points will win the game. If both players score 4 points simultaneously, the game will end in a tie. 
The computer's ships are not visible to the user, hence the requirement for the user to guess the location. The location of each players ships are set randomly. The guesses made by the computer are also random, while the users guesses are entered manually by the user.
When a ship is hit, the corresponding coordinate on the players board will display a "*" symbol. A missed guess will be represented by an "x" and the ships on the users board are represented by teh "@" symbol. After each player makes a guess, both players boards will be displayed, showing whether they hit or missed their target and a text message will also inform the user of the coordinates chosen by both players, whether they hit or missed and what the score current score is. The user will then be prompted to choose to continue playing or to quit the game. If either player reaches a score of 4, the game will end, though the user will be presented with an option to play again.

## Existing Features:
* Player is updated with score at end of each round.
* Player is updated with guesses made by both players at end of each round.
* Player is given an option to quit or continue at the end of each round or at the end of each game.
* player boards are updated following each round.
* randomly generated computer guesses.
* randomly generated ship locations.
* data validation preventing the user from coordinates outside the range of the board.
* data validation preventing the player from entering a string values instead of numeric values for the players guess.
* data validation prevents the same coordinates being guessed more than once.
* scores are incremented between rounds.
* game variables such as score, ship locations, player and computer guesses are reset between games.
* game data stored in global lists and variables


## Future Features:
* text based imagery to illustrate when a ship is hit
* best of three type score counting system
* game summary showing time spent playing and number of guesses made

## Data Model:
I used a series of lists to store the game data. There a list for the computers and players ship locations, guesses, player boards and variables for the scores and the players name.

## Testing:
* every coordinate from (0, 0) - (4, 4) entered to ensure the values on the board update with an x.
* played countless rounds to ensure all coordinates update with an "x" for a miss and "*" for a hit.
* played game to through to end of round numerous times to ensure that the game win/game lose messages printed correctly.
* checked that the player is presented with an option to continue or quit after each round and after each game.
* checked that the players name is displayed above the player board after being input by the player.
* Checked that data validation for user inputting row and column numbers raised an error if text or values above 4 and below zero were input or text was input instead of an iteger.
* checked that all game values were cleared correctly at the begining of a new game.
* checked that the player and cpu score incremented correctly after each round.
* checked that the players board displayed the randomly generated ship positions correctly after being printed.
* checked that the player and cpu coordinate guesses text messages were printed with the correct values.
* checked that the player and cpu guesses were stored correctly and could not be used twice in the same round.
* checked that the coordinates chosen by the player and cpu were checked against the ship/target coordinates correctly and displayed the correct hit/miss message if the values matched/ didnt match.
* Code was checked usign PEP8 online with no errors found.

## Solved Bugs:
1. I was trying to print the player board after each turn. I had been using the append method to mark the board with an x , but this was causing two boards to be printed. I used extend method instead to update the board before printing.  This fixed the bug and the programme was now printing one updated board instead of two.

2. I tried usign a for loop to compare a list (player guess) with lists inside another list (CPU ship locations). But it appeared that this function would only match the player guess with teh first index of the CPU ship locations list. I then tried using the 'for x in list' loop and it worked as I intended where the player guess value could be matched with any of the values in the CPU ship locations list and not just the first one.

3. I wanted to increment the player score variable each time a ship was hit but I couldnt update the global variable from inside the function . After a fair amout of googling I found a suggestion to put the 'global' key word infront of the variable  inside the function, and sure enough, it worked.

4. After each round, a message is displayed showign what coordinates were guessed by both the player and the CPU. I noticed that the players board appeared to be printing the cpu's guesses opposite to the coordinates printed in the message. Initially I thought the error was beign caused by the print updated palyer board function. However I soon found that the arguments for the message fucntion were in teh wrong order (column value before the row value). I changed the order of the arguments and now the coordinates in the message match those on the updated board. 

5. I added a function to allow the user to choose to play a new game or quit when a game had been completed. I included a function to reset all gamevariables or lists to empty or zero. However when the new game was played, the old boards were printed along side the new boards. This was similar to a bug I experienced previously. I discovered that I had forgotten to add some lists to the reset function. Once I added these lists, the new game printed the boards as correctly.

6. During testing of playing beyond one round, I found that the game would malfunction in that the CLI would accept any input but would not provide any feedback at all. This bug would occur after a few guesses were made by the player. The number of guesses before the game hung varied. Eventually I realised that this was because one of the lists that stored all of teh guesses made by the CPU was not cleared at the end of round one. So once all of the remianing coordinates not yet picked by the CPU were eventually picked, the CPU was not able to make and more guesses. Addign this list to the function for resetting the CPUS guesses at the end of a round fixed this bug. 

* Remaining Bugs:
* None that I'm aware of.

## Validator Testing:
* PEP8 online was used to test the code. No errors were found.

## Deployment:
 
## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

-----
Happy coding!
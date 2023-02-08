# Tron

This challenge will heavily test the skills of using classes and interacting between them. Your task is to make a game where two players face off in a game of [light cycles](https://www.youtube.com/watch?v=SqSuRdkglxM) from Tron.

## Game board

This is an example of a game:

1. It is 56 turns in.
2. The board is 40 * 20 squares (playable area)
3. There are 2 players

```txt
 ----------------------------------------
|                    o-------------o     |
|                           o---o  |     |
|                           |   |  |     |
|                           |   |  |     |
|                           |   |  |     |
|                 o---------o   |  |     |
|                oo             |  |     |
|           1----o              o--o     |
|     2--o                               |
|        |    o--------------o           |
|        |    |              |           |
|        |    |      o------o|           |
|        |    |      |      ||           |
|        o----o      |      ||           |
|                    |      oo           |
|                    |                   |
|                    |                   |
|                    |                   |
|                    |                   |
|                    o                   |
 ----------------------------------------
```

## Level format

To play the game a level file will be loaded that will contain information about the game to be played. This is the format of the game above:

```json title=board.json
{
    "Size": [40, 20],
    "Players": {
        "1": [20, 0],
        "2": [20, 19]
    },
    "Points": {
        "Kill": 10,
        "Survivor": 10,
        "Suicide": -5
    }
}
```

The file format is in `json`.

1. The numbers in size must be integers greater than 0.
2. The number of players may change, but their spawning positions must fit inside the board and not overlap with another player. The character on the left is the character that will be drawn to represent the player on the board. It must be a singular character. The spawning position must be an integer. The coordinates [x, y] is the top left of the board and [0, 0] is the top left.
3. The points represents how many points each player gets for killing another player or being the last player standing.

## Running the game

To run the game you will type:

```bash
$ python tron.py board.json
```

If the user does not supply a board print:

`Usage: python tron.py [board.json]`

### Bad level format

Before starting the game, perform a few on `board.json` to make sure it is a valid file format. Here's what you should do if the `board.json` file is invalid. In each case, close the program after printing:

1. `board.json` does not exist

    ```bash
    Level file '{board}' does not exist.
    ```

2. There are less than 2 players.

    ```bash
    Must be at least 2 players to play.
    ```

3. Player's spawn is out of bounds.

    ```bash
    Player `{char}` spawns out of bounds.
    ```

4. Size is not 1x1 or larger.

    ```bash
    Board size must be greater than 1x1 or larger.
    ```

Any other errors to do with the format can simply just crash the program, so just assume it's correct beyond the above.

:::tip

Use the `json` module in Python to parse the file. Do not try to do this on your own. Hint: `json.loads()`.

:::

## Rules

At the start of each turn print: `Player {char}'s turn`, then print the board.

After that, wait for user input printing `> `.

A variety of commands will dictate how the player moves. Valid movements are turn left, turn right, and forward. Moving backwards is not allowed. These movements will be controlled by user input. This is what should happen you each user input while the game is being played.

- `help` Display a help message of the list of commands available to the player.
- `a` Move left
- `d` Move right
- `w` Move up
- `s` Move down
- `score` Prints the scoreboard
- `quit` Prints the scoreboard then closes the app.
- `board` Print the board again.
- Any other invalid input should print: `Use 'help' for a list of commands`

If the movement is invalid, then print: `Can't move backwards, try again`.

Once a player has moved on their turn, rotate turns to the next player. This means that there could be more than 2 players. There could be 10 players in the game!

A player dies if they run into a wall or a trail of their own.

- If you die to a wall, then the closest player (Manhattan distance) receives the points for the kill.
- If you die to a trail of another player or directly run into another player, they get the kill points.
- If you die to your own trail then the suicide points are awarded to you. (Usually negative).
- As soon as you die, all your trails are wiped from the map.

When there is one player remaining, print the board saying they won, then start a new round. Continue playing rounds until a user types `quit`.

## Example

```json title=small.json
{
    "Size": [7, 4],
    "Players": {
        "1": [3, 0],
        "2": [3, 3]
    },
    "Points": {
        "Kill": 10,
        "Survivor": 5,
        "Suicide": -5
    }
}
```

```bash
$ python tron.py small.json
```

```txt
--- New Round ---
Player 1's turn
 ------- 
|   1   |
|       |
|       |
|   2   |
 ------- 
> score
Player 1: 0
Player 2: 0
> blah
Use 'help' for a list of commands
> d
Player 2's turn
 ------- 
|   -1  |
|       |
|       |
|   2   |
 ------- 
> w
Player 1's turn
 ------- 
|   -1  |
|       |
|   2   |
|   |   |
 ------- 
> s
Player 2's turn
 ------- 
|   -o  |
|    1  |
|   2   |
|   |   |
 ------- 
> d
Player 1's turn
 ------- 
|   -o  |
|    1  |
|   o2  |
|   |   |
 ------- 
> s
Player 2 wins
 ------- 
|       |
|       |
|   o2  |
|   |   |
 ------- 
--- New Round ---
Player 1's turn
 ------- 
|   1   |
|       |
|       |
|   2   |
 -------
> quit
Player 1: 0
Player 2: 15
```

Any other commands or details are free to be interpreted however you like.

This game touches on many concepts and one of the biggests challenges will be your architecture.

- How are you going to structure your classes?
- What class interactions make sense?
- Where should logic go?
- What functions or methods are you going to write?
- How am I going to handle user input and printing?

All of this is up to you to decide. As you improve as a programmer you will come back to this challenge and learn better ways to solve the problem.

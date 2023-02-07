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
        "1": [20, 19],
        "2": [20, 0],
    },
    "Points": {
        "Kill": 10,
        "Survivor": 10
    }
}
```

The take-aways is that the file format is `json`.
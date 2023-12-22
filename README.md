tbd

## Installation Instructions
1. [Install VS Code & Python](https://code.visualstudio.com/docs/python/python-tutorial)
   1. Install Python3.10+ (newer the better!)
   2. Install Python extension
2. git clone https://github.com/zacmccul/unknown.git in VS Code
3. `python -m venv .venv`
4. `.venv/Scripts/activate` depending on the system may need .bat, .ps1, or just activate.
5. Copy `rummi.pth` to `.venv/Lib/site-packages` and replace `YOUR_USER_PATH/tests` with the ABSOLUTE (e.g. C:\\Users etc.) paths to tests and src. This is to make python unit test for pre-commit work correctly.
6. `pip install -r requirements.txt`
7. `pre-commit install`  (prefix with python -m if pre-commit isn't found)
8. `pre-commit run --all-files`
9. Set up VS Code Test Cases (unittest, tests/ directory, \*test\*.py option)


## Roadmap

### Requirements


1. An understanding of the actual rules
   1. Write a document describing what the rules, how to code that etc.
2. Start with text interface first
   1. Write functions that doOutput(), and have the initial version be text and we can then come back later
        and replace/add a UI function instead
3. Graphics????
4. AI players (might be hard)
5. Board, up to four/five players each have their hand, each player has like a melded area, and players can meld on other players.
   1. Code to represent a tile.
   2. code to represent a board.
   3. A hand
   4. A meld area
   5. A player
   6. Game state

Game State: Players & Board
Board: includes the center pieces & other general info, whose turn it is, turn order, etc.
Player: AI or human, a hand, a meld area
A bunch of these include tiles.



TDD: Test Driven Development.
Normal process of: Read the problem, figure out a solution, write a solution, add test cases & debug.
TDD process: Read the problem, write test cases that test if the code meets the requirements, then write code to turn failing tests into passing tests. Once all tests are passed, that is a working solution if the test cases are complete.

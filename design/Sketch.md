```mermaid
graph TD;
    A-->B;
    A-->C;
    B-->D;
    C-->D;
```


Player:
1. Current hand, which is a list of tiles?
2. FirstMeld or not
3.

board:
1. Wall
2. createWall or shuffleTiles
3.

Tiles:
1. Tile Number & Color
2. getScore()


GameState
1. CalculateWinner
   1. Sum getScore for each player
2. Whose turn it is
3. Turn order
4.

```mermaid
---
title: GameState
---
classDiagram

    class GameState{
      +int whose_turn
      +list[int] scores
      +Board board
      +list[Player] players
      +next_turn()
      +save_state()
      +load_state()
      +valid_actions() list[Action]
      +calculate_score() list[int]
    }
    class Player{
      +bool is_human
      +hand: list[Tile]
      +bool: melded
      +take_turn(GameState)
      +calculate_score() int
    }
    class AI{
      +choose_action(GameState)
    }
    class Human{
      +choose_action(GameState)
    }
    class Board{
      +list[Tile] wall
      +grab_tile() Tile
      +setup()
    }
    class Action{
      +__repr__() str
    }
    class Tile{
      +str: color
      +int: value
    }
    Player <|-- AI
    Player <|-- Human

```

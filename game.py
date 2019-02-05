#!/usr/bin/env python3

import random

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""

"""The Game is a default of 5 rounds. If no winner can be determined,
it will restart itself until a final winner is found"""


class Player:
    # always plays rock
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):
    # uses a random move
    def move(self):
        return random.choice(moves)


class RotatingPlayer(Player):
    # rotates through the moves
    def __init__(self):
        self.rotation_index = 0

    def move(self):
        if self.rotation_index == 0:
            self.rotation_index = 1
            return 'rock'
        elif self.rotation_index == 1:
            self.rotation_index = 2
            return 'paper'
        else:
            self.rotation_index == 0
            return 'scissors'


class Copycat(Player):
    # copies the last player move
    def __init__(self):
        # copycat starts with rock too
        # since it cant copy anything in the first round
        self.last_move = 'rock'

    def learn(self, my_move, their_move):
        self.last_move = their_move

    def move(self):
        return self.last_move


class ManualPlayer(Player):
    def move(self):
        while True:
            move = input('Rock, Paper or Scissors?:/t').lower()
            if 'rock' in move:
                return 'rock'
            elif 'scissors' in move:
                return 'scissors'
            elif 'paper' in move:
                return 'paper'


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


def draw(one, two):
    return one == two


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        # ok there is no draw and the game gets restarted (see below)
        # since score is set here it will not get reset when the game restarts
        # for that to happen just introduce those instance variables in
        # play_game()
        self.p1.score = 0
        self.p2.score = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        if beats(move1, move2):
            print('PLAYER 1 WINS')
            self.p1.score += 1
        elif draw(move1, move2):
            print('DRAW')
        else:
            print('PLAYER 2 WINS')
            self.p2.score += 1
        print(f'Score: Player 1: {self.p1.score}\t Player 2: {self.p2.score}')

    def play_game(self):
        print("Game start!")
        # it will by default play 5 rounds but ties are not acceptable
        for round in range(5):
            # i know were supposed to be programmers starting with 0
            # but round 0? whats that supposed to be?
            print(f"Round {round + 1}:")
            self.play_round()
        print("Game over!")
        if self.p1.score > self.p2.score:
            print(f'Player 1 won with {self.p1.score}:{self.p2.score} points!')
        elif self.p1.score < self.p2.score:
            print(f'Player 2 won with {self.p2.score}:{self.p1.score} points!')
        else:
            # real draws dont exist in my game it forces you to play again
            print('Its a draw. Play again!')
            self.play_game()


if __name__ == '__main__':
    # when called as a main it will let a human player play randomly
    # against one of the 4 bots
    game = Game(ManualPlayer(), random.choice([RandomPlayer(), Player(),
                                               RotatingPlayer(), Copycat()]))
    game.play_game()

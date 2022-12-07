from enum import IntEnum
from abc import ABC, abstractmethod


class Winner(IntEnum):
    OPPONENT = 0
    DRAW = 3
    PLAYER = 6


class Choice(ABC):
    def beats(self, other: 'Choice') -> bool:
        return type(self.wins_to()) == type(other)

    @abstractmethod
    def wins_to(self) -> 'Choice':
        pass

    @abstractmethod
    def loses_to(self) -> 'Choice':
        pass

    @abstractmethod
    def points(self) -> int:
        pass


class Rock(Choice):
    def wins_to(self) -> Choice:
        return Scissors()

    def loses_to(self) -> Choice:
        return Paper()

    def points(self) -> int:
        return 1


class Paper(Choice):
    def wins_to(self) -> Choice:
        return Rock()

    def loses_to(self) -> Choice:
        return Scissors()

    def points(self) -> int:
        return 2


class Scissors(Choice):
    def wins_to(self) -> Choice:
        return Paper()

    def loses_to(self) -> Choice:
        return Rock()

    def points(self) -> int:
        return 3


def to_choice(guide_char: str) -> Choice:
    if guide_char == 'A' or guide_char == 'X':
        return Rock()
    if guide_char == 'B' or guide_char == 'Y':
        return Paper()
    if guide_char == 'C' or guide_char == 'Z':
        return Scissors()
    raise Exception(f'{guide_char} is not a thing')


def handle_game_part1(input_line: str) -> int:
    """
    Return the amount of points the player gets for this game
    """
    opponent_choice, player_choice = [to_choice(x) for x in input_line.strip().split(' ')]
    winner = who_wins(opponent_choice, player_choice)
    return player_choice.points() + winner


def who_wins(player1_choice, player2_choice) -> Winner:
    if type(player1_choice) == type(player2_choice):
        return Winner.DRAW
    if player1_choice.beats(player2_choice):
        return Winner.OPPONENT
    else:
        return Winner.PLAYER


def to_result(desired_result: str) -> Winner:
    if desired_result == 'X':
        return Winner.OPPONENT
    if desired_result == 'Y':
        return Winner.DRAW
    if desired_result == 'Z':
        return Winner.PLAYER


def what_to_play(opponents_choice: Choice, desired_result: Winner):
    if desired_result == Winner.DRAW:
        return opponents_choice

    if desired_result == Winner.PLAYER:
        return opponents_choice.loses_to()
    if desired_result == Winner.OPPONENT:
        return opponents_choice.wins_to()



def handle_game_part2(input_line: str) -> int:
    line_parts = input_line.strip().split(' ')
    opponent_choice = to_choice(line_parts[0])
    desired_result = to_result(line_parts[1])
    my_choice = what_to_play(opponent_choice, desired_result)
    points = my_choice.points() + desired_result
    return points



with open("input.txt") as infile:
    total_points_part1 = 0
    total_points_part2 = 0
    for line in infile:
        total_points_part1 = total_points_part1 + handle_game_part1(line)
        total_points_part2 = total_points_part2 + handle_game_part2(line)

    print(f"Total points (for part 1): {total_points_part1}")
    print(f"Total points (for part 2): {total_points_part2}")



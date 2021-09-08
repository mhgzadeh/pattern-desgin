from abc import ABC, abstractmethod
from random import choice


class PlayerBase(ABC):
    choices = ['r', 'p', 's']

    @abstractmethod
    def move(self):
        pass


class HumanPlayer(PlayerBase):
    def move(self):
        return input('Choose your next move ... ')


class SystemPlayer(PlayerBase):
    def move(self):
        return choice(self.choices)


class Game:

    @staticmethod
    def start_game():
        game_type = input(
            "please choose game type ('s': system player, 'm': multiple player: "
        )
        if game_type == 's':
            p1 = HumanPlayer()
            p2 = SystemPlayer()
        elif game_type == 'm':
            p1 = HumanPlayer()
            p2 = HumanPlayer()
        else:
            print('Invalid input.')
            p1 = None
            p2 = None
        return p1, p2


if __name__ == '__main__':
    game = Game()
    player_1, player_2 = game.start_game()

    for player in [player_1, player_2]:
        print(player.move())

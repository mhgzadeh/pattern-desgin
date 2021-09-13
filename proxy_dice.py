from random import randint


class User:
    def __init__(self, name):
        self.name = name


class Dice:
    @staticmethod
    def roll():
        return randint(1, 6)


class Game:
    def __init__(self, u1, u2):
        self.user1 = u1
        self.user2 = u2
        self.turn = u1
        self.dice = Dice
        
    def change_turn(self):
        self.turn = self.user2 if self.turn == self.user1 else self.user1

    def roll_dice(self, user):
        if self.turn == user:
            self.change_turn()
            return self.dice.roll()
        return "It's not your turn."


if __name__ == '__main__':

    user1 = User('Mohammad')
    user2 = User('Amin')

    game = Game(user1, user2)

    print(game.roll_dice(user2))
    print(game.roll_dice(user2))
    print(game.roll_dice(user1))
    print(game.roll_dice(user2))
    print(game.roll_dice(user2))
    print(game.roll_dice(user2))
    print(game.roll_dice(user1))
    print(game.roll_dice(user2))

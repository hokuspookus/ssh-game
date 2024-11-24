import os
import time
import keyboard
import cursor

cursor.hide()

PLAYING: bool = True
WIDTH: int = 20
HEIGHT: int = 20
REFRESH_RATE: float = 0.10


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def fprint(string) -> None:
    print(string, end='')


class Position:
    def __init__(self, x: int, y: int):
        self.x: int = x
        self.y: int = y

    def __repr__(self):
        return f"({self.x}, {self.y})"


class Player:
    def __init__(self):
        self.pos: Position = Position(10, 10)
        self.health: int = 100
        print("Created Player!")

    def clamp(self):
        if self.pos.x < 2: self.pos.x = 2
        if self.pos.x > WIDTH-1: self.pos.x = WIDTH-1
        if self.pos.y < 2: self.pos.y = 2
        if self.pos.y > HEIGHT-1: self.pos.y = HEIGHT-1

    def up(self):
        self.pos.y -= 1

    def down(self):
        self.pos.y += 1

    def left(self):
        self.pos.x -= 1

    def right(self):
        self.pos.x += 1


def print_stats() -> None:
    fprint('\nHealth: [')
    fprint('-' * int(Tim.health / 10))
    fprint(' ' * (10 - int(Tim.health / 10)))
    print(']')

    print(f'Pos: {Tim.pos}')


clear()
Tim = Player()

while PLAYING:
    clear()
    for i in range(HEIGHT):
        print('|', end='')

        if i == 0 or i == (HEIGHT - 1):
            print('-' * (WIDTH - 2), end='')
        elif (i + 1) == Tim.pos.y:
            print(' ' * (Tim.pos.x - 2), end='')
            print('@', end='')
            print(' ' * (WIDTH - Tim.pos.x - 1), end='')
        else:
            print(' ' * (WIDTH - 2), end='')

        print('|')

    print_stats()

    time.sleep(0.25)
    key = keyboard.read_key()

    if key == 'w':
        Tim.up()
    if key == 's':
        Tim.down()
    if key == 'a':
        Tim.left()
    if key == 'd':
        Tim.right()
    if key == '+':
        WIDTH += 10
    if key == '-':
        WIDTH -= 10

    Tim.clamp()

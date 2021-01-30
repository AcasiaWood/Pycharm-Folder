import pygame
import random
from datetime import datetime
from datetime import timedelta

# define the screen size
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
BLOCK_SIZE = 20

# RGB
RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
GRAY = (127, 127, 127)

# reset the game
pygame.init()
pygame.display.set_caption('snake_game')

# create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


# define the rectangle
def draw_background(screen):
    background = pygame.Rect((0, 0), (SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.draw.rect(screen, WHITE, background)


def draw_block(screen, color, position):
    block = pygame.Rect(
        (position[0] * BLOCK_SIZE, position[1] * BLOCK_SIZE),
        (BLOCK_SIZE, BLOCK_SIZE)
    )
    pygame.draw.rect(screen, color, block)


def draw_lines(screen, color):
    for i in range(int(SCREEN_WIDTH / 20)):
        pygame.draw.line(screen, color, (i * BLOCK_SIZE, 0), (i * BLOCK_SIZE, SCREEN_HEIGHT), 1)
        pygame.draw.line(screen, color, (0, i * BLOCK_SIZE), (SCREEN_WIDTH, i * BLOCK_SIZE), 1)


# snake`s arrow
class Offset:
    NONE = [0, 0]
    RIGHT = [1, 0]
    LEFT = [-1, 0]
    UP = [0, -1]
    DOWN = [0, 1]


# define the color and location
class Snake:
    # enter the snake`s color and location and direction
    def __init__(self, color, position, offset):
        self.color = color
        self.offset = offset
        self.positions = [
            position,
            [position[0], position[1] + 1],
            [position[0], position[1] + 2],
            [position[0], position[1] + 3]
        ]

    def draw(self):
        for position in self.positions:
            draw_block(screen, self.color, position)

    def move(self):
        now_position = [self.positions[0][0], self.positions[0][1]]
        self.positions[0][0] += self.offset[0]
        self.positions[0][1] += self.offset[1]
        last_position = now_position
        for i in range(1, len(self.positions)):
            now_position = [self.positions[i][0], self.positions[i][1]]
            self.positions[i] = last_position
            last_position = now_position

    def growth(self):
        end_tail = self.positions[-1]
        front_tail = self.positions[-2]
        x_diff = end_tail[0] - front_tail[0]
        y_diff = end_tail[1] - front_tail[1]
        self.positions.append([end_tail[0] + x_diff, end_tail[1] + y_diff])

    pass


# define the color and location
class Apple:
    # enter the apple color and location
    def __init__(self, color, position):
        self.color = color
        self.position = position

    def draw(self):
        draw_block(screen, self.color, self.position)

    pass


# define the snake game
class Game:
    def __init__(self, snake, apple):
        self.snake = snake
        self.apple = apple

    def draw(self):
        draw_background(screen)
        self.apple.draw()
        self.snake.draw()
        pygame.display.update()

    def crash(self):
        snake_head = self.snake.positions[0]
        if snake_head in self.snake.positions[1:]:
            return True
        if snake_head[0] > 19 or snake_head[1] > 19 or snake_head[0] < 0 or snake_head[1] < 0:
            return True
        return False

    def start(self):
        last_movement = datetime.now()
        move_flag = True
        while True:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    exit()
                elif event.type == pygame.KEYDOWN and move_flag:
                    move_flag = False
                    if event.key == pygame.K_RIGHT and self.snake.offset != Offset.LEFT:
                        self.snake.offset = Offset.RIGHT
                    elif event.key == pygame.K_LEFT and self.snake.offset != Offset.RIGHT:
                        self.snake.offset = Offset.LEFT
                    elif event.key == pygame.K_DOWN and self.snake.offset != Offset.UP:
                        self.snake.offset = Offset.DOWN
                    elif event.key == pygame.K_UP and self.snake.offset != Offset.DOWN:
                        self.snake.offset = Offset.UP
            if timedelta(milliseconds=150) <= datetime.now() - last_movement:
                move_flag = True
                self.snake.move()
                last_movement = datetime.now()
            if self.apple.position == self.snake.positions[0]:
                while self.apple.position in self.snake.positions:
                    self.apple.position = [random.randint(0, 19), random.randint(0, 19)]
                self.snake.growth()
            if self.crash():
                break
            self.draw()

    pass


game = Game(
    Snake(GREEN, [9, 9], Offset.RIGHT),
    Apple(RED, [5, 5])
)
game.start()

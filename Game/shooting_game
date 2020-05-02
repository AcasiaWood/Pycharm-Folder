import pygame
import random

# define the color
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# define the display
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 700

# ship object class
class ShipSprite(pygame.sprite.Sprite):
    def __init__(self, image_size=(0, 0), position=[0, 0]):
        super().__init__()
        self.sprite_src = 'img/ship.png'  # ship image path
        self.sprite_size = image_size  # ship image size
        self.sprite_pos = position  # ship location

        # movement flag
        self.move_flag = {
            pygame.K_RIGHT: False,
            pygame.K_LEFT: False,
            pygame.K_UP: False,
            pygame.K_DOWN: False
        }

        # ship speed
        self.speedX = 5
        self.speedY = 5

        # load the ship image and increase the image size for sprite_size
        origin_img = pygame.image.load(self.sprite_src)
        self.sprite_sheet = pygame.transform.scale(origin_img, (self.sprite_size[0], self.sprite_size[1]))

        # draw the surface of the loaded image
        self.image = pygame.Surface((self.sprite_size[0], self.sprite_size[1]))  # draw the surface
        self.image.set_colorkey(BLACK)  # set the background color (투명)
        # send the bit to the loaded image surface
        self.image.blit(self.sprite_sheet, (0, 0))
        # create the rectangle from the surface
        self.rect = self.image.get_rect()

    def update(self, *args):
        # execute the x, y movement about available move_flag
        if self.move_flag[pygame.K_RIGHT] and self.sprite_pos[0] < SCREEN_WIDTH - self.sprite_size[0]:
            self.sprite_pos[0] += self.speedX
        if self.move_flag[pygame.K_LEFT] and self.sprite_pos[0] > 0:
            self.sprite_pos[0] -= self.speedX
        if self.move_flag[pygame.K_UP] and self.sprite_pos[1] > 0:
            self.sprite_pos[1] -= self.speedY
        if self.move_flag[pygame.K_DOWN] and self.sprite_pos[1] < SCREEN_HEIGHT - self.sprite_size[1]:
            self.sprite_pos[1] += self.speedY
        self.rect.x = self.sprite_pos[0]
        self.rect.y = self.sprite_pos[1]
        pass

    def key_down(self, key):
        if key in self.move_flag.keys():
            self.move_flag[key] = True

    def key_up(self, key):
        if key in self.move_flag.keys():
            self.move_flag[key] = False

# bullet object class
class BulletSprite(pygame.sprite.Sprite):
    def __init__(self, image_size=(0, 0), position=[0, 0]):
        super().__init__()
        self.sprite_src = 'img/bullet.png'  # bullet image path
        self.sprite_size = image_size  # bullet image size
        self.sprite_pos = position  # bullet location

        # ship speed
        self.speed = 12

        # load the bullet image and increase the image size for sprite_size
        origin_img = pygame.image.load(self.sprite_src)
        self.sprite_sheet = pygame.transform.scale(origin_img, (self.sprite_size[0], self.sprite_size[1]))

        # draw the surface of the loaded image
        self.image = pygame.Surface((self.sprite_size[0], self.sprite_size[1]))  # draw the surface
        self.image.set_colorkey(BLACK)  # set the background transparency color
        # send the bit to the loaded image surface
        self.image.blit(self.sprite_sheet, (0, 0))
        # create the rectangle from the surface
        self.rect = self.image.get_rect()

    def update(self, *args):
        self.sprite_pos[1] -= self.speed
        self.rect = self.sprite_pos[1]

# bullet object group class
class BulletGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()

    def update(self):
        super().update()
        for bullet in self.sprites():
            if bullet.sprite_pos[1] < -bullet.sprite_pos[1]:
                self.remove(bullet)

    def key_down(self, key, ship_pos):
        if key == pygame.K_SPACE:
            new_bullet = BulletSprite(
                (32, 32),
                [ship_pos[0] + 9, ship_pos[1] - 32]
            )
            self.add(new_bullet)

    def draw(self, screen):
        for bullet in self.sprites():
            screen.blit(bullet.image, bullet.sprite_pos)

# enemy object class
class EnemySprite(pygame.sprite.Sprite):
    def __init__(self, image_size=(0, 0), position=[0, 0]):
        super().__init__()
        self.sprite_src = 'img/enemy.png'  # enemy image path
        self.sprite_size = image_size  # enemy image size
        self.sprite_pos = position  # enemy location

        # enemy speed
        self.speed = 3
        # enemy hp
        self.HP = 4

        # load the enemy image and increase the image size for sprite_size
        origin_img = pygame.image.load(self.sprite_src)
        self.sprite_sheet = pygame.transform.scale(origin_img, (self.sprite_size[0], self.sprite_size[1]))

        # draw the surface of the loaded image
        self.image = pygame.Surface((self.sprite_size[0], self.sprite_size[1]))  # draw the surface
        self.image.set_colorkey(BLACK)  # set the background transparency color
        # send the bit to the loaded image surface
        self.image.blit(self.sprite_sheet, (0, 0))
        # create the rectangle from the surface
        self.rect = self.image.get_rect()

    def update(self, *args):
        self.sprite_pos[1] += self.speed
        self.rect.y = self.sprite_pos[1]

class EnemyGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.frame_count = 0

    def update(self):
        super().update()
        for enemy in self.sprites():
            if enemy.sprite_pos[1] > SCREEN_HEIGHT:
                self.remove(enemy)
            if enemy.HP <= 0:
                self.remove(enemy)
        self.auto_add()

    def auto_add(self):
        # auto add the enemy sprite on the random x and execute as 120 frame
        if self.frame_count < 120:  # 60 FPS = 1 second
            self.frame_count += 1
        else:
            self.frame_count = 0
            new_enemy = EnemySprite((60, 60), [random.randint(0, 440), -60])
            self.add(new_enemy)

        pass

    def draw(self, screen):
        for enemy in self.sprites():
            screen.blit(enemy.image, enemy.sprite_pos)

# game management class
class Game:
    def __init__(self):
        # reset the module
        success, failure = pygame.init()
        print('{0} success, {1} failure'.format(success, failure))

        self.clock = pygame.time.Clock()  # a clock object to use tick function
        self.FPS = 60  # show the frame for a second
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # create the display
        pygame.display.set_caption("shooting_game")  # set the title of the game
        self.background_src = 'img/background.png'  # background image path
        self.playing = False  # game executed state
        self.background_first = 0  # first background image location
        self.background_second = -SCREEN_HEIGHT  # second background image location
        self.speed_background = 2  # background movement speed

        # load the background image and regulate the screen size
        background_origin = pygame.image.load(self.background_src)
        self.background_img = pygame.transform.scale(background_origin, (SCREEN_WIDTH, SCREEN_HEIGHT + 2))

        # ship object
        self.ship = ShipSprite((50, 50), [234, 550])

        # create the bullet group
        self.bullet_group = BulletGroup()

        # create the enemy group
        self.enemy_group = EnemyGroup()

    # a function to frame the game
    def execute(self):
        self.playing = True
        while self.playing:
            self.clock.tick(self.FPS)
            self.events()  # process the event
            self.update()  # update the game state
            self.draw()  # draw all the objects in the game

    def events(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.playing = False
            elif event.type == pygame.KEYDOWN:
                self.ship.key_down(event.key)
                self.bullet_group.key_down(event.key, self.ship.sprite_pos)
            elif event.type == pygame.KEYUP:
                self.ship.key_up(event.key)
        pass

    def background_update(self):
        # move the first background for y_coordinate
        # if first background get out the SCREEN_HEIGHT, change the first background`s coordinate to SCREEN_HEIGHT
        # second background is as same as above note
        if self.background_first >= SCREEN_HEIGHT:
            self.background_first = -SCREEN_HEIGHT
        else:
            self.background_first += self.speed_background

        if self.background_second >= SCREEN_HEIGHT:
            self.background_second = -SCREEN_HEIGHT
        else:
            self.background_second += self.speed_background
        pass

    def update(self):
        self.background_update()
        self.ship.update()
        self.bullet_group.update()
        self.enemy_group.update()
        pass

    def draw(self):
        self.screen.fill(WHITE)  # the screen surface is filled with white color
        # draw the background image
        self.screen.blit(self.background_img, (0, self.background_first))  # draw the first background image
        self.screen.blit(self.background_img, (0, self.background_second))  # draw the second background image
        self.screen.blit(self.ship.image, self.ship.sprite_pos)  # draw the ship image
        self.bullet_group.draw(self.screen)  # draw all the images in the bullet group
        self.enemy_group.draw(self.screen)  # draw all the images in the enemy group
        pygame.display.flip()  # update all the surface objects being in the game
        pass

game = Game()
game.execute()

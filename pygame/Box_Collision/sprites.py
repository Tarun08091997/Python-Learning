"""IT is used to create the player,enemy or tile anything that can be used as physical quantity"""
import pygame
import random

""" It creates a box sprite with a size_x,size_y size and color filled init having 
     center at a random place  """

class create_box(pygame.sprite.Sprite):
    def __init__(self,size_x,size_y,color):
        super().__init__()
        self.moving_speed_x = 3
        self.moving_speed_y = 2.5

        self.image = pygame.Surface((size_x,size_y))  ## it will create a image object using Surface
        self.image.fill(color) # it will fill 'color' in image surface
        self.rect = self.image.get_rect()     ## create rectangle aroung image Surface
        self.rect.center = (random.randint(150,1216),random.randint(50,718))

    def update(self):

        self.rect.x += self.moving_speed_x
        self.rect.y += self.moving_speed_y




"""This class create a static and a moving boxes as refrence of create_box
    update function will always update the next place for moving object and update it in the screen"""

class static_moving_collision():
    def __init__(self):
        self.static_box = create_box(200,100,'blue')
        self.static_group = pygame.sprite.Group(self.static_box)
        self.static_box.rect.center = (700,350)
        self.moving_box = create_box(100,100,'red')
        self.moving_group = pygame.sprite.Group(self.moving_box)



    def check_collision(self):
        # if moving box right goes beyond width or moving box left goes beyond 0 => x -ve motion
        # if upper side goes beyond zeo or down side goes beyon height => -ve y motion
        if self.moving_box.rect.right >= 1366 or self.moving_box.rect.left <= 0:
            self.moving_box.moving_speed_x *= -1
            self.moving_box.image.fill((random.randint(0,255),random.randint(0,255),random.randint(0,255)))

        if self.moving_box.rect.top <= 0 or self.moving_box.rect.bottom >= 768 :
            self.moving_box.moving_speed_y *= -1
            self.moving_box.image.fill((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

        self.tolerence = 10

        if self.moving_box.rect.colliderect(self.static_box.rect):
            if abs(self.moving_box.rect.right - self.static_box.rect.left) < self.tolerence or \
                    abs(self.moving_box.rect.left - self.static_box.rect.right) < self.tolerence:
                self.moving_box.moving_speed_x *= -1
                self.moving_box.image.fill((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
                self.static_box.image.fill((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

            if abs(self.moving_box.rect.bottom - self.static_box.rect.top) < self.tolerence or \
                    abs(self.moving_box.rect.top - self.static_box.rect.bottom) < self.tolerence:
                self.moving_box.moving_speed_y *= -1
                self.moving_box.image.fill((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
                self.static_box.image.fill((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))


    def update(self, screen):

        self.moving_group.update()  ## the sprite_group has override method from the class of sprite added in it
        screen.fill('gray')
        self.static_group.draw(screen)
        self.moving_group.draw(screen)
        pygame.display.update()

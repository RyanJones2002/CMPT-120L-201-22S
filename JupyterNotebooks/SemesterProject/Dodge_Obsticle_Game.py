

import pygame
from pygame.locals import *
import time
import random

#Window size & Variables
WIDTH = 400
HEIGHT = 500
ACC = 0.5
FRIC = -0.12
FPS = 60
SPEED = 5
SCORE = 0

#Defining colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
magenta = pygame.Color(255, 0, 255)
yellow = pygame.Color(255, 255, 0)
cyan = pygame.Color(0, 255, 255)
blue = pygame.Color(0, 0, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)

#Initialising pygame
pygame.init()
vec = pygame.math.Vector2

#Initialise game window & setting caption
pygame.display.set_caption('Dodge Obsticle Game')
game_window = pygame.display.set_mode((WIDTH, HEIGHT))

#FPS (frames per second) controller
FramePerSec = pygame.time.Clock()

#Displaying Score function
def show_score(choice, color, font, size):

	#Creating font object score_font
	score_font = pygame.font.SysFont(font, size)
	
	#Create the display surface object
	score_surface = score_font.render('Score : ' + str(SCORE), True, color)
	
	#Create a rectangular object for the text surface object
	score_rect = score_surface.get_rect()
	
	#Displaying text
	game_window.blit(score_surface, score_rect)

#Defining the player 
class Player(pygame.sprite.Sprite):

    #Initilizing player attributes
    def __init__(self):

        #Super function allows us to avoid using base class name explicitly
        super().__init__()

        #Adding size
        self.surf = pygame.Surface((25,25))

        #Adding color
        self.surf.fill((magenta))

        #Defining shape & center
        self.rect = self.surf.get_rect(center = (200, 450))

        #Defining starting position
        self.pos = vec((200, 450))

        #Defining starting velocity
        self.vel = vec(0,0)

        #Defining starting acceleration
        self.acc = vec(0,0)

    #creating player movement
    def move(self):

        #Defining starting acceleration
        self.acc = vec(0,0)

        #When L/R arrow key pressed, -/+ acceleration in corresponding direction
        pressed_keys = pygame.key.get_pressed() 
        if pressed_keys[K_LEFT]:
            self.acc.x = -ACC
        if pressed_keys[K_RIGHT]:
            self.acc.x = ACC  

        #Calculating new position based on key pressed with respect to velocity, friction, & acceleration
        self.acc.x += self.vel.x * FRIC
        self.vel += self.acc
        self.pos += self.vel + .5 * self.acc

        #Wrap around screen feature
        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH

        #returns the point at the center of the bottom of the rectangle
        self.rect.midbottom = self.pos

#Defining the first object
class Object(pygame.sprite.Sprite):

      #Initilizing objects attributes
      def __init__(self):

        #Super function allows us to avoid using base class name explicitly
        super().__init__() 

        #Adding size
        self.surf = pygame.Surface((25,25))

        #Adding color
        self.surf.fill((cyan)) 

        #Get rectangle object
        self.rect = self.surf.get_rect()

        #Making the center of the object spawn randomly along top of display
        self.rect.center=(random.randint(40,WIDTH-40),0)

      #Creating object movement  
      def move(self):

        #Moves object down 10 pixels
        self.rect.move_ip(0,10)

        #Allows you to modify variable (score) outside of current scope 
        global SCORE

        #Checks if top of object has reached end of screen and if true, resets at random location along x-axis
        if (self.rect.top > 500):
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)

            #Increase score when object passes
            SCORE += 5 

      #Blit() takes 2 inputs (surface & object) & draws rectangle to image (the surface)
      def draw(self, surface):
        surface.blit(self.image, self.rect) 

#Definations are constant for remaining objects

#Defining the 2nd object
class Object_2(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.surf = pygame.Surface((30,30))
        self.surf.fill((yellow)) 
        self.rect = self.surf.get_rect()
        self.rect.center=(random.randint(40,WIDTH-40),0) 
      def move(self):
        self.rect.move_ip(0,12)
        global SCORE
        if (self.rect.top > 500):
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)
            SCORE += 5 
            
        
      def draw(self, surface):
        surface.blit(self.image, self.rect) 

#Defining the 3rd object
class Object_3(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.surf = pygame.Surface((30,30))
        self.surf.fill((blue)) 
        self.rect = self.surf.get_rect()
        self.rect.center=(random.randint(40,WIDTH-40),0) 
      def move(self):
        self.rect.move_ip(0,8)
        global SCORE
        if (self.rect.top > 500):
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)
            SCORE += 5 
            
      def draw(self, surface):
        surface.blit(self.image, self.rect)

#Defining the 4th object
class Object_4(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.surf = pygame.Surface((40,40))
        self.surf.fill((red)) 
        self.rect = self.surf.get_rect()
        self.rect.center=(random.randint(40,WIDTH-40),0) 
      def move(self):
        self.rect.move_ip(0,5)
        global SCORE
        if (self.rect.top > 500):
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)
            SCORE += 5 
            
      def draw(self, surface):
        surface.blit(self.image, self.rect) 

#Defining the 5th object
class Object_5(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.surf = pygame.Surface((35,35))
        self.surf.fill((green))
        self.rect = self.surf.get_rect()
        self.rect.center=(random.randint(40,WIDTH-40),0) 
      def move(self):
        self.rect.move_ip(0,10)
        global SCORE
        if (self.rect.top > 500):
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)
            SCORE += 5 
            
      def draw(self, surface):
        surface.blit(self.image, self.rect) 

#Game over function
def game_over():

	#Creating font object my_font
	my_font = pygame.font.SysFont('times new roman', 50)
	
	#Creating a text surface on which text will be drawn
	game_over_surface = my_font.render(
		'Your Score Is : ' + str(SCORE), True, magenta)
	
	#Create a rectangular object for the text surface object
	game_over_rect = game_over_surface.get_rect()
	
	#Setting position of the text
	game_over_rect.midtop = (WIDTH/2, HEIGHT/4)
	
	#Blit will draw the text on screen
	game_window.blit(game_over_surface, game_over_rect)
	pygame.display.flip()
	
	#After 3 seconds we will quit the program
	time.sleep(3)
	
	#Deactivating pygame library
	pygame.quit()
	
	#Quit the program
	quit()


#Defining the player sprite
P1 = Player() 

#Defining the object sprites
O1 = Object()
O2 = Object_2()
O3 = Object_3()
O4 = Object_4()
O5 = Object_5()

#Grouping the object sprites
objects = pygame.sprite.Group()
#Adding objects to group
objects.add(O1, O2, O3, O4, O5)

#Grouping all sprites
all_sprites = pygame.sprite.Group()
#Adding sprites to group
all_sprites.add(P1, O1, O2, O3, O4, O5)

#Increase speed every 1 second, new User event
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

#Game Loop
while True:

    #Cycle through all events occuring
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        if event.type == INC_SPEED:
            SPEED += 2

    #Filling background
    game_window.fill(black)

    #Move P1
    P1.move() 

    #Move & Re-draws all Sprites
    for entity in all_sprites:
        game_window.blit(entity.surf, entity.rect)
        entity.move()

    #End game on collision
    if pygame.sprite.spritecollideany(P1, objects):
        game_over()

    #Display score continuously
    show_score(1, white, 'times new roman', 20)

    #Refresh game screen
    pygame.display.update()

    #Frame Per Second /Refresh Rate
    FramePerSec.tick(FPS)










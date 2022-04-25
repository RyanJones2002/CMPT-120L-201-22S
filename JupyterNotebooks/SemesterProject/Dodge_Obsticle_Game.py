

# Need obsticle speed, obsticle direction and starting point, 

# Need player class, 
    #move function
    #Is hit function
    #   
# object class(ball),
    #move function
    #destroy function
#  list of objects of balls to keep track, 


from turtle import position
import pygame
import time
import random


# Window size
window_x = 400
window_y = 500

# defining colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
magenta = pygame.Color(255, 0, 255)
yellow = pygame.Color(255, 255, 0)
cyan = pygame.Color(0, 255, 255)

# Initialising pygame
pygame.init()

# Initialise game window
pygame.display.set_caption('Dodge Obsticle Game')
game_window = pygame.display.set_mode((window_x, window_y))

# FPS (frames per second) controller
fps = pygame.time.Clock()

# defining player default position
player_position = [200, 450]

# defining player speed?
player_speed = 15



# obsticle position
obsticle_position = [random.randrange(1, (window_x//10)) * 10,
				random.randrange(1, (window_y//10)) * 10]



obsticle_spawn = True

# initial score
score = 0

# displaying Score function
def show_score(choice, color, font, size):

	# creating font object score_font
	score_font = pygame.font.SysFont(font, size)
	
	# create the display surface object
	# score_surface
	score_surface = score_font.render('Score : ' + str(score), True, color)
	
	# create a rectangular object for the text
	# surface object
	score_rect = score_surface.get_rect()
	
	# displaying text
	game_window.blit(score_surface, score_rect)

# game over function
def game_over():

	# creating font object my_font
	my_font = pygame.font.SysFont('times new roman', 50)
	
	# creating a text surface on which text
	# will be drawn
	game_over_surface = my_font.render(
		'Your Score is : ' + str(score), True, magenta)
	
	# create a rectangular object for the text
	# surface object
	game_over_rect = game_over_surface.get_rect()
	
	# setting position of the text
	game_over_rect.midtop = (window_x/2, window_y/4)
	
	# blit will draw the text on screen
	game_window.blit(game_over_surface, game_over_rect)
	pygame.display.flip()
	
	# after 2 seconds we will quit the program
	time.sleep(2)
	
	# deactivating pygame library
	pygame.quit()
	
	# quit the program
	quit()

class Player:
    def __init__(self):
        self.positionX = 200
        self.positionY = 450
        self.rect = pygame.Rect(self.positionX,self.positionY,50,50)

    def getX(self):
        return self.positionX
    
    def getY(self):
        return self.positionY

    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    change_to = 'LEFT'
                    del self.rect
                    self.positionX -= 5
                    self.rect = pygame.Rect(self.positionX,self.positionY,50,50)
                    print("left", self.positionX)
                    self.render() 
                if event.key == pygame.K_RIGHT:
                    change_to = 'RIGHT'
                    del self.rect
                    self.positionX += 5
                    self.rect = pygame.Rect(self.positionX,self.positionY,50,50)
                    print("right", self.positionX)    
                    self.render()  
    
    def render(self):
        pygame.draw.rect(game_window,white,self.rect)
        pygame.display.update(self.rect)
        
       
player = Player()

# Main Function
while True:
	
	# handling key events
	# If two keys pressed simultaneously
	# we don't want player to move into two
	# directions simultaneously
    player.move()

	# displaying score countinuously
    game_window.fill(black)

	# Refresh game screen
    pygame.display.update()

	# Frame Per Second /Refresh Rat
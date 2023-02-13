# These are half of the classes used in the game
# May 27, 2021

# Import stuff
import pygame, sys, math, random

# Initialize pygame
pygame.init()

# Constants
BLACK = (0, 0, 0)
REAL_WHITE = (255, 255, 255)
WHITE = (131, 24, 161)
WIDTH = 800
HEIGHT = 600

# Wall class which creates the walls
class Wall(pygame.sprite.Sprite):
 
    def __init__(self, x, y, width, height, color):
 
        # Call the parent's constructor
        super().__init__()
 
        # Lets us make wall
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

# Previous block class used for enemies now, but I never changed the name
class Block(pygame.sprite.Sprite):
    def __init__(self, color):
        # Call the parent class (Sprite) constructor
        super().__init__()
        # Use image for slime
        self.image = pygame.image.load("slime.png").convert()
        # Set colorkey
        self.image.set_colorkey(BLACK)        
        self.rect = self.image.get_rect()

# Reusing winblock class I made for my midterm game
class WinBlock(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__()
        self.image = pygame.image.load("treasure_chest.png").convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()

# Class used to help with using sprite sheets
class SpriteSheet(object):
    def __init__(self, file_name):
        self.sprite_sheet = pygame.image.load(file_name).convert()
        
    def get_image(self, x, y, width, height):
        image = pygame.Surface([width, height]).convert()
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        image.set_colorkey(BLACK)
        return image 

# Class for the player character
class Player(pygame.sprite.Sprite):
    # Set speed vector
    change_x = 0
    change_y = 0
 
    def __init__(self, x, y):
        # Call the parent's constructor
        super().__init__()
        
        # Lists for the walking frames
        self.walking_frames_l = []
        self.walking_frames_r = []
        self.walking_frames_u = []
        self.walking_frames_d = []       
        
        # Sets default direction to facing right
        self.direction = "R"       
        
        # Get images from sprite sheet and append to respective list
        sprite_sheet = SpriteSheet("GreenCap24x27.png")
        image = sprite_sheet.get_image(0, 81, 24, 27)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(24, 81, 24, 27)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(48, 81, 24, 27)
        self.walking_frames_r.append(image)
        
        image = sprite_sheet.get_image(0, 54, 24, 27)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(24, 54, 24, 27)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(48, 54, 24, 27)
        self.walking_frames_l.append(image)
        
        image = sprite_sheet.get_image(0, 27, 24, 27)
        self.walking_frames_u.append(image)
        image = sprite_sheet.get_image(24, 27, 24, 27)
        self.walking_frames_u.append(image)
        image = sprite_sheet.get_image(48, 27, 24, 27)
        self.walking_frames_u.append(image)
        
        image = sprite_sheet.get_image(0, 0, 24, 27)
        self.walking_frames_d.append(image)
        image = sprite_sheet.get_image(24, 0, 24, 27)
        self.walking_frames_d.append(image)
        image = sprite_sheet.get_image(48, 0, 24, 27)
        self.walking_frames_d.append(image)         
        
        self.image = self.walking_frames_r[0]
        
        self.rect = self.image.get_rect()
        
        self.rect.y = y
        self.rect.x = x        
        
    def changespeed(self, x, y):
        # Allows for movement
        self.change_x += x
        self.change_y += y
        
        # Used to determine which direction player is facing
        # NOTE: If you've played the game you've probably noticed the animation is
        # pretty scuffed. I'm pretty sure it has to do with how the code below is
        # set up and how it interacts with the way player movement is implemented
        # I am pretty sure if I change the player movement system I could get the
        # walking animation to work correctly but this was when I was almost finished
        # and decided it wasnt worth it especially if I didn't work out. I also did
        # not want to risk breaking the game by changing the movement system so I
        # settled for the slightly messed up animation
        if x > 0:
            self.direction = "R"
        elif x < 0:
            self.direction = "L"
        elif y > 0:
            self.direction = "U"
        else:
            self.direction = "D"
        
        # Goes through the frames to create the walking animation
        if self.direction == "R":
            frame = (self.rect.x // 30) % len(self.walking_frames_r)
            self.image = self.walking_frames_r[frame]
        elif self.direction == "L":
            frame = (self.rect.x // 30) % len(self.walking_frames_l)
            self.image = self.walking_frames_l[frame]
        elif self.direction == "U":
            frame = (self.rect.y // 30) % len(self.walking_frames_u)
            self.image = self.walking_frames_u[frame]
        else:
            frame = (self.rect.y // 30) % len(self.walking_frames_d)
            self.image = self.walking_frames_d[frame]            
 
    # This method sets up for our movement and contains check so the player
    # doesn't go through things
    def move(self, walls, block_list):
        
        # Move left/right
        self.rect.x += self.change_x
 
        # Did we hit a wall?
        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
        for block in block_hit_list:
            # If we are moving right, set our right side to the left side of
            # the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right
                
        # Did we hit an enemy?
        block_hit_list = pygame.sprite.spritecollide(self, block_list, False)        
        for block in block_hit_list:
            # If we are moving right, set our right side to the left side of
            # the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right         
 
        # Move up/down
        self.rect.y += self.change_y
 
        # Check and see if we hit a wall
        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
        for block in block_hit_list:
            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom        
    
        # Check and see if we hit an enemy
        block_hit_list = pygame.sprite.spritecollide(self, block_list, False)
        for block in block_hit_list:
            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom               

# Class for the firballs thrown by the player, originally called bullets
# before I decided to go with a dungeon theme
class Bullet(pygame.sprite.Sprite):
    def __init__(self, start_x, start_y, dest_x, dest_y):
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        # Set up the image for the bullet
        self.image = pygame.image.load("fireball.png").convert()
        self.image.set_colorkey(BLACK)
 
        self.rect = self.image.get_rect()
 
        # Move the bullet to our starting location
        self.rect.x = start_x
        self.rect.y = start_y
 
        # Because rect.x and rect.y are automatically converted
        # to integers, we need to create different variables that
        # store the location as floating point numbers. Integers
        # are not accurate enough for aiming.
        self.floating_point_x = start_x
        self.floating_point_y = start_y
 
        # Calculation the angle in radians between the start points
        # and end points. This is the angle the bullet will travel.
        x_diff = dest_x - start_x
        y_diff = dest_y - start_y
        angle = math.atan2(y_diff, x_diff);
 
        # Taking into account the angle, calculate our change_x
        # and change_y. Velocity is how fast the bullet travels.
        velocity = 5
        self.change_x = math.cos(angle) * velocity
        self.change_y = math.sin(angle) * velocity
 
    def update(self):
 
        # The floating point x and y hold our more accurate location.
        self.floating_point_y += self.change_y
        self.floating_point_x += self.change_x
 
        # The rect.x and rect.y are converted to integers.
        self.rect.y = int(self.floating_point_y)
        self.rect.x = int(self.floating_point_x)
 
        # If the bullet flies of the screen, get rid of it.
        if self.rect.x < 0 or self.rect.x > WIDTH or self.rect.y < 0 or self.rect.y > HEIGHT:
            self.kill()
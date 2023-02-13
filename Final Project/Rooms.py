# The room classes took up a lot of space so I put them away separartely
# May 27, 2021

# Import stuff
import pygame, sys, math, random
from Classes import *

# Initialize pygame
pygame.init()

# Constants
BLACK = (0, 0, 0)
REAL_WHITE = (255, 255, 255)
WHITE = (131, 24, 161)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
WIDTH = 800
HEIGHT = 600

# Parent room class
class Room(object):
    # Each room has a list of walls, and of enemy sprites.
    wall_list = None
    enemy_sprites = None
    block_list = None
    win_block_list = None
 
    def __init__(self):
        self.wall_list = pygame.sprite.Group()
        self.enemy_sprites = pygame.sprite.Group()    
        self.block_list = pygame.sprite.Group()
        self.movingsprites = pygame.sprite.Group()
        self.win_block_list = pygame.sprite.Group()

# Spawn room
class Room0(Room):
    def __init__(self):
        super().__init__()
 
        # This is a list of walls. Each is in the form [x, y, width, height]
        walls = [[0, 0, 20, 250, WHITE],
                 [0, 350, 20, 250, WHITE],
                 [780, 0, 20, 250, WHITE],
                 [780, 350, 20, 250, WHITE],
                 [20, 0, 760, 20, WHITE],
                 [20, 580, 760, 20, WHITE],
                 [120, 120, 440, 20, WHITE],
                 [540, 140, 20, 240, WHITE],
                 [540, 380, 120, 20, WHITE],
                 [660, 20, 20, 380, WHITE],
                 [120, 240, 20, 220, WHITE],
                 [140, 240, 120, 20, WHITE],
                 [240, 260, 20, 100, WHITE],
                 [260, 340, 180, 20, WHITE],
                 [440, 240, 20, 240, WHITE],
                 [460, 460, 220, 20, WHITE],
                 [540, 480, 20, 120, WHITE],
                 [340, 140, 20, 100, WHITE],
                 ]
                 
 
        # Loop through the list. Create the wall, add it to the list
        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)
        
        # Place the enemies
        # I did this indiviually and probably could have created a class or function
        # to make the process easier
        block = Block(RED)
        block.rect.x = 40
        block.rect.y = 500
        self.block_list.add(block)
        self.movingsprites.add(block)
        block = Block(RED)
        block.rect.x = 130
        block.rect.y = 179
        self.block_list.add(block)
        self.movingsprites.add(block)
        block = Block(RED)
        block.rect.x = 160
        block.rect.y = 300
        self.block_list.add(block)
        self.movingsprites.add(block)
        block = Block(RED)
        block.rect.x = 320
        block.rect.y = 300
        self.block_list.add(block)
        self.movingsprites.add(block)
        block = Block(RED)
        block.rect.x = 480
        block.rect.y = 550
        self.block_list.add(block)
        self.movingsprites.add(block) 
        block = Block(RED)
        block.rect.x = 380
        block.rect.y = 180
        self.block_list.add(block)
        self.movingsprites.add(block)
        block = Block(RED)
        block.rect.x = 600
        block.rect.y = 520
        self.block_list.add(block)
        self.movingsprites.add(block)
        block = Block(RED)
        block.rect.x = 720
        block.rect.y = 80
        self.block_list.add(block)
        self.movingsprites.add(block)
        block = Block(RED)
        block.rect.x = 720
        block.rect.y = 440
        self.block_list.add(block)
        self.movingsprites.add(block)

class Room1(Room):
    def __init__(self):
        super().__init__()
 
        walls = [[0, 0, 20, 250, WHITE],
                 [0, 350, 20, 250, WHITE],
                 [780, 0, 20, 250, WHITE],
                 [780, 350, 20, 250, WHITE],
                 [20, 0, 760, 20, WHITE],
                 [20, 580, 760, 20, WHITE],
                 [240, 20, 20, 100, WHITE],
                 [560, 120, 220, 20, WHITE],
                 [20, 350, 100, 20, WHITE],
                 [560, 140, 20, 100, WHITE],
                 [560, 240, 100, 20, WHITE],
                 [660, 240, 20, 120, WHITE],
                 [120, 470, 560, 20, WHITE],
                 [240, 370, 20, 100, WHITE],
                 [560, 370, 20, 100, WHITE],
                 [440, 120, 20, 240, WHITE],
                 [440, 360, 140, 20, WHITE],
                 [120, 120, 20, 100, WHITE],
                 [120, 220, 340, 20, WHITE],
                 ]
 
        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)
            
        block = Block(RED)
        block.rect.x = 240
        block.rect.y = 180
        self.block_list.add(block)
        self.movingsprites.add(block)
        block = Block(RED)
        block.rect.x = 720
        block.rect.y = 70
        self.block_list.add(block)
        self.movingsprites.add(block)
        block = Block(RED)
        block.rect.x = 650
        block.rect.y = 180
        self.block_list.add(block)
        self.movingsprites.add(block)
        block = Block(RED)
        block.rect.x = 720
        block.rect.y = 530
        self.block_list.add(block)
        self.movingsprites.add(block)
        block = Block(RED)
        block.rect.x = 70
        block.rect.y = 530
        self.block_list.add(block)
        self.movingsprites.add(block)
        block = Block(RED)
        block.rect.x = 330
        block.rect.y = 300
        self.block_list.add(block)
        self.movingsprites.add(block)
        block = Block(RED)
        block.rect.x = 330
        block.rect.y = 400
        self.block_list.add(block)
        self.movingsprites.add(block)
        block = Block(RED)
        block.rect.x = 540
        block.rect.y = 310
        self.block_list.add(block)
        self.movingsprites.add(block)
        block = Block(RED)
        block.rect.x = 660
        block.rect.y = 410
        self.block_list.add(block)
        self.movingsprites.add(block)
        
class Room2(Room):
    def __init__(self):
        super().__init__()
 
        walls = [[0, 0, 20, 350, WHITE],
                 [0, 350, 20, 250, WHITE],
                 [780, 0, 20, 250, WHITE],
                 [780, 350, 20, 250, WHITE],
                 [20, 0, 760, 20, WHITE],
                 [20, 580, 760, 20, WHITE]
                ]
 
        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)
            
        # For loops to place enemies in rows, probably could have used
        # a nested for loop but didn't realize till I was done
        z = 0  
        for i in range(10):
            block = Block(GREEN)
            block.rect.x = 55
            block.rect.y = 55 + z
            self.block_list.add(block)
            self.movingsprites.add(block)
            z += 50
         
        z = 0
        for i in range(10):
            block = Block(GREEN)
            block.rect.x = 105
            block.rect.y = 55 + z
            self.block_list.add(block)
            self.movingsprites.add(block)
            z += 50
        
        z = 0    
        for i in range(10):
            block = Block(GREEN)
            block.rect.x = 155
            block.rect.y = 55 + z
            self.block_list.add(block)
            self.movingsprites.add(block)
            z += 50
            
        z = 0    
        for i in range(10):
            block = Block(GREEN)
            block.rect.x = 205
            block.rect.y = 55 + z
            self.block_list.add(block)
            self.movingsprites.add(block)
            z += 50     
            
        z = 0    
        for i in range(10):
            block = Block(GREEN)
            block.rect.x = 255
            block.rect.y = 55 + z
            self.block_list.add(block)
            self.movingsprites.add(block)
            z += 50             
 
class Room3(Room):
    def __init__(self):
        super().__init__()

        walls = [[0, 0, 20, 250, WHITE],
                 [0, 350, 20, 250, WHITE],
                 [780, 0, 20, 250, WHITE],
                 [780, 350, 20, 250, WHITE],
                 [20, 0, 760, 20, WHITE],
                 [20, 580, 760, 20, WHITE],
                 [20, 350, 58, 20, WHITE],
                 [702, 230, 78, 20, WHITE],
                 [702, 250, 20, 116, WHITE],
                 [312, 484, 20, 96, WHITE],
                 [410, 484, 20, 96, WHITE],
                 [624, 464, 156, 20, WHITE],
                 [254, 20, 20, 232, WHITE],
                 [468, 20, 20, 96, WHITE],
                 [78, 116, 98, 20, WHITE],
                 [78, 136, 20, 96, WHITE],
                 [78, 232, 254, 20, WHITE],
                 [156, 252, 20, 96, WHITE],
                 [78, 464, 176, 20, WHITE],
                 [234, 348, 20, 116, WHITE],
                 [254, 348, 78, 20, WHITE],
                 [312, 232, 20, 116, WHITE],
                 [410, 464, 156, 20, WHITE],
                 [546, 348, 20, 116, WHITE],
                 [468, 348, 176, 20, WHITE],
                 [624, 116, 20, 232, WHITE],
                 [546, 116, 176, 20, WHITE],
                 [546, 136, 20, 116, WHITE],
                 [312, 116, 78, 20, WHITE],
                 [390, 116, 20, 136, WHITE],
                 [390, 232, 98, 20, WHITE],
                 [468, 252, 20, 96, WHITE],
                 ]
 
        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)
            
        block = Block(RED)
        block.rect.x = 140
        block.rect.y = 180
        self.block_list.add(block)
        self.movingsprites.add(block)
        block = Block(RED)
        block.rect.x = 200
        block.rect.y = 180
        self.block_list.add(block)
        self.movingsprites.add(block)
        block = Block(RED)
        block.rect.x = 260
        block.rect.y = 280
        self.block_list.add(block)
        self.movingsprites.add(block)
        block = Block(RED)
        block.rect.x = 70
        block.rect.y = 70
        self.block_list.add(block)
        self.movingsprites.add(block)
        block = Block(RED)
        block.rect.x = 150
        block.rect.y = 70
        self.block_list.add(block)
        self.movingsprites.add(block)
        block = Block(RED)
        block.rect.x = 70
        block.rect.y = 530
        self.block_list.add(block)
        self.movingsprites.add(block)
        block = Block(RED)
        block.rect.x = 140
        block.rect.y = 530
        self.block_list.add(block)
        self.movingsprites.add(block)
        block = Block(RED)
        block.rect.x = 210
        block.rect.y = 530
        self.block_list.add(block)
        self.movingsprites.add(block)
        block = Block(RED)
        block.rect.x = 720
        block.rect.y = 530
        self.block_list.add(block)
        self.movingsprites.add(block)
        block = Block(RED)
        block.rect.x = 600
        block.rect.y = 530
        self.block_list.add(block)
        self.movingsprites.add(block)
        block = Block(RED)
        block.rect.x = 480
        block.rect.y = 530
        self.block_list.add(block)
        self.movingsprites.add(block)
        block = Block(RED)
        block.rect.x = 720
        block.rect.y = 410
        self.block_list.add(block)
        self.movingsprites.add(block)
        block = Block(RED)
        block.rect.x = 600
        block.rect.y = 410
        self.block_list.add(block)
        self.movingsprites.add(block)
        block = Block(RED)
        block.rect.x = 140
        block.rect.y = 410
        self.block_list.add(block)
        self.movingsprites.add(block)
        block = Block(RED)
        block.rect.x = 330
        block.rect.y = 410
        self.block_list.add(block)
        self.movingsprites.add(block)
        block = Block(RED)
        block.rect.x = 420
        block.rect.y = 410
        self.block_list.add(block)
        self.movingsprites.add(block)
        block = Block(RED)
        block.rect.x = 700
        block.rect.y = 60
        self.block_list.add(block)
        self.movingsprites.add(block)
        block = Block(RED)
        block.rect.x = 540
        block.rect.y = 60
        self.block_list.add(block)
        self.movingsprites.add(block)
        block = Block(RED)
        block.rect.x = 370
        block.rect.y = 60
        self.block_list.add(block)
        self.movingsprites.add(block)
        block = Block(RED)
        block.rect.x = 560
        block.rect.y = 300
        self.block_list.add(block)
        self.movingsprites.add(block)

class Room4(Room):
    def __init__(self):
        super().__init__()
 
        walls = [[0, 0, 20, 250, WHITE],
                 [0, 350, 20, 250, WHITE],
                 [780, 0, 20, 350, WHITE],
                 [780, 350, 20, 250, WHITE],
                 [20, 0, 760, 20, WHITE],
                 [20, 580, 760, 20, WHITE],
                 ]
 
        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)
        
        # Create the item to allow the player to win
        win_block_list = pygame.sprite.Group()
        block = WinBlock(20, 20)
        block.rect.x = 600
        block.rect.y = 280
        self.win_block_list.add(block)
        self.movingsprites.add(block)        

# Final project for ICS4UY
# May 27, 2021
# For my final project I made this game, all game assets from opengameart.org

# We begin by importing everything we need
import pygame, sys, math, random
from Classes import *
from Rooms import *

# These are the colors
BLACK = (0, 0, 0)
# I started off with having all the walls white but decided to change the color
# Instead of changing each wall color indiviually I just changed the RGB value
WHITE = (131, 24, 161)
REAL_WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)

# Call this function so the Pygame library can initialize itself
pygame.init()

# Create an 800x675 sized screen
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode([WIDTH, HEIGHT+75])

# Set the title of the window
pygame.display.set_caption('Maze Dungeon')       

# We will use this function to drawy text easily
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

# This function will create the menu when you start up the game
def main_menu():
    
    # We set up some variables and load pics, sounds, and fonts
    running = False
    wall = pygame.image.load("stonewallback.png").convert()
    wall_pos = [0, 0]
    menu_bgm = pygame.mixer.Sound("Harp.ogg")
    menu_bgm.play(-1)
    click_sound = pygame.mixer.Sound("clicks.ogg")
    my_font = pygame.font.Font('Seagram.ttf', 60)
    my_font1 = pygame.font.Font('Seagram.ttf', 80)
    my_font2 = pygame.font.Font('Seagram.ttf', 40)
    clock = pygame.time.Clock()    
    
    # While loop for the scene
    while not running:
        
        # Set up backdrop
        screen.fill(BLACK)
        screen.blit(wall, wall_pos)

        # Use this to get mouse position
        mx, my = pygame.mouse.get_pos()

        # Create a button
        button_1 = pygame.Rect(300, 240, 200, 60)
        pygame.draw.rect(screen, WHITE, button_1)
        
        # Draw text to the screen
        draw_text('Maze Dungeon', my_font1, REAL_WHITE, screen, 125, 100)
        draw_text('Play', my_font2, REAL_WHITE, screen, 350, 240)
        draw_text('Instructions:', my_font, REAL_WHITE, screen, 220, 320)
        draw_text('Click play to start.Use arrow keys or w,a,s,d', my_font2, REAL_WHITE, screen, 10, 400)
        draw_text('to move.Left click to throw fireballs at enemies.', my_font2, REAL_WHITE, screen, 10, 450)
        draw_text('Press R at any time to return to the menu.', my_font2, REAL_WHITE, screen, 40, 500)
        draw_text('You can also press Esc to quit at any time.', my_font2, REAL_WHITE, screen, 40, 550)
        draw_text('Find the treasure to win and have fun!', my_font2, REAL_WHITE, screen, 70, 600)

        # Main event loop below
        click = False
        for event in pygame.event.get():
            # Allows us to quit
            if event.type == pygame.QUIT:
                pygame.quit()
                running = True
                sys.exit()
            # Allows us to quit when we press esc
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                    running = True
            # Click is set to true when we left click
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        # If we press button call game function and change scene          
        if button_1.collidepoint((mx, my)):
            if click:
                click_sound.play()
                menu_bgm.stop()
                game()
                running = True
       
        # Lets us see
        pygame.display.flip()
        # Set to 60 fps
        clock.tick(60)
    
    # Idle friendly quit 
    pygame.quit()

# Function for the win scene
def win_scene():
    # Set up variables, load images, sounds, and fonts
    run = False
    my_font = pygame.font.Font('Seagram.ttf', 60)
    my_font1 = pygame.font.Font('Seagram.ttf', 80)
    my_font2 = pygame.font.Font('Seagram.ttf', 40)    
    clock = pygame.time.Clock()
    back = pygame.image.load("winback.png").convert()
    back_pos = [0, 0]
    win_bgm = pygame.mixer.Sound("Lively Meadow.wav")
    win_bgm.play(-1)
    
    # Main loop
    while not run:
        # Event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = True
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                    run = True
                # Allows us to press r to return to menu
                if event.key == pygame.K_r:
                    win_bgm.stop()
                    main_menu()
                    click = True
        
        # Set background           
        screen.fill(BLACK)
        screen.blit(back, back_pos)
        # Draw text
        draw_text('Congratulations!', my_font1, REAL_WHITE, screen, 120, 100)
        draw_text('You Won!', my_font1, REAL_WHITE, screen, 210, 200)
        draw_text('Press R to return to the menu', my_font2, REAL_WHITE, screen, 140, 300)       
    
        pygame.display.flip()
        clock.tick(60)
        
    pygame.quit()            
        
# Actual game scene function
def game():
    # Create the player object
    player = Player(50, 50)
    
    # set up sprite variables
    movingsprites = pygame.sprite.Group()
    movingsprites.add(player)
    bullet_list = pygame.sprite.Group()
    walls = pygame.sprite.Group()
    wall_list = pygame.sprite.Group()
    block_list = pygame.sprite.Group()
    
    # Set some variables
    score = 0
    enemy = 0
    
    # Create font
    my_font = pygame.font.Font('Seagram.ttf', 35)
    
    # Load image
    floor = pygame.image.load("Dungeon_floor.png").convert()
    floor_pos = [0, 0]
    
    # Load sounds
    fire = pygame.mixer.Sound("fire.wav")
    slime_die = pygame.mixer.Sound("slime_step.ogg")
    bgm = pygame.mixer.Sound("TheLoomingBattle.ogg")
    # Loop bgm
    bgm.play(-1)
    
    # Create list for rooms
    rooms = []
 
    # Create rooms and append to list
    room = Room0()
    rooms.append(room)
 
    room = Room1()
    rooms.append(room)
 
    room = Room2()
    rooms.append(room)
    
    room = Room3()
    rooms.append(room)
    
    room = Room4()
    rooms.append(room)    
 
    # Set up more variables below
    current_room_no = 0
    current_room = rooms[current_room_no]
 
    clock = pygame.time.Clock()
    frame_count = 0
    frame_rate = 60
    start_time = 90
 
    win = False
    done = False
 
    # Main loop
    while not done:
 
        # Processing for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                sys.exit()
 
            # Set player speed when keys are pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    player.changespeed(-4, 0)
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    player.changespeed(4, 0)
                if event.key == pygame.K_UP or event.key == ord('w'):
                    player.changespeed(0, -4)
                if event.key == pygame.K_DOWN or event.key == ord('s'):
                    player.changespeed(0, 4)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                        done = True
                    if event.key == pygame.K_r:
                        bgm.stop()
                        main_menu()
                        click = True
                        
            # Set opposite speed when keys are released
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    player.changespeed(4, 0)
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    player.changespeed(-4, 0)
                if event.key == pygame.K_UP or event.key == ord('w'):
                    player.changespeed(0, 4)
                if event.key == pygame.K_DOWN or event.key == ord('s'):
                    player.changespeed(0, -4)
                    
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Fire a bullet if the user clicks the mouse button
                # Get the mouse position
                pos = pygame.mouse.get_pos()
                mouse_x = pos[0]
                mouse_y = pos[1]
                # Create the bullet based on where we are, and where we want to go.
                bullet = Bullet(player.rect.x, player.rect.y, mouse_x, mouse_y)
                # Add the bullet to the lists
                movingsprites.add(bullet)
                bullet_list.add(bullet)
                # Play sound when bullet is fired
                fire.play()
 
        # Lets player move
        player.move(current_room.wall_list, current_room.block_list)
        # Update sprites
        movingsprites.update()
 
        # All if statements below allow the player to change rooms
        if player.rect.x < -15:
            if current_room_no == 0:
                current_room_no = 2
                current_room = rooms[current_room_no]
                player.rect.x = 790
            elif current_room_no == 3:
                current_room_no = 1
                current_room = rooms[current_room_no]
                player.rect.x = 790
            elif current_room_no == 4:
                current_room_no = 3
                current_room = rooms[current_room_no]
                player.rect.x = 790
            elif current_room_no == 1:
                current_room_no = 0
                current_room = rooms[current_room_no]
                player.rect.x = 790            
 
        if player.rect.x > WIDTH + 1:
            if current_room_no == 0:
                current_room_no = 1
                current_room = rooms[current_room_no]
                player.rect.x = 0
            elif current_room_no == 1:
                current_room_no = 3
                current_room = rooms[current_room_no]
                player.rect.x = 0
            elif current_room_no == 3:
                current_room_no = 4
                current_room = rooms[current_room_no]
                player.rect.x = 0
            elif current_room_no == 2:
                current_room_no = 0
                current_room = rooms[current_room_no]
                player.rect.x = 0            
              
        # Lets us shoot enemies  
        for bullet in bullet_list:
            # See if it hit a block
            block_hit_list = pygame.sprite.spritecollide(bullet, current_room.block_list, True)
            # For each block hit, remove the bullet and add to the score
            for block in block_hit_list:
                bullet_list.remove(bullet)
                movingsprites.remove(bullet)
                score += 15
                enemy += 1
                slime_die.play()
            # Remove the bullet if it flies up off the screen
            if bullet.rect.y < -10:
                bullet_list.remove(bullet)
                movingsprites.remove(bullet)
         
        # Prevents bullets from going through walls   
        for bullet in bullet_list:
            # See if it hit a block
            block_hit_list = pygame.sprite.spritecollide(bullet, current_room.wall_list, False)
            # For each block hit, remove the bullet
            for block in block_hit_list:
                bullet_list.remove(bullet)
                movingsprites.remove(bullet)      
        
        # Sets win to true when player accquires the treasure   
        win_block_hit_list = pygame.sprite.spritecollide(player, current_room.win_block_list, True)
        for block in win_block_hit_list:
            win = True 
        
        # If we win, screen changes to the win scene
        if win == True:
            bgm.stop()
            win_scene()
            done = True
                
        # Set background
        screen.fill(BLACK)
        screen.blit(floor, floor_pos)
        
        # Sets up the timer
        total_seconds = frame_count // frame_rate
        minutes = total_seconds // 60
        seconds = total_seconds % 60
        output_string = "Time: {0:02}:{1:02}".format(minutes, seconds)
        time_text = my_font.render(output_string, True, REAL_WHITE)
        screen.blit(time_text, [300, 615])
        
        # Draw sprites to the screen
        current_room.block_list.draw(screen)
        movingsprites.draw(screen)
        current_room.wall_list.draw(screen)
        current_room.win_block_list.draw(screen)
        
        # Draw text
        draw_text('Score: ', my_font, REAL_WHITE, screen, 625, 615)
        draw_text('Enemies', my_font, REAL_WHITE, screen, 20, 600)
        draw_text('Deafeated: ', my_font, REAL_WHITE, screen, 20, 630)
        score_text = my_font.render(str(score), True, REAL_WHITE)
        enemy_text = my_font.render(str(enemy), True, REAL_WHITE)
        screen.blit(score_text, [720, 615])
        screen.blit(enemy_text, [180, 630])
 
        pygame.display.flip()
        
        frame_count += 1
        clock.tick(frame_rate)
 
    pygame.quit()

# Lets main menu to start up before everything else
if __name__ == "__main__":
    main_menu()
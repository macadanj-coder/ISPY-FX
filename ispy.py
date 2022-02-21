##
# Create I Spy with an FX Twist
# @author Josh Ryan Macadangdang
# @date 6/5/2018
# @course ICS3U1-4

#Import Pygame
import pygame
import random

#Initialize game engine
pygame.init()

#Define colours
BLACK = [0,0,0]
WHITE = [255,255,255]
BLUE = [0,55,255]

#Classes
#Picture Object
class Picture():
    """ Hold the fields for a picture """
    def __init__(self):
        self.image = ""
        self.x_pos = ""
        self.y_pos = ""
        self.clue = ""
        
    #Draw self(picture) on screen
    def draw(self,screen):
        screen.blit(self.image,[self.x_pos,self.y_pos])
        
    #Draw the clue of the picture on screen
    def draw_clue(self,clue):
        text_clue = font.render("I Spy with my little eye... something that " + str(self.clue),True,WHITE)
        screen.blit(text_clue,[10,670])
   

## Main ##
#Set screen and screen size
size = [1024,700]
screen = pygame.display.set_mode(size)

#Set caption
pygame.display.set_caption("I Spy FX Edition")

## MODEL ##
#Lists of attributes for each pciture object
imageList = ["basketball1.jpg","sharpie1.jpg","school_crest1.jpg","eraser1.jpg","dpcdsb1.jpg","cross1.jpg","calculator1.jpg","desk1.jpg","locker1.jpg","pen1.jpg","pencil1.jpg","textbook1.jpg","tiger1.jpg","uniform1.jpg"]
x_posList = [0,200,568,400,400,215,25,800,10,558,800,200,600,800]
y_posList = [0,50,200,500,350,110,270,500,450,400,10,400,10,250]
clueList = ["is round","is sharp","is on our sweaters","fixes mistakes","looks like a 'D'","intersects at 90 degrees","is a computer","is wooden","is narrow","is mightier than the sword","draws peoples attention","contains equations","has stripes","is worn everyday"]

#We will store each picture object here
pictureList = []

#Creates our picture objects
for i in range(len(imageList)):
    picture = Picture()
    picture.image = pygame.image.load(imageList[i]).convert()
    picture.x_pos = x_posList[i]
    picture.y_pos = y_posList[i]
    picture.clue = clueList[i]
    pictureList.append(picture)

#Pick the corret picture from a randomnly shuffled picture list
random.shuffle(pictureList)
correct_picture = pictureList[0]

#Set the height and parameters
height = correct_picture.image.get_height() #Gotten from: https://www.pygame.org/docs/ref/surface.html
width = correct_picture.image.get_width()

#We will use this to help determine the collision of the mouse and the picture
parameters = [correct_picture.x_pos + width, correct_picture.y_pos + height] 

## Main Loop until user quits ##
clock = pygame.time.Clock()

#Variables
lives = 3
correct = False
incorrect = False

main_done = False
while not main_done:
    game_over = False
    game = False
    winner = False
    menu = True
    
    ##Main Menu##
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu = False
                main_done = True
                
            #User presses on a key
            elif event.type == pygame.KEYDOWN:
                
                #If that key is "ENTER" exit the menu screen
                if event.key == pygame.K_RETURN:
                    menu = False
                    game = True
                    
        #Clear the screen and set the background 
        screen.fill(WHITE)

        #Select font
        font = pygame.font.SysFont('Calibri', 30, True, False)

        #Render the text
        mainMenuText = font.render("Welcome to i Spy! Press ENTER to start!",True,BLACK)

        #Display text on screen
        screen.blit(mainMenuText, [200, 200])

        #Update screen 
        pygame.display.flip()

        #Limit to 60 frames per second
        clock.tick(60)

    ##Game Screen##
    # Loop until done is false    
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
                main_done = True
                
            #Did the user click 
            elif event.type == pygame.MOUSEBUTTONDOWN: #Gotten from:https://stackoverflow.com/questions/10990137/pygame-mouse-clicking-detection#
                
                #Get the position of the mouse when the user clicked
                pos = pygame.mouse.get_pos()
                x = pos[0]
                y = pos[1]
                
                #Check if the user clicked on the correct object
                if ( x >= correct_picture.x_pos and x <= parameters[0] ) and (y >= correct_picture.y_pos and y <= parameters[1]):#Gotten from: https://blog.penjee.com/mouse-clicked-on-image-in-pygame/
                    correct = True
                    incorrect = False
                    
                #If the user didn't click the object take one life away
                else:
                    lives += -1
                    correct =False
                    incorrect = True
                    
            #If the user runs out of lives stop the game
            elif lives == 0:
                game = False
           
                 
        #Clear the screen and set the background
        screen.fill(BLUE)

        #All Drawing Codes Below Here
        #Draw the pictures that will be used in the game
        for i in range(len(pictureList)):
            pictureList[i].draw(screen)

        #Draw the text box onnthe bottom of the screen
        pygame.draw.rect(screen, BLACK, [0, 665, 1024, 50])

        #Draw Text   
        #Select Font
        font = pygame.font.SysFont('Calibri',25,True,False)

        #Texts
        text_lives = font.render("Current Lives:" + str(lives),True,WHITE)
        text_correct = font.render("Correct!",True,BLACK)
        text_incorrect = font.render("Incorrect",True,BLACK)

        #Display Text on screen
        #Display Lives               
        screen.blit(text_lives,[820,670])

        #Display "Correct" when user clicks correct object
        if correct is True:
            screen.blit(text_correct,[x,y])
            game = False

        #Display "Incorrect" when the user does not click on the correct object
        if incorrect is True:
            screen.blit(text_incorrect,[x,y])

        #Display Clue
        correct_picture.draw_clue(screen)

            
        #Update the screen with what we've drawn
        pygame.display.flip()

        #Limit to 60 framse per second
        clock.tick(60)

    ##Winner Screen##
    if correct is True:
        winner = True
        while winner:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    winner = False
                    main_done = True

                if event.type == pygame.KEYDOWN:
                    # If user presses enter restart the game from the beginning
                    if event.key == pygame.K_RETURN:
                        
                        #Restart all the variables necessary for the game        
                        winner = False
                        game = True
                        correct = False
                        lives = 3
                        
                        #Randomnly shuffle the picture list again so we get a new correct picture
                        random.shuffle(pictureList)
                        correct_picture = pictureList[0]
                        
                        #Set the height and parameters of the new correct picture
                        height = correct_picture.image.get_height() #Gotten from: https://www.pygame.org/docs/ref/surface.html
                        width = correct_picture.image.get_width()

                        #We will use this to help determine the collision of the mouse and the picture
                        parameters = [correct_picture.x_pos + width, correct_picture.y_pos + height] 

                #Fill the screen and set the background        
                screen.fill(WHITE)

                #Select the font
                font = pygame.font.SysFont('Calibri', 30, True, False)

                #Render the text
                winner_text = font.render("Winner: Press ENTER to restart",True,BLACK)

                #Display text on screen
                screen.blit(winner_text, [200, 200])

                #Update the text on screen
                pygame.display.flip()

                #Limit to 60 frames per second
                clock.tick(60)
                
    ##Game Over Screen##
    #When the player runs out of lives display game over screen
    else:
        game_over = True
        while game_over:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    game_over = False
                    main_done = True
                    
                #If user presses a key
                if event.type == pygame.KEYDOWN:

                    #If that key is "ENTER" end the main loop
                    if event.key == pygame.K_ESCAPE:
                        game_over = False
                        main_done = True

                #Clear the screen and set the background
                screen.fill(BLACK)

                #Select font
                font = pygame.font.SysFont('Calibri', 30, True, False)

                #Render text
                gameOverText = font.render("GAME OVER!:Press ESC to exit",True,WHITE)

                #Display text on screen
                screen.blit(gameOverText, [200, 200])

                #Update the screen
                pygame.display.flip()

                #Limit to 60 frames
                clock.tick(60)

#Be IDLE Friendly        
pygame.quit()

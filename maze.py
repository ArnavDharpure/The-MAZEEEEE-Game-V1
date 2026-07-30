import pygame

#init-initiate, like a new phone no mean play games, first need to update and logina dn stuff
pygame.init()

font = pygame.font.SysFont(None, 72)


WHITE=(255,255,255)
BLACK=(0,0,0)
RED = (255,0,0)
GRAY = (170,170,170) 
BLUE = (0, 120, 255)

winner = None
game_state = "MENU"

#MAZEEEEEE
CELL_SIZE = 40

maze=[
[1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1],
[1,0,1,0,1,1,1,1,1,1,1,0,1,0,1,1,1,0,1,0,1],
[1,0,1,0,0,0,1,0,0,0,0,0,1,0,0,0,1,0,1,0,1],
[1,0,1,1,1,0,1,0,1,1,1,1,1,1,1,0,1,0,1,1,1],
[1,0,1,0,0,0,1,0,1,0,1,0,0,0,0,0,1,0,0,0,1],
[1,0,1,0,1,1,1,0,1,0,1,0,1,1,1,1,1,1,1,0,1],
[1,0,0,0,1,0,1,0,1,0,1,0,0,0,1,0,0,0,0,0,1],
[1,1,1,1,1,0,1,0,1,0,1,0,1,1,1,0,1,1,1,1,1],
[1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1],
[1,0,1,0,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,0,1],
[1,0,1,0,1,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,1],
[1,0,1,1,1,0,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1],
[1,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0,1,0,0,0,1],
[1,0,1,0,1,1,1,1,1,1,1,0,1,1,1,1,1,0,1,0,1],
[1,0,1,0,1,0,0,0,0,0,1,0,0,0,1,0,0,0,1,0,1],
[1,0,1,0,1,0,1,1,1,0,1,1,1,1,1,0,1,1,1,0,1],
[1,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0,1,0,1,0,1],
[1,0,1,1,1,1,1,0,1,1,1,0,1,1,1,1,1,0,1,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1],
]


WIDTH=840
HEIGHT=840
screen = pygame.display.set_mode((WIDTH, HEIGHT))

#Setting the display title
pygame.display.set_caption("The MAZEEEEE Game")

#Screen opens and closes, Need a loop to update display
'''While using a loop we prefer =false than break inside a fxn because break means the cursor just exits the loop but =false means the loop has ended but the entire code inside the fxn will be executed even the one inside and below false'''
running=True
player_row = 20
player_col = 19
player_size = 24

ai_row = 0
ai_col = 1

frame_count = 0
ai_delay = 70


# UHOHHHHH THE AI CODEEEEE
ai_path = [
(0,1),(1,1),(2,1),(3,1),(4,1),(5,1),(6,1),(7,1),
(7,2),(7,3),(6,3),(5,3),(5,4),(5,5),(4,5),(3,5),
(3,4),(3,3),(2,3),(1,3),(1,4),(1,5),(1,6),(1,7),
(1,8),(1,9),(1,10),(1,11),(2,11),(3,11),(3,10),
(3,9),(3,8),(3,7),(4,7),(5,7),(6,7),(7,7),(8,7),
(9,7),(9,6),(9,5),(10,5),(11,5),(12,5),(13,5),
(13,4),(13,3),(14,3),(15,3),(16,3),(17,3),(17,4),
(17,5),(16,5),(15,5),(15,6),(15,7),(15,8),(15,9),
(16,9),(17,9),(17,8),(17,7),(18,7),(19,7),(19,8),
(19,9),(19,10),(19,11),(18,11),(17,11),(17,12),
(17,13),(17,14),(17,15),(16,15),(15,15),(15,16),
(15,17),(14,17),(13,17),(13,18),(13,19),(14,19),
(15,19),(16,19),(17,19),(18,19),(19,19),(20,19)
]

ai_step = 0

while running:
    frame_count += 1


#No event=pygame.event.get because usme ek baar value assign ho gayi to ho gayi phir kitni bhi keys daba kuch nai hoga. Agar karna hai to inside list bana but just using pygae.smth is better
 #check events
    for current_event in pygame.event.get():

        if current_event.type == pygame.QUIT:
            running=False

        #Checking If any key was pressed
        elif current_event.type == pygame.KEYDOWN:
             
             if game_state == "MENU":
                  if current_event.key == pygame.K_RETURN:
                       game_state = "PLAYING"

                  elif current_event.key == pygame.K_ESCAPE:
                       running = False

             elif game_state == "PLAYING":
                      if current_event.key == pygame.K_ESCAPE:
                              game_state = "PAUSED"
                      elif current_event.key == pygame.K_UP:
                                          if player_row > 0 and maze[player_row - 1][player_col] == 0:
                                                  player_row -= 1
          
                      elif current_event.key == pygame.K_DOWN:
                                          if player_row < len(maze)-1 and maze[player_row + 1][player_col] == 0:
                                              player_row += 1
          
                      elif current_event.key == pygame.K_LEFT:
                              if player_col > 0 and maze[player_row][player_col - 1] == 0:
                                  player_col -= 1
                      elif current_event.key == pygame.K_RIGHT:
                              if player_col < len(maze[0])-1 and maze[player_row][player_col + 1] == 0:
                                  player_col += 1
             elif game_state=="PAUSED":
                   if current_event.key == pygame.K_r:
                         #reset position
                         player_row = 20
                         player_col = 19

                         ai_row=0
                         ai_col=1
                         ai_step=0

                         winner=None

                         game_state="PLAYING"
                   elif current_event.key ==pygame.K_ESCAPE:
                         running = False
    #Draw character and update screen
    screen.fill(WHITE)

    #MENU
    if game_state == "MENU":
       title = font.render("THE MAZEEEEE GAME", True, BLACK)   #Image created
       start = font.render("Press ENTER to Start", True, BLACK)
       exit_text = font.render("Press ESC to Exit", True, BLACK)

       screen.blit(title, (160, 200))   #Image pasted
       screen.blit(start, (180, 330))
       screen.blit(exit_text, (180, 420))
       pygame.display.update()
       continue

    #Menu in game
    if game_state == "PAUSED":
        if winner=="PLAYER":
            title = font.render("YOU WIN!", True, BLACK)
        elif winner=="AI":
              title = font.render("COMPUTER WINS!", True, BLACK)
        else:
              title = font.render("GAME PAUSED!", True, BLACK)
        
        restart = font.render("Press R to Restart", True, BLACK)
        exit_text = font.render("Press ESC to Exit", True, BLACK)

        screen.blit(title, (220, 220))
        screen.blit(restart, (210, 330))
        screen.blit(exit_text, (210, 420))

        pygame.display.update()
        continue

    #AI MOVEMENT
    if game_state == "PLAYING":
        if frame_count % ai_delay == 0:
              if ai_step < len(ai_path) - 1:
                 ai_step += 1
                 ai_row, ai_col = ai_path[ai_step]


    #WIN/LOSE SYSTEMMMMMMMMMMM
    if player_row == 0 and player_col == 1:
       winner="PLAYER"

    if ai_row == 20 and ai_col == 19:
        winner="AI"

    #THE MAZEEEEEEEEEEEEEEEEEEEEEEEE ITSELF!!!!!!!
    for row in range(len(maze)):
        for col in range(len(maze[row])):
                if maze[row][col] == 1:
                    pygame.draw.rect(
                        screen,
                        GRAY,
                        (
                            col * CELL_SIZE,
                            row * CELL_SIZE,
                            CELL_SIZE,
                            CELL_SIZE
                        )
                    )
    #Player
    pygame.draw.rect(
    screen,
    RED,
    (
        player_col * CELL_SIZE + 8,
        player_row * CELL_SIZE + 8,
        player_size,
        player_size
    )
    )

    #Ai
    pygame.draw.rect(
    screen,
    BLUE,
    (
          ai_col * CELL_SIZE + 8,
          ai_row * CELL_SIZE + 8,
          player_size,
          player_size
     )
    )
    if winner == "PLAYER":
       winner="PLAYER"
       game_state="PAUSED"
    elif winner == "AI":
       winner="AI"
       game_state="PAUSED"
    pygame.display.update()
pygame.quit()
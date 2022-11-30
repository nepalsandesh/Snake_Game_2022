import pygame
import grid




width = 1920
height = 1000
resolution = (width, height)


pygame.init()
screen = pygame.display.set_mode(resolution)
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()
FPS = 10

# colors
black = (0, 0, 0)
white = (255, 255, 255)
dark_blue = (15, 15, 55)

scale = 30
offset = 1

Grid = grid.Grid(width, height, scale, offset)
Grid.make_grid()
key = None


while True:
    clock.tick(FPS)
    screen.fill(black)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()
                
            if event.key == pygame.K_UP:
                key = "up"
            if event.key == pygame.K_DOWN:
                key = "down"
            if event.key == pygame.K_LEFT:
                key = "left"
            if event.key == pygame.K_RIGHT:
                key = "right"

    Grid.snake(key)
    Grid.draw(screen, black, white)
  
                
    
    pygame.display.flip()
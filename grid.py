import numpy
import pygame
import random



class Grid:
    """Grid Class"""
    def __init__(self, width, height, scale, offset):
        
        self.width = width
        self.height = height
        self.scale = scale
        self.offset = offset
        
        self.rows = int(height//scale)
        self.columns = int(width//scale)
        
        self.grid_array = numpy.ndarray(shape=(self.rows, self.columns))
        self.snake_array = [(5,6), (5,7), (5,8), (5,9),(5,10),(5,11),(5,12),(5,13),(5,14),(5,15),(5,16),(5,17),(5,18),(5,19)]
        
        
        
    def make_grid(self):
        for x in range(self.rows):
            for y in range(self.columns):
                self.grid_array[x][y] = 0
                
                
    # grid_array drawing function
    def draw(self, screen, on_color, off_color):
        for y in range(self.rows):
            for x in range(self.columns):
                x_pos = x * self.scale
                y_pos = y * self.scale 
                rect = pygame.Rect(x_pos, y_pos, self.scale-self.offset, self.scale-self.offset)
                
                if self.grid_array[y][x] == 0:
                    pygame.draw.rect(screen, off_color, rect)
                elif self.grid_array[y][x] == 1:
                    pygame.draw.rect(screen, on_color, rect)
                    
    

        
    def snake(self, arrow):
        self.make_grid()
        snake_head = self.snake_array[-1]
        head_row, head_col = snake_head
                 
        if head_row >= self.rows:
            head_row = 0
        
        if head_row <= 0:
            print("hi")
            head_row = self.rows
            
        
        print("doing")
        
        if arrow == "right":
            self.snake_array.append([head_row, head_col+1])  
            self.snake_array.pop(0)

        if arrow == "down":
            self.snake_array.append([head_row+1, head_col])
            self.snake_array.pop(0)

        if arrow == "left":
            self.snake_array.append([head_row, head_col-1])
            self.snake_array.pop(0)
            
        if arrow == "up":
            self.snake_array.append([head_row-1, head_col])
            self.snake_array.pop(0)
            

        
        for point in self.snake_array:
            if point[0] > 32:
                point[0] = 0
            
            
            self.grid_array[point[0]][point[1]] = 1
            

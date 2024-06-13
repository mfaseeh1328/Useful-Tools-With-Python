import pygame, sys, random, math, time
pygame.init()

class MovingGradients():
    def __init__(self, win, color1, color2, color3):
        self.window = win
        self.width, self.height = self.window.get_size()[0], self.window.get_size()[1]
        self.gradient_index = 0
        self.color1, self.color2, self.color3 = color1, color2, color3
        self.change1, self.change2, self.change3 = False, False, False
        self.y = 0

    def draw_surface(self):
        surface = pygame.Surface((self.width, self.height))
        surface.fill((self.color1, self.color2, self.color3))
    
        self.window.blit(surface, (0, 0))
    def update_color_one(self):
        
        if self.change1 is not True:
            self.color1 += 1
            
        if self.color1 >= 255:
            self.color1 = 255

            if self.color1 <= 255:
                self.change1 = True
            
        if self.change1 == True:
            self.color1 -= 1

        if self.color1 <= 100:
            self.color1 = 100
            self.change1 = False

    def update_color_two(self):
        
        if self.change2 is not True:
            self.color2 += 1
            
        if self.color2 >= 255:
            self.color2 = 255

            if self.color2 <= 255:
                self.change2 = True
            
        if self.change2 == True:
            self.color2 -= 1

        if self.color2 <= 100:
            self.color2 = 100
            self.change2 = False

    def update_color_three(self):
        
        if self.change3 is not True:
            self.color3 += 1
            
        if self.color3 >= 255:
            self.color3 = 255

            if self.color3 <= 255:
                self.change3 = True
            
        if self.change3 == True:
            self.color3 -= 1

        if self.color3 <= 100:
            self.color3 = 100
            self.change3 = False

    def create_gradient(self, start_color, end_color):
        surface = pygame.Surface((self.width, self.height))
        surface.fill(start_color)
        dy = (end_color[1] - start_color[1]) / self.height
        self.y = 0

        for i in range(self.height):
            color = (start_color[0], start_color[1] + int(self.y), start_color[2])
            pygame.draw.line(self.window, (color), (0, i), (self.width, i))
            self.y += dy 

WIDTH, HEIGHT = 1000, 900
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
CLOCK = pygame.time.Clock()
color_one, color_two = (150, 90, 180), (100, 250, 25)

def exit_game(run):
    if run:
        run = False
        sys.exit()    

    pygame.quit()
def update_display():
    pygame.display.update()

def main():

    moving_gradients = MovingGradients(WIN, random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    DT = 0
    run = True
    while run:

        WIN.fill(('white'))
        #moving_gradients.draw_surface()

        #moving_gradients.update_color_one()
        #moving_gradients.update_color_two()
        #moving_gradients.update_color_three()

        #moving_gradients.create_gradient(color_one, color_two)
        update_display()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game(run)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit_game(run)
        DT = CLOCK.tick(60) / 1000

if __name__ == '__main__':
    main()
            
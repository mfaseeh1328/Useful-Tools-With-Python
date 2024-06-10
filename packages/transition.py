import pygame, sys, random, math, time
pygame.init()

class Transition():
    def __init__(self, surface):
        self.window = surface
        self.size = self.window.get_size()

        # slide transition
        self.rect = pygame.Rect(0, 0, self.size[0], self.size[1])
        self.vel_bool, self.vel = 0, 0
        self.stop_slide_transition = False

        # circular transition
        self.radius = 50
        self.stop_circular_transition = False
        self.timer = 0

        # fade transition
        self.fade_blocks = []
        self.alpha_value = []
        self.block_size = 20
        self.stop_fade_transition = False
        self.block_vel = 0

        for i in range(self.size[0] // self.block_size):
            x = i * self.block_size
            for j in range(self.size[0] // self.block_size - 10):
                y = j * self.block_size
                self.fade_blocks.append([x, y])
            
        for i in range(self.size[0] // self.block_size):
            alpha_speed = random.randint(0, 10)
            self.alpha_value.append(alpha_speed)

    def slide_transition(self, x, y, vel, color):
        if self.stop_slide_transition is not True:
            self.rect, self.vel_bool = pygame.Rect(x, y, self.size[0], self.size[1]), vel
            if self.vel_bool == 1:
                self.vel += 30

                self.rect.x += (self.vel_bool + self.vel)
            if self.rect.x >= self.size[0]:
                self.rect.x = -self.size[0]
                self.vel_bool, self.vel = 0, 0
                self.stop_slide_transition = True

        pygame.draw.rect(self.window, (color), self.rect)
        return self.stop_slide_transition
    
    def circular_transition(self, color, speed, left_over):

        if self.stop_circular_transition is not True:
            if self.radius <= self.size[0] - 100:
                self.radius += speed
        try:
            if self.radius >= self.size[0] - 100:
                self.stop_circular_transition = True
            if self.stop_circular_transition is True:
                self.timer += 1
            if self.timer >= 200:
                self.radius = 0
                self.timer = 0
        except Exception as error:
            print(error)

        pygame.draw.circle(self.window, (color), (self.size[0] // 2, self.size[1] // 2), int(self.radius), int(self.radius - left_over))
        return self.stop_circular_transition

    def fadeIn_block_transition(self, color):
        surface = pygame.Surface((self.block_size, self.block_size))
        surface.fill(color)
        current_alpha = [0 for i in range(50)]
        timer = 0

        self.block_vel += 1
        if self.block_vel >= 240:
            self.block_vel = 240

        for current, speed in zip(current_alpha, self.alpha_value):
            if self.stop_fade_transition is not True:
                current += speed + self.block_vel

                if current >= 240:
                    timer += 1

                    if timer >= 50:
                        timer = 0
                        self.stop_fade_transition = True

            else:
                if self.stop_fade_transition == True:
                    current = 0
            surface.set_alpha(current)

        for blocks in self.fade_blocks:
            self.window.blit(surface, (blocks[0], blocks[1]))
        return self.stop_fade_transition

WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT), pygame.SCALED | pygame.NOFRAME)
CLOCK = pygame.time.Clock()

def quit_game(run):
    if run:
        run = False
        sys.exit()

def main():
    run = True
    transition = Transition(WIN)
    DT = 0                          # delta time for frame-rate independence

    while run:

        WIN.fill(('gold'))

        #transition.slide_transition(-WIDTH, 0, 1, "black")
        #transition.circular_transition('black', 10, 0)
        transition.fadeIn_block_transition('black')

        pygame.display.update()

        DT = CLOCK.tick(60) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               quit_game(run)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    quit_game(run)
    pygame.quit()

if __name__ == '__main__':
    main()
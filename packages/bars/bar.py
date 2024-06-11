import pygame, sys, math, time, random
pygame.init()

class ProgressBars():
    def __init__(self, win, width, image, load_bar_width):
        # health bar
        self.window = win
        self.width, self.height = width, width // 10
        self.image = image
        self.img_width, self.img_height = self.image[0].get_width(), self.image[0].get_height()
        self.player = [pygame.image.load(f"packages/bars/player/{i}.png").convert_alpha() for i in range(1, 5)]
        self.player_index = 0
        self.bar_index = 0
        self.border_width, self.border_height = self.img_width, self.img_height
        # loading bar
        self.load_bar_width = load_bar_width
        self.load_border_width = self.window.get_size()[0] - 100

    def health_bar(self, x, y, dt):

        def animate():
            try:
                self.bar_index += 70 * dt
                if self.bar_index >= 410:
                    self.bar_index = 0
            except Exception as error:
                print(error)
        animate()

        pygame.draw.rect(self.window, ('white'), (x - 8, math.sin(time.time()) * 20 + y - 3, self.border_width + 15, self.border_height + 5), 2)
        self.window.blit(pygame.transform.scale(self.image[round(int(self.bar_index // 10))], (self.img_width, self.img_height)), (x, math.sin(time.time()) * 20 + y))
        
    def animate_player(self, x, y, dt):
        self.player_index += 100 * dt
        if self.player_index >= 120:
            self.player_index = 0

        self.window.blit(pygame.transform.scale2x(self.player[round(int(self.player_index // 30), 2)]), (x, y))

    def loading_bar(self, border_color, bar_color, x, y):

        if self.load_bar_width <= self.load_border_width - 6:
            self.load_bar_width += random.randint(-1, 4)

        pygame.draw.rect(self.window, (border_color), (x - 3, y - 3, self.load_border_width, 16), 2)
        pygame.draw.rect(self.window, (bar_color), (x, y, self.load_bar_width, 10))

WIDTH, HEIGHT, FPS = 600, 600, 60
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
CLOCK = pygame.time.Clock()
DT = 0
BAR = [pygame.image.load(f"packages/bars/progressBar/{i}.png").convert_alpha() for i in range(1, 42)]

def exit_game(run):
    if run:
        run = False
        sys.exit()
    pygame.quit()

def update_display():
    pygame.display.update()

def main():
    global DT

    progressbar = ProgressBars(WIN, 150, BAR, 0)

    run = True
    while run:
        WIN.fill(('black'))

        DT = CLOCK.tick(60) / 1000

        #progressbar.health_bar(WIDTH // 2 - 100, HEIGHT // 2, DT)
        progressbar.loading_bar('red', 'red', 50, HEIGHT // 2)
        #progressbar.animate_player(WIDTH // 2 - 50, HEIGHT // 2 + 40, DT)

        update_display()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game(run)

if __name__ == '__main__':
    main()

        
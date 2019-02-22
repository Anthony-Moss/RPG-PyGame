import pygame
from random import randint

KEY_UP = 273
KEY_DOWN = 274
KEY_LEFT = 276
KEY_RIGHT = 275

# creating a Player class to represent the users character
class Player():
    def __init__(self, x, y, x_dir, y_dir, avatar):
        self.x = x
        self.y = y
        self.x_dir = x_dir
        self.y_dir = y_dir
        self.avatar = avatar
    
    def update(self, width, height):
        self.x += self.x_dir
        self.y += self.y_dir
        if self.x + 64 > width:
            self.x_dir = 0
        if self.x - 32 < 0:
            self.x_dir = 0
        if self.y + 64 > height:
            self.y_dir = 0
        if self.y - 32 < 0:
            self.y_dir = 0

    def render(self, screen):
        screen.blit(self.avatar, (self.x, self.y))



def main():
    width = 960
    height = 960

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('My Game')
    clock = pygame.time.Clock()
    sir_david_quinith = Player(464, 896, 0, 0, pygame.image.load('images/quinith_wings.png'))

    # Game initialization
    background_img = pygame.image.load('images/rpg_background_tilemap.png').convert_alpha()
    stop_game = False
    while not stop_game:
        for event in pygame.event.get():

            # Event handling
            if event.type == pygame.KEYDOWN:
                if event.key == KEY_UP:
                    sir_david_quinith.y_dir = -3
                elif event.key == KEY_DOWN:
                    sir_david_quinith.y_dir = 3
                elif event.key == KEY_LEFT:
                    sir_david_quinith.x_dir = -3
                elif event.key == KEY_RIGHT:
                    sir_david_quinith.x_dir = 3
                elif event.key == pygame.K_RETURN:
                    main()
                # deactivate the cooresponding speeds
                # when an arrow key is released
            if event.type == pygame.KEYUP:
                if event.key == KEY_UP:
                    sir_david_quinith.y_dir = 0
                elif event.key == KEY_DOWN:
                    sir_david_quinith.y_dir = 0
                elif event.key == KEY_LEFT:
                    sir_david_quinith.x_dir = 0
                elif event.key == KEY_RIGHT:
                    sir_david_quinith.x_dir = 0
            if event.type == pygame.QUIT:
                stop_game = True


        # Game logic
        
        # Draw background
        screen.blit(background_img, (0,0))

        # Game display
        
        sir_david_quinith.render(screen)
        sir_david_quinith.update(width,height)
        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
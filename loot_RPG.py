import pygame

# creating a Player class to represent the users character
class Player():
    def __init__(self, x_pos, y_pos, x_pos_dir, y_pos_dir)
def main():
    width = 640
    height = 640
    blue_color = (97, 159, 182)

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('My Game')
    clock = pygame.time.Clock()

    # Game initialization
    background_img = pygame.image.load('images/tile_background3.png').convert_alpha()
    stop_game = False
    while not stop_game:
        for event in pygame.event.get():

            # Event handling

            if event.type == pygame.QUIT:
                stop_game = True


        # Game logic
        
        # Draw background
        screen.fill(blue_color)

        # Game display
        screen.blit(background_img, (0,0))

        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
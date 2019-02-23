import pygame
import time
from random import randint

KEY_UP = 273
KEY_DOWN = 274
KEY_LEFT = 276
KEY_RIGHT = 275

# # creating a Block class to hold games sprites
# class newSprite(pygame.sprite.Sprite):
#     def __init__(self, x, y, file_name):
#         pygame.sprite.Sprite.__init__(self)
#         # self.images = []
#         # self.images.append(pygame.image.load(file_name))
#         self.image = file_name
#         self.x = x
#         self.y = y
#         self.rect = self.image.get_rect()
#         self.rect.topleft=(0,0)
#         self.mask = pygame.mask.from_surface(self.image)

#     def update(self, rect_x, rect_y):
#         self.rect.x = rect_x
#         self.rect.y = rect_y




class Player(pygame.sprite.Sprite):
    def __init__(self, x_dir, y_dir, name, avatar, width, height):
        super().__init__()
        # self.x = x
        # self.y = y
        self.x_dir = x_dir
        self.y_dir = y_dir
        self.name = name
        self.image = avatar
        self.avatar = avatar.convert_alpha()
        self.rect = self.avatar.get_rect()
    
    def update(self, width, height):
        self.rect.x += self.x_dir
        self.rect.y += self.y_dir
        if self.rect.x + 64 > width:
            self.x_dir = 0
        if self.rect.x - 32 < 0:
            self.x_dir = 0
        if self.rect.y + 64 > height:
            self.y_dir = 0
        if self.rect.y - 32 < 0:
            self.y_dir = 0

    def render(self, screen):
        screen.blit(self.avatar, (self.rect.x, self.rect.y))
    
class Monster(pygame.sprite.Sprite):
    def __init__(self, width, height, name, avatar):
        super().__init__()
        # self.x = x
        # self.y = y
        self.avatar = avatar
        self.name = name
        self.image = avatar

        self.rect = self.avatar.get_rect()

class Combat(pygame.sprite.Sprite):
    def __init__(self, width, height, name, avatar, health, attack):
        super().__init__()
        self.combat_width = width
        self.combat_height = height
        self.name = name
        self.avatar = avatar
        self.image = avatar
        self.health = health
        self.attack = attack
        self.rect = self.avatar.get_rect()


def main():
    width = 960
    height = 960
    blue =  (97, 159, 182)

    eto_start_x = randint(74, 896)
    eto_start_y = randint(74,896)
    omori_start_x = randint(74, 896)
    omori_start_y = randint(74, 896)

    pygame.init()

    screen = pygame.display.set_mode((width, height))
    combat_screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('My Game')
    clock = pygame.time.Clock()

    block_list = pygame.sprite.Group()
    all_sprites_list = pygame.sprite.Group()
    combat_sprites_list = pygame.sprite.Group()

    sir_david_quinith = Player(0, 0, "Sir David Quinith", pygame.image.load('images/quinith_wings.png').convert_alpha(), width, height)
    sir_david_quinith.rect.x = 464
    sir_david_quinith.rect.y = 896
    all_sprites_list.add(sir_david_quinith)

    sir_david_quinith_combat = Combat(width, height,  "Sir David Quinith", pygame.image.load('images/quinith_wings.png').convert_alpha(), 100, 15)
    sir_david_quinith_combat.rect.x = 230
    sir_david_quinith_combat.rect.y = 420

    enemy_combat = Combat(width, height, "name", pygame.image.load('images/jason.png').convert_alpha(), 90, 10)

    combat_sprites_list.add(sir_david_quinith_combat, enemy_combat)    
    

    Eto = Monster(width, height, "Eto", pygame.image.load('images/demonspawn_red_m.png').convert_alpha())
    Eto.rect.x = eto_start_x
    Eto.rect.y = eto_start_y

    block_list.add(Eto)
    all_sprites_list.add(Eto)

    Yakumo_Omori = Monster(omori_start_x, omori_start_y, "JASON", pygame.image.load('images/jason.png').convert_alpha())
    Yakumo_Omori.rect.x = omori_start_x
    Yakumo_Omori.rect.y = omori_start_y
    
    block_list.add(Yakumo_Omori)
    all_sprites_list.add(Yakumo_Omori)
        
    # Game initialization
    background_img = pygame.image.load('images/rpg_background_tilemap.png').convert_alpha()
    combat_background = pygame.image.load('images/background.png').convert_alpha()
    stop_game = False
    in_combat = False
    while not stop_game:
        for event in pygame.event.get():
            if in_combat == False:

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
                    
                    # elif event.key == pygame.K_RETURN:
                    #     main()

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

            if in_combat == True:
                user_health = sir_david_quinith_combat.health
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        enemy_combat.health -= sir_david_quinith_combat.attack
                        user_health -= enemy_combat.attack + randint(1,5)
                    elif event.key == pygame.K_2:
                        enemy_combat.health -= (sir_david_quinith_combat.attack) + 5
                        user_health -= enemy_combat.attack + randint(1,5)
                    elif event.key == pygame.K_3:
                        enemy_combat.health -= (sir_david_quinith_combat.attack) * 2
                        user_health -= enemy_combat.attack + randint(1,5)
                    elif event.key == pygame.K_q:
                        main()



            if event.type == pygame.QUIT:
                stop_game = True
            
            # while in_combat == True:
            #     font = pygame.font.Font(None, 25)
            #     block = font.render("you killed %s!" % (block.name), True, (blue))
            #     rect = block.get_rect()
            #     rect.center = screen.get_rect().center
            #     screen.blit(block, rect)
            #     pygame.display.update()





        # while in_combat == True:


        # Game logic
        player_hit_list = pygame.sprite.spritecollide(sir_david_quinith, block_list, True)
        for block in player_hit_list:
            # pygame.time.wait(3000)
            # Render text
                font = pygame.font.Font(None, 25)
                block = font.render("you killed %s!" % (block.name), True, (blue))
                rect = block.get_rect()
                rect.center = screen.get_rect().center
                screen.blit(block, rect)
                pygame.display.update()
                in_combat = True
            

        block_list.update(width, height)
        # Draw background
        #If the player is not in combat show normal screen and characters
        if in_combat == False:
            screen.blit(background_img, (0,0))
            block_list.draw(screen)
            sir_david_quinith.render(screen)
            sir_david_quinith.update(width,height)
            # if player is is in combat it loads the combat screen
        elif in_combat == True:
            screen.fill(blue)
            combat_screen.blit(combat_background, (224,240))
            combat_sprites_list.draw(combat_background)

            font = pygame.font.Font(None, 25)
            block = font.render("Press 1 for normal attack", True, (blue))
            rect = block.get_rect()
            rect.center = combat_screen.get_rect().center
            screen.blit(block, rect)

            # pygame.display.update()
            # font2 = pygame.font.Font(None, 25)
            block2 = font.render("Press 2 for heavy attack", True, (blue))
            rect2= block2.get_rect().move(380,360)
            combat_screen.blit(block2, rect2)
            pygame.display.update()


        # Game display


        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()

import pygame
import time
from random import randint

KEY_UP = 273
KEY_DOWN = 274
KEY_LEFT = 276
KEY_RIGHT = 275


class Player(pygame.sprite.Sprite):
    def __init__(self, x_dir, y_dir, name, avatar, width, height, attack, health):
        super().__init__()
        # self.x = x
        # self.y = y
        self.x_dir = x_dir
        self.y_dir = y_dir
        self.name = name
        self.image = avatar
        self.avatar = avatar.convert_alpha()
        self.attack = attack
        self.health = health
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
    def __init__(self, width, height, name, avatar, attack, health):
        super().__init__()
        # self.x = x
        # self.y = y
        self.avatar = avatar
        self.name = name
        self.image = avatar.convert_alpha()
        self.attack = attack
        self.health = health
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
    black = (255, 255, 255)
    red = (62, 6, 6)
    green = (29, 167, 27)
    bright_pink = (204, 46, 110)

    # enemy_starts_x = []
    # enemy_starts_y = []

    # omori_start_x = randint(74, 896)
    # omori_start_y = randint(74,896)

    eto_start_x = randint(74, 896)
    eto_start_y = randint(74, 896)

    extra_monster_1_x = randint(74, 896)
    extra_monster_1_y = randint(74,896)

    extra_monster_2_x = randint(74, 896)
    extra_monster_2_y = randint(74, 896)

    extra_monster_3_x = randint(74, 896)
    extra_monster_3_y = randint(74, 896)

    extra_monster_4_x = randint(74, 896)
    extra_monster_4_y = randint(74, 896)

    extra_monster_5_x = randint(74, 896)
    extra_monster_5_y = randint(74, 896)

    

    pygame.init()

    screen = pygame.display.set_mode((width, height))
    combat_screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('My Game')
    clock = pygame.time.Clock()

    block_list = pygame.sprite.Group()
    all_sprites_list = pygame.sprite.Group()
    combat_sprites_list = pygame.sprite.Group()
    fighting_sprite_list = pygame.sprite.Group()

    sir_david_quinith = Player(0, 0, "Sir David Quinith", pygame.image.load('images/quinith_wings.png').convert_alpha(), width, height, 0, 200)
    sir_david_quinith.rect.x = 464
    sir_david_quinith.rect.y = 896
    heavy_attack_count = 0
    spell_attack_count = 0
    extra_attack = 10
    

    sir_david_quinith_combat = Combat(width, height,  "Sir David Quinith", pygame.image.load('images/quinith_wings.png').convert_alpha(), 100, 15)
    sir_david_quinith_combat.rect.x = 224
    sir_david_quinith_combat.rect.y = 370

    enemy_combat = Combat(width, height, "name", pygame.image.load('images/jason.png').convert_alpha(), 90, 10)
    enemy_combat.rect.x = 224
    enemy_combat.rect.y = 64
    combat_sprites_list.add(sir_david_quinith_combat, enemy_combat)    
    

    Eto = Monster(width, height, "Eto", pygame.image.load('images/ghoul.png').convert_alpha(), 10, 90)
    Eto.rect.x = eto_start_x
    Eto.rect.y = eto_start_y


    Yakumo_Omori = Monster(width, height, "JASON", pygame.image.load('images/jason.png').convert_alpha(), 0, 400)
    Yakumo_Omori.rect.x = 464
    Yakumo_Omori.rect.y = 64

    extra_monster_1 = Monster(extra_monster_1_x, extra_monster_1_y, "Monster 1", pygame.image.load('images/ghoul.png').convert_alpha(), 0, 500)
    extra_monster_1.rect.x = extra_monster_1_x
    extra_monster_1.rect.y = extra_monster_1_y

    extra_monster_2 = Monster(extra_monster_2_x, extra_monster_2_y, "Monster 2", pygame.image.load('images/ghoul.png').convert_alpha(), 0, 0)
    extra_monster_2.rect.x = extra_monster_2_x
    extra_monster_2.rect.y = extra_monster_2_y

    extra_monster_3 = Monster(extra_monster_3_x, extra_monster_3_y, "Monster 3", pygame.image.load('images/ghoul.png').convert_alpha(), 0, 500)
    extra_monster_3.rect.x = extra_monster_3_x
    extra_monster_3.rect.y = extra_monster_3_y

    extra_monster_4 = Monster(extra_monster_4_x, extra_monster_4_y, "Monster 4", pygame.image.load('images/ghoul.png').convert_alpha(), 0, 500)
    extra_monster_4.rect.x = extra_monster_4_x
    extra_monster_4.rect.y = extra_monster_4_y

    extra_monster_5 = Monster(extra_monster_5_x, extra_monster_5_y, "Monster 5", pygame.image.load('images/ghoul.png').convert_alpha(), 0, 500)
    extra_monster_5.rect.x = extra_monster_5_x
    extra_monster_5.rect.y = extra_monster_5_y
    
    block_list.add(Yakumo_Omori, Eto, extra_monster_1, extra_monster_2, extra_monster_3, extra_monster_4, extra_monster_5)
    all_sprites_list.add(sir_david_quinith, Yakumo_Omori, Eto,extra_monster_1, extra_monster_2, extra_monster_3, extra_monster_4, extra_monster_5)
        
    # Game initialization
    background_img = pygame.image.load('images/rpg_background_tilemap.png').convert_alpha()
    combat_background = pygame.image.load('images/combat_background.png').convert_alpha()
    stop_game = False
    in_combat = False
    do_attack = False
    lose = False
    win = False
    while not stop_game:
        for event in pygame.event.get():
            
            # Event handling
            if event.type == pygame.KEYDOWN:
                if event.key == KEY_UP:
                    sir_david_quinith.y_dir = -4
                elif event.key == KEY_DOWN:
                    sir_david_quinith.y_dir = 4
                elif event.key == KEY_LEFT:
                    sir_david_quinith.x_dir = -4
                elif event.key == KEY_RIGHT:
                    sir_david_quinith.x_dir = 4

                elif event.key == pygame.K_1:
                    sir_david_quinith.attack += 15 + extra_attack
                    Yakumo_Omori.attack += randint(10,30)
                        
                elif event.key == pygame.K_2:
                    if heavy_attack_count < 2:
                        heavy_attack_count += 1
                        sir_david_quinith.attack += 20 + extra_attack
                        Yakumo_Omori.attack += randint(10, 40)
                            
                elif event.key == pygame.K_3:
                    if spell_attack_count < 2:
                        spell_attack_count += 1
                        sir_david_quinith.attack += 65 + extra_attack
                        Yakumo_Omori.attack += (randint(30, 50)) + (randint(10, 20))
                            
                elif event.key == pygame.K_RETURN:
                    main()
                
                elif event.key == pygame.K_q:
                    stop_game = True

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
        player_hit_list = pygame.sprite.spritecollide(sir_david_quinith, block_list, True)
        for block in player_hit_list:
            fighting_sprite_list.add(block)

            if pygame.sprite.collide_rect(sir_david_quinith, Yakumo_Omori):
                in_combat = True
            
            if pygame.sprite.collide_rect(sir_david_quinith, Eto):
                extra_attack += 10
            
            if pygame.sprite.collide_rect(sir_david_quinith, extra_monster_1):
                extra_attack += 10

            if pygame.sprite.collide_rect(sir_david_quinith, extra_monster_2):
                extra_attack += 10

            if pygame.sprite.collide_rect(sir_david_quinith, extra_monster_3):
                extra_attack += 10        

            if pygame.sprite.collide_rect(sir_david_quinith, extra_monster_4):
                extra_attack += 10

            if pygame.sprite.collide_rect(sir_david_quinith, extra_monster_5):
                extra_attack += 10
        
        

            
        
        if in_combat == True:
            do_attack = True
            
            monster_health = Yakumo_Omori.health
            monster_attack = Yakumo_Omori.attack
            user_attack = sir_david_quinith.attack
            user_health = sir_david_quinith.health

            if do_attack == True:
                monster_health -= sir_david_quinith.attack
                user_health -= Yakumo_Omori.attack
                if monster_health <= 0:
                    win = True
                    # in_combat = False #this was origionally here bc we were supposed to fight multiple monsters but shelved atm
                if user_health <= 0:
                    lose = True



        block_list.update(width, height)
        # Draw background
        #If the player is not in combat show normal screen and characters
        if in_combat == False:
            screen.blit(background_img, (0,0))
            block_list.draw(screen)
            sir_david_quinith.render(screen)
            sir_david_quinith.update(width,height)

            font = pygame.font.Font(None, 30)
            block_extra_attack = font.render("Extra character attack: %d" % extra_attack, True, (bright_pink))
            rect_extra_attack = block_extra_attack.get_rect().move(50, 50)
            screen.blit(block_extra_attack, rect_extra_attack)


            # if player is is in combat it loads the combat screen
        elif in_combat == True:
            screen.fill(black)
            combat_screen.blit(combat_background, (224,240))
            combat_sprites_list.draw(combat_background)

            if not lose and not win:

                font = pygame.font.Font(None, 25)
                block = font.render("Press 1 for normal attack", True, (blue))
                rect = block.get_rect().move(360, 420)
                screen.blit(block, rect)

                # pygame.display.update()
                # font2 = pygame.font.Font(None, 25)
                block2 = font.render("Press 2 for heavy attack", True, (blue))
                rect2= block2.get_rect().move(364,470)
                combat_screen.blit(block2, rect2)

                block5 = font.render("Press 3 for heavy attack", True, (blue))
                rect5= block2.get_rect().move(364,520)
                combat_screen.blit(block5, rect5)

                block3 = font.render(str(monster_health), True, (red))
                rect3= block3.get_rect().move(449,350)
                combat_screen.blit(block3, rect3)

                block4 = font.render(str(user_health), True, (green))
                rect4= block4.get_rect().move(449,595)
                combat_screen.blit(block4, rect4)

            if lose == True:
                font_lose = pygame.font.Font(None, 30)
                block_lose = font_lose.render("You lose! Sorry!", True, (black))
                rect_lose = block_lose.get_rect()
                rect_lose.center = combat_screen.get_rect().center
                combat_screen.blit(block_lose, rect_lose)

                font_try_again = pygame.font.Font(None, 30)
                block_try_again = font_try_again.render("Play again? Press enter to resart, or 'q' to exit!", True, (black))
                rect_try_again = block_try_again.get_rect().move(242, 500)
                combat_screen.blit(block_try_again, rect_try_again)
            
            if win == True:
                font_win = pygame.font.Font(None, 30)
                block_win = font_win.render("You Won! Great job!", True, (bright_pink))
                rect_win = block_win.get_rect()
                rect_win.center = combat_screen.get_rect().center
                combat_screen.blit(block_win, rect_win)

                font_try_again = pygame.font.Font(None, 30)
                block_try_again = font_try_again.render("Play again? Press enter to resart or Q to exit", True, (bright_pink))
                rect_try_again = block_try_again.get_rect().move(242, 500)
                combat_screen.blit(block_try_again, rect_try_again)


        # Game display


        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
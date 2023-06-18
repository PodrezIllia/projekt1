import settings
import pygame
import area 
import dicts
import os 
win = pygame.display.set_mode((dicts.SETTINGS_WIN["WIDTH"], dicts.SETTINGS_WIN["HEIGHT"]))
flag_bullet_die = False
class Sounds:
    def __init__(self, sound = None):
        self.DIE_BULLET_VERSION = sound
        self.DIE_BULLET_VERSION = pygame.mixer.Sound(os.path.join(os.path.abspath(__file__ + '/..'), 'sounds/die_bullet_version.wav'))
        self.PISTOL_SHOOT = sound
        self.PISTOL_SHOOT = pygame.mixer.Sound(os.path.join(os.path.abspath(__file__ + '/..'), 'sounds/pistol_shoot.wav'))
        self.DIE_SMOKE_VERSION = sound
        self.DIE_SMOKE_VERSION = pygame.mixer.Sound(os.path.join(os.path.abspath(__file__ + '/..'), 'sounds/die_smoke_version.wav'))
die_bullet_version = Sounds('sounds/die_bullet_version.wav')
pistol_shoot = Sounds('sounds/pistol_shoot.wav')
die_smoke_version = Sounds('sounds/die_smoke_version.wav')
        
class Sprite(settings.Settings):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.STEP = 2
        self.GRAVITY = 6
        self.ACTIVE_GRAVITY = True
        self.CAN_MOVE_RIGHT = True
        self.CAN_MOVE_LEFT = True
        self.COUNT_JUMP = 0
        self.JUMP = False
        self.KEY_PRESSED = False
        self.OPEN_DOOR = False
        self.MASK_ON = False
        self.INJURED = False
        self.EXIT_DOOR = False
        self.MEDIC_MOVE_RIGHT = False
        self.MEDIC_MOVE_LEFT = False
        self.MOVE_BULLET = False
    def move_sprite(self):
            event = pygame.key.get_pressed()
            if event[pygame.K_RIGHT] and self.X + self.WIDTH <= dicts.SETTINGS_WIN["WIDTH"]:
                if self.CAN_MOVE_RIGHT == True:
                    self.X += self.STEP
                    # walk_sound.WALK_SOUND.play()
                    # self.RECT.x = self.RECT.x + self.STEP
            elif event[pygame.K_LEFT] and self.X + 1 >= 0:   
                   if self.CAN_MOVE_LEFT == True:      
                        self.X -= self.STEP
                        # walk_sound.WALK_SOUND.play()
                        # self.RECT.x = self.RECT.x - self.STEP 

     #
    def jump(self, list_rect):
        event = pygame.key.get_pressed()
        #
        if event[pygame.K_UP] and self.KEY_PRESSED == False:
            self.KEY_PRESSED = True
        #
        if self.KEY_PRESSED and self.COUNT_JUMP <= 30:
            self.JUMP = True
            self.COUNT_JUMP += 1
            # self.RECT.y -= 11
            self.Y -= 11
            self.can_move_up(list_rect)
        if self.COUNT_JUMP > 30:
            self.JUMP = False 
            # self.KEY_PRESSED = False
            # self.COUNT_JUMP = 0
            
    def medic_move(self):
        if self.MEDIC_MOVE_LEFT == True:
                self.X -= 2
        if self.MEDIC_MOVE_RIGHT == True:
            # print(1111111111)
                self.X += 2
        if self.X + self.WIDTH < 0:
            self.MEDIC_MOVE_LEFT = False
        if self.X > 800:
            self.MEDIC_MOVE_RIGHT = False
    def medic_move_screen(self):
        if self.X < 0:
            # print(1)
            self.X += 5
        if self.X > 800:
            # print(1111111111)
                self.MEDIC_MOVE_LEFT = True
        

    def gravity(self, list_rect):
       
        self.can_move_down(list_rect)
        if self.ACTIVE_GRAVITY:
            self.Y += self.GRAVITY
            
        
    def can_move_right(self, list_rect):
        for block in list_rect:
            if self.Y + 10 <= block.Y + block.HEIGHT and self.Y + self.HEIGHT - 10 >= block.Y:
                # print(block.HEIGHT, "23e43ed3sede")
                if self.X + self.WIDTH <= block.X + self.STEP and self.X + self.WIDTH >= block.X:
                    self.CAN_MOVE_RIGHT = False
                    self.X -= self.STEP
                    # self.RECT.x -= 3
                    break
                else:
                    self.CAN_MOVE_RIGHT = True
    def can_move_left(self, list_rect):
        for block in list_rect:
            if  self.Y + 10 <= block.Y + block.HEIGHT and self.Y + self.HEIGHT - 10 >= block.Y:
                # print(block.HEIGHT, "23e43ed3sede")
                if self.X >= block.X - self.STEP and self.X <= block.X + block.WIDTH:
                        self.CAN_MOVE_LEFT = False
                        self.X += self.STEP
                        # self.RECT.x += 3
                        break
                else:
                    self.CAN_MOVE_LEFT = True
    def can_move_down(self, list_rect):
        
        for block in list_rect:
            if self.X <= block.X + block.WIDTH and self.X + self.WIDTH >= block.X:
                # print(self.Y + self.HEIGHT, block.Y, self.Y)
                if self.Y + self.HEIGHT >= block.Y and self.Y + self.HEIGHT <= block.Y + self.GRAVITY:
                    # print(self.Y + self.HEIGHT, block.Y, self.Y)
                    # print(self.Y + self.HEIGHT, block.Y)
                    # self.RECT.Y = block.Y - self.RECT.height - 1
                # if block.Y + block.height > self.RECT.Y:
                    self.ACTIVE_GRAVITY = False
                    self.COUNT_JUMP = 0
                    self.KEY_PRESSED = False
                    self.Y = block.Y - self.HEIGHT
                      
                    break
                else:
                    self.ACTIVE_GRAVITY = True
                

    def can_move_up(self, list_rect):
        for block in list_rect:
            if self.Y <= block.Y + block.HEIGHT and self.Y + self.HEIGHT >= block.Y + block.HEIGHT:
                if self.X + 50>= block.X and self.X + self.WIDTH - 50 <= block.X + block.WIDTH:
                    self.COUNT_JUMP = 41
                    self.ACTIVE_GRAVITY = True
            # if block.x <= self.X + self.WIDTH and block.x + block.width >= self.X + self.WIDTH:
            #     if block.Y + block.height > self.Y:
            #         self.COUNT_JUMP = 41
            #         self.ACTIVE_GRAVITY = True
    def draw_text(self, win, key):
        font = pygame.font.SysFont("kokila", 20)
        follow = font.render(f"нажмите {key} что бы взаимодействовать с предметами!", 1, (0,0,0))
        win.blit(follow, (100, 200))

    def lever_collide(self, win):
        event = pygame.key.get_pressed()
        if self.X + self.WIDTH <= settings.lever.X + settings.lever.WIDTH + 20 and self.X + 20 >= settings.lever.X:
            if self.Y >= settings.lever.HEIGHT + 20 and self.Y + self.HEIGHT <= settings.lever.Y + settings.lever.HEIGHT + 20:
                self.draw_text(win, "E")
                if event[pygame.K_e]:
                #    print(22222)
                   self.OPEN_DOOR = True
    def mask_collide(self, win):
        event = pygame.key.get_pressed()
        if self.X + self.WIDTH <= mask.X + mask.WIDTH + 20 and self.X + 20 >= mask.X:
            # print(5555)
            # print(self.RECT.y  + 21 >= mask.RECT.y, self.RECT.y + 21, mask.RECT.y)
            if self.Y + 21 >= mask.Y and self.Y + self.HEIGHT <= mask.Y + mask.HEIGHT + 20:
                self.draw_text(win, "R")
                # print(2222223333)
                if event[pygame.K_r]:
                    # print(222222)'
                    self.MASK_ON = True
                    self.NAME_IMAGE = "game2/images/sprite_with_injured.png"
                    mask.NAME_IMAGE = None
                    self.load_image()

    def injured_collide(self):
        event = pygame.key.get_pressed()
        if self.X + self.WIDTH <= settings.injured.X + settings.injured.WIDTH + 20 and self.X + 20 >= settings.injured.X:
            if self.Y + 21 >= settings.injured.Y and self.Y + self.HEIGHT <= settings.injured.Y + settings.injured.HEIGHT + 20:
                self.draw_text(win, "F")
                if event[pygame.K_f]:
                    self.NAME_IMAGE = "game2/images/sprite_with_injured.png"
                    self.load_image()
                    self.INJURED = True
    def position(self):
        event = pygame.key.get_pressed()
        if event[pygame.K_t]:
            print(self.X)
    def door_collide(self):
        if not self.OPEN_DOOR:
            if self.Y >= door.Y and self.Y + self.HEIGHT - 10 <= door.Y + door.HEIGHT:
                # print(11111)
                if self.X + self.WIDTH >= door.X:
                    # print(5555)
                    self.CAN_MOVE_RIGHT = False
                    self.X -= 3
                    self.X -= 3
        if self.OPEN_DOOR:
            # print(1111)
            door.NAME_IMAGE = None
            door.IMAGE = None
    # def open_door(self):
    #     if self.OPEN_DOOR:
    #         print(1111)
    #         self.NAME_IMAGE = None
    def bullet(self):
        global flag_bullet_die
        for block in area.list_rect:
            if block.X <= bullet.X + bullet.WIDTH and block.X + block.WIDTH > bullet.X + bullet.WIDTH:
                if bullet.HEIGHT > block.Y - bullet.HEIGHT and bullet.Y + bullet.HEIGHT < block.y + bullet.HEIGHT + block.HEIGHT:
                    self.MOVE_BULLET = False
                    break
                else:
                    self.MOVE_BULLET = True
            else:
                self.MOVE_BULLET = True
        if self.MOVE_BULLET:
            # print("erhbhUIWRHOIQHOUE")
            if sprite.X + sprite.WIDTH <= bullet.X + bullet.WIDTH and sprite.X >= bullet.X:
                # print("aoaoaooa")
                # if sprite.Y >= bullet.Y and sprite.Y + sprite.HEIGHT <= bullet.Y + bullet.HEIGHT:
                # print("ulygiguoviuo")
                die_bullet_version.DIE_BULLET_VERSION.play()
                self.MOVE_BULLET = False
                flag_bullet_die = True
        if bullet.X <= 0:
            self.MOVE_BULLET = False
        if bullet.X >= 800:
            self.MOVE_BULLET = False
        pistol_shoot.PISTOL_SHOOT.play()
        if self.MOVE_BULLET:
            # print(111111)
            bullet.X += self.STEP
    def medic_bot(self):
        if self.X.collidepoint(medic_bot.X, medic_bot.Y):
            print("123")

    def door_exit_collide(self):
        if self.INJURED:
            if self.Y >= door_exit.Y and self.Y + self.HEIGHT - 10 <= door_exit.Y + door_exit.HEIGHT:
                # print(11111)
                if self.X + self.WIDTH >= door_exit.X:
                    event = pygame.key.get_pressed()
                    self.draw_text(win, "E")
                    if event[pygame.K_e]:
                        # self.OPEN_DOOR = False
                        self.EXIT_DOOR = True
                
                


sprite = Sprite(color = (0,0,0), x = 330, y = 600, width = 50, height = 60, name_image = "game2/images/sprite.png")
smoke = Sprite(x = 0, y = 750, width = 50, height = 50, name_image = "game2/images/smoke.png")
mask = Sprite(x = 5, y = 5, width = 50, height = 50, name_image = "game2/images/mask.png")
door = Sprite(x = 520, y = 600, width = 120, height = 120, name_image = "game2/images/door.png")
door_exit = Sprite(x = 600, y = 0, width = 120, height = 120, name_image = "game2/images/door.png")
medic_bot = Sprite(x = 20, y = 660, width = 50, height = 50, name_image = "game2/images/enemy.png")
sprite_2 = Sprite(color = (0,0,0), x = 300, y = 660, width = 50, height = 60, name_image = "game2/images/sprite.png")
bullet = Sprite(x = 100, y = 660, width = 50, height = 50, name_image = "game2/images/bullet.png")
medic_escape = Sprite(x = 0, y = 0, width = 800, height = 800, name_image = "game2/images/medic_escape.png")
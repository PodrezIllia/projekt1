import pygame 
import dicts 
import settings
import area
import sprite
pygame.init()
smoke_width = 50
smoke_height = 50
smoke_x = 0
smoke_y = 750
smoke = sprite.Sprite(x = smoke_x, y = smoke_y, width = smoke_width, height = smoke_height, name_image = "game2/images/smoke.png")
scene1 = False
level1 = False
level2 = True
scene3 = False
smoke_count = 0 
fps = 60
win = pygame.display.set_mode((dicts.SETTINGS_WIN["WIDTH"], dicts.SETTINGS_WIN["HEIGHT"]))
pygame.display.set_caption("game")
area.create_world(area.list_world_2)
def run_game():
    global smoke
    global scene1
    global level1
    global scene3
    # global level2
    clock = pygame.time.Clock()
    move_medic_count = 0
    medic_left = 0
    game = True
    medic_left_count_1 = 0
    medic_right = 0
    medic_right_count_1 = 0
    medic_right_count_2 = 0
    medic_right_count_3 = 0
    move_medic_right = False
    move_medic_left = True
    last_medic_time_move = 0
    last_medic_time_move_count = 0
    while game:
        last_medic_time_move += 1
        move_medic_count += 1
        print(last_medic_time_move)
        global smoke_x
        global smoke_y
        global smoke_height
        global smoke_width
        global smoke_count
        global level2
        # for event in pygame.event.get():
        if scene1: #пажасата заработай   '
            settings.bg_menu.blit_sprite(win)
            settings.play.blit_sprite(win)
            settings.developers.blit_sprite(win)
            settings.exit.blit_sprite(win)
            # settings.play.draw_rect(win)
            # settings.developers.draw_rect(win)
            # settings.exit.draw_rect(win)
            # for event in pygame.event.get():
            #     if event.type == pygame.QUIT:
            #         game = False  
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game = False  
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    click = event.pos 
                    print(click)
                    if settings.play.RECT.collidepoint(click):
                        print(1)
                        level1 = True
                        area.create_world(area.list_world_1)
                        scene1 = False
                    if settings.exit.RECT.collidepoint(click):
                        print(2)
                        game = False 
                    if settings.developers.RECT.collidepoint(click):
                        print(3)
                        scene3 = True
                        scene1 = False
                        
                if event.type == pygame.MOUSEMOTION:
                    if settings.play.RECT.collidepoint(event.pos):
                        settings.play = settings.Settings(x = 365,y = 115, width = 75, height = 35,name_image = "game2/images/play.png")
                    if not settings.play.RECT.collidepoint(event.pos):
                        settings.play = settings.Settings(x = 350,y = 100, width = 100, height = 50,name_image = "game2/images/play.png")

                    if settings.developers.RECT.collidepoint(event.pos):
                       
                        settings.developers = settings.Settings(x = 365,y = 200, width = 75, height = 35,name_image = "game2/images/developers.png")
                    if not settings.developers.RECT.collidepoint(event.pos):
                        settings.developers = settings.Settings(x = 350,y = 175, width = 100, height = 50,name_image = "game2/images/developers.png")

                    if settings.exit.RECT.collidepoint(event.pos):
                        settings.exit = settings.Settings(x = 365,y = 275, width = 75, height = 35,name_image = "game2/images/exit.png")
                    if not settings.exit.RECT.collidepoint(event.pos):
                        settings.exit = settings.Settings(x = 350,y = 250, width = 100, height = 50,name_image = "game2/images/exit.png")
            pygame.display.flip()

        if level1: 
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    click = event.pos 
                    print(click)
                if event.type == pygame.QUIT:
                    game = False  
            # print(clock.get_fps())
            smoke_count += 1
            settings.bg.blit_sprite(win)
            sprite.sprite.can_move_right(area.list_rect)
            sprite.sprite.can_move_left(area.list_rect)
            # sprite.sprite.can_move_down(area.list_rect)
            sprite.sprite.move_sprite()
            sprite.sprite.jump(area.list_rect)
            sprite.sprite.blit_sprite(win)
            sprite.sprite.gravity(list_rect= area.list_rect)
            sprite.smoke.blit_sprite(win)
            if sprite.mask.IMAGE != None:
                sprite.mask.blit_sprite(win)
            sprite.mask.gravity(list_rect= area.list_rect)
            settings.lever.blit_sprite(win)
            settings.injured.blit_sprite(win)
                # settings.mask.NAME_IMAGE = None
            sprite.sprite.lever_collide(win)
            sprite.sprite.mask_collide(win)
            sprite.sprite.injured_collide()
            # sprite.sprite.draw_rect(win)
            if sprite.door.IMAGE != None:
                sprite.door.blit_sprite(win)
            sprite.sprite.door_collide()
            sprite.door_exit.blit_sprite(win)
            sprite.sprite.door_exit_collide()
            # sprite.door.open_door()
            # sprite.sprite.draw_text(win, )
            
            for el in area.list_create_world:
                el.blit_sprite(win)

            if smoke_count == 50:
                # sprite.smoke.WIDTH += 50
                # sprite.smoke.HEIGHT += 50
                # print(1)
                smoke_width += 50
                smoke_height += 50
                # smoke_x += 20
                smoke_y -= 20
                smoke = sprite.Sprite(x = smoke_x, y = smoke_y, width = smoke_width, height = smoke_height, name_image = "game2/images/smoke.png")
                # smoke.blit_sprite(win)
                smoke_count = 0

            smoke.blit_sprite(win)
            #условие смерти от дыма
            sprite.sprite.position()
            x = sprite.sprite.X
            y = sprite.sprite.Y
            sprite_cor = x,y
            if sprite.sprite.X + sprite.sprite.WIDTH <= smoke.X + smoke.WIDTH + 20 and sprite.sprite.X + 20 >= smoke.X:
                if sprite.sprite.Y + 21 >= smoke.Y and sprite.sprite.Y + sprite.sprite.HEIGHT <= smoke.Y + smoke.HEIGHT + 20:
                    if sprite.sprite.MASK_ON == True:
                        pass
                    else:
                        smoke = sprite.Sprite(x = 0, y = 750, width = 50, height = 50, name_image = "game2/images/smoke.png")
                        smoke_width = 50
                        smoke_height = 50
                        smoke_x = 0
                        smoke_y = 750

                        sprite.die_smoke_version.DIE_SMOKE_VERSION.play()
                        level1 = False
                        scene1 = True
                        smoke_count = 0
                      # print("touch")
            if sprite.sprite.EXIT_DOOR:
                level2 = True
                area.create_world(area.list_world_2)
                level1 = False
            pygame.display.flip()
        if level2: 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game = False  
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    click = event.pos 
                    print(click)
            settings.bg.blit_sprite(win)
            # area.create_world(area.list_world_2)
            for el in area.list_create_world:
                el.blit_sprite(win)
            sprite.sprite_2.can_move_right(area.list_rect)
            sprite.sprite_2.can_move_left(area.list_rect)
            # sprite.sprite.can_move_down(area.list_rect)
            sprite.sprite_2.move_sprite()
            sprite.sprite_2.jump(area.list_rect)
            sprite.sprite_2.blit_sprite(win)
            sprite.sprite_2.gravity(list_rect= area.list_rect) 
            sprite.medic_bot.blit_sprite(win)
            sprite.medic_bot.medic_move()
            # sprite.medic_bot.medic_move_screen()
            # sprite.medic_bot.can_move_left(list_rect= area.list_rect)
            # sprite.medic_bot.can_move_right(list_rect= area.list_rect)
            # print(sprite.medic_bot.X)
            sprite.medic_bot.gravity(list_rect= area.list_rect)
            sprite.bullet.blit_sprite(win)
            sprite.sprite_2.bullet()
            if sprite.flag_bullet_die == True:
                level2 = False
                scene1 = True
            if move_medic_count == 150 and medic_left != 5 and move_medic_left == True:
                print(11111)
                sprite.medic_bot.MEDIC_MOVE_LEFT = True
                move_medic_count = -100
                medic_left += 1
            # else:
            #     sprite.medic_bot.MEDIC_MOVE_LEFT = False
            if medic_left == 2:
                    sprite.medic_bot.MEDIC_MOVE_LEFT = False
                    sprite.medic_bot.X = 0
                    sprite.medic_bot.Y = 190
                # print(sprite.medic_bot.X)
                # print(1)
            if medic_left == 4:
                if medic_left_count_1 != 1:
                    sprite.medic_bot.MEDIC_MOVE_LEFT = False
                    sprite.medic_bot.X = 0
                    sprite.medic_bot.Y = 0
                    medic_left_count_1 += 1
                    move_medic_right = True
                    medic_left = 0
                    move_medic_left = False
            if move_medic_count == 150 and medic_right != 6 and move_medic_right == True:
                medic_left_count_1 = 0
                sprite.medic_bot.MEDIC_MOVE_LEFT = False
                # print(11111)
                sprite.medic_bot.MEDIC_MOVE_RIGHT = True
                move_medic_count = -100
                medic_right += 1
            if medic_right == 1:
                if medic_right_count_1 != 1:
                    # print(22222)
                    sprite.medic_bot.MEDIC_MOVE_RIGHT = False
                    sprite.medic_bot.X = 750
                    sprite.medic_bot.Y = 70
                    # sprite.medic_bot.gravity(list_rect= area.list_rect)
                    # medic_right_count_1 += 1
                # print(sprite.medic_bot.X)
                # print(1)
            if medic_right == 3:
                if medic_right_count_2 != 1:
                    sprite.medic_bot.MEDIC_MOVE_RIGHT = False
                    sprite.medic_bot.X = 750
                    sprite.medic_bot.Y = 630
                    medic_right_count_2 += 1
            if medic_right == 5:
                if medic_right_count_3 != 1:
                    sprite.medic_bot.MEDIC_MOVE_RIGHT = False
                    sprite.medic_bot.X = 750
                    sprite.medic_bot.Y = 190
                    move_medic_left = True
                    move_medic_count = 0
                    medic_right = 0
                    move_medic_right = False
                    medic_right_count_3 += 1
            if last_medic_time_move > 2250 and last_medic_time_move_count < 3:
                sprite.medic_bot.X = 0
                sprite.medic_bot.Y = 660
                last_medic_time_move = 0
                last_medic_time_move_count += 1
                if last_medic_time_move_count == 2:
                    last_medic_time_move += 1800
            if last_medic_time_move_count >= 3:
                sprite.medic_escape.blit_sprite(win)
            pygame.display.flip()
        if scene3:
            settings.bg_developers.blit_sprite(win)
            settings.back.blit_sprite(win)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    click = event.pos
                    if settings.back.RECT.collidepoint(click):
                        scene1 = True
                        scene3 = False
                if event.type == pygame.MOUSEMOTION:
                    if settings.back.RECT.collidepoint(event.pos):
                        settings.back = settings.Settings(x = 715,y = 0, width = 75, height = 45,name_image = "game2/images/back.png")
                    if not settings.back.RECT.collidepoint(event.pos):
                        settings.back = settings.Settings(x = 700,y = 0, width = 100, height = 50,name_image = "game2/images/back.png")
            pygame.display.flip()
        clock.tick(fps)      
run_game() 
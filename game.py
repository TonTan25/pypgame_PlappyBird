from importlib.resources import read_text
import re
import pygame, sys , random
from pygame import display

from pygame.time import Clock
from pygame.transform import rotate

pygame.mixer.pre_init(frequency=44100,size=-16,channels=2,buffer=512)
pygame.init()
###--- tao ham 
def create_cot():
    random_cot_pos = random.choice(cot_heght)
    bot_cot = cot.get_rect(midtop = (500,random_cot_pos))
    top_cot = cot.get_rect(midtop = (500,random_cot_pos - 500))
    return bot_cot,top_cot
def move_cot(cots):
    for pipe in cots :
        pipe.centerx -= 5
    return cots
def draw_cot(cots):
    for pipe in cots:
        if pipe.bottom >= 600:
            screen.blit(cot,pipe)
        else:
            flip_cot = pygame.transform.flip(cot,False,True)
            screen.blit(flip_cot,pipe)
def draw_floor():
    screen.blit(floor,(floor_x_pos,550))
    screen.blit(floor,(floor_x_pos+432,550))
def check_vacham(cots): 
    for pipe in cots:
        if like_rect.colliderect(pipe):
            like_hit_sound.play()
            print('X')
            return False
    if like_rect.top <= -75:
        print('Y')
    elif like_rect.bottom >=550:
        return False
    return True
def rotate_like(like1):
    new_like = pygame.transform.rotozoom(like1,-like_movement*3,1)
    return new_like
def like_animation():
    new_like = like_list[like_index]
    new_like_rect = new_like.get_rect(center = (100,like_rect.centery))
    return new_like,new_like_rect
def over_animation():
    new_game_over = over_list[over_index]
    new_game_over_rect = new_game_over.get_rect(center = (216,game_over_rect.centery))
    return new_game_over,new_game_over_rect
def diem_display (game_state):
    if game_state == 'main game' :
        diem_sur = game_font.render(str(int(diem)),True,(125,125,125))
        diem_rect = diem_sur.get_rect(center = (216,100))
        screen.blit(diem_sur,diem_rect)
    if game_state == 'game_over':
        diem_sur = game_font.render(f'Score:{int(diem)}',True,(0,0,0))
        diem_rect = diem_sur.get_rect(center = (216,50))
        screen.blit(diem_sur,diem_rect)

        diem_cao_sur = game_font.render(f'High Score:{str(int(diem_cao))}',True,(0,0,0))
        diem_cao_rect = diem_cao_sur.get_rect(center = (216,100))
        screen.blit(diem_cao_sur,diem_cao_rect)
def update_diem(diem,diem_cao):
    if diem > int(diem_cao):
        diem_cao = diem
        return diem_cao
    else:
        return diem_cao
#--- chen backgroud 
screen = pygame.display.set_mode((432,700))
clock = pygame.time.Clock()
game_font = pygame.font.Font('images/04B_19.TTF',40)
### tao cac bien
game_active = True
gravity = 1 # trong luc
diem = 0
diem_cao = 0
like_movement = 0 
# tao man hinh ket thuc
over_1 = pygame.image.load('images/zero_two/1.jpg').convert()
over_2 = pygame.image.load('images/zero_two/2.jpg').convert()
over_3 = pygame.image.load('images/zero_two/3.jpg').convert()
over_4 = pygame.image.load('images/zero_two/4.jpg').convert()
over_5 = pygame.image.load('images/zero_two/5.jpg').convert()
over_6 = pygame.image.load('images/zero_two/6.jpg').convert()
over_7 = pygame.image.load('images/zero_two/7.jpg').convert()
over_8 = pygame.image.load('images/zero_two/8.jpg').convert()
over_9 = pygame.image.load('images/zero_two/9.jpg').convert()
over_10 = pygame.image.load('images/zero_two/10.jpg').convert()
over_11 = pygame.image.load('images/zero_two/11.jpg').convert()
over_12 = pygame.image.load('images/zero_two/12.jpg').convert()
over_13 = pygame.image.load('images/zero_two/13.jpg').convert()
over_14 = pygame.image.load('images/zero_two/14.jpg').convert()
over_15 = pygame.image.load('images/zero_two/15.jpg').convert()
over_16 = pygame.image.load('images/zero_two/16.jpg').convert()
over_17 = pygame.image.load('images/zero_two/17.jpg').convert()
over_18 = pygame.image.load('images/zero_two/18.jpg').convert()
over_19 = pygame.image.load('images/zero_two/19.jpg').convert()
over_20 = pygame.image.load('images/zero_two/20.jpg').convert()
over_list = [over_1,over_2,over_3,over_4,over_5,over_6,over_7,over_8,over_9,over_10,over_11,over_12,over_13,over_14,over_15,over_16,over_17,over_18,over_19,over_20]
over_index = 0
game_over = over_list[over_index]
game_over_rect = game_over.get_rect(center = (216,300))
game_over_change = pygame.USEREVENT + 1
pygame.time.set_timer(game_over_change,46)
#backgroud
bg = pygame.image.load('images/backgroud-3.jpg').convert()
#--- chen floor - san 
floor = pygame.image.load('images/no1.jpg').convert()
floor_x_pos = 0
#--- chen vat the
liked = pygame.image.load('images/liked.png').convert_alpha()
disliked = pygame.image.load('images/disliked.png').convert_alpha()
fliked = pygame.image.load('images/fliked.png').convert_alpha()
like_list = [disliked,liked,fliked]
like_index = 0
like = like_list[like_index]
# like = pygame.transform.scale2x(like)
like_rect = like.get_rect(center = (100, 350))
# tao time cho cho like
like_change = pygame.USEREVENT + 2
pygame.time.set_timer(like_change,200)
#--- chen chuong ngai vat
cot = pygame.image.load('images/cot.jpg').convert()
cot_list = []
# tao thoi gian xuat hien
spawn_cot = pygame.USEREVENT
pygame.time.set_timer(spawn_cot, 1500)
## tao chieu cao bat ki
cot_heght = [200,250,300,350,400]
# chen am thanh 
like_flap_sound = pygame.mixer.Sound('sound/sfx_wing.wav')
like_hit_sound = pygame.mixer.Sound('sound/sfx_hit.wav')
score_sound = pygame.mixer.Sound('sound/sfx_point.wav')
score_sound_countdown = 100
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_active:
                like_movement = 0
                like_movement =- 11
                like_flap_sound.play()
                print('z')
            if event.key == pygame.K_SPACE and game_active == False:
                game_active = True
                cot_list.clear()
                like_rect.center = (100,350)
                like_movement = 0
                diem = 0
        if event.type == spawn_cot :
            cot_list.extend(create_cot())
        if event.type == like_change:
            if like_index <2:
                like_index += 1
            else:
                like_index = 0  
            like, like_rect = like_animation()
        if event.type == game_over_change:
            if over_index < 19:
                over_index += 1
            else :
                over_index = 0
            game_over,game_over_rect = over_animation()
    screen.blit(bg,(0,0))
    if game_active :
        # liked
        like_movement += gravity
        rotated_like = rotate_like(like)
        like_rect.centery += like_movement
        screen.blit(rotated_like,like_rect)
        game_active = check_vacham(cot_list)
        #cot 
        cot_list = move_cot(cot_list)
        draw_cot(cot_list)
        diem_display('main game')
        diem += 0.015
        score_sound_countdown -=1
        if score_sound_countdown <= 0:
            score_sound.play()
            score_sound_countdown = 100
    else:
        screen.blit(game_over,game_over_rect)
        diem_cao = update_diem(diem,diem_cao)
        diem_display('game_over')
    #san 
    floor_x_pos -= 1 
    draw_floor()
    if floor_x_pos <= -432:
        floor_x_pos = 0
    pygame.display.update()
    clock.tick(30)

from PPlay.gameimage import *
from PPlay.window import *
from PPlay.mouse import *
from PPlay.keyboard import *
from PPlay.sprite import *
from PPlay.sound import *


janela = Window(1200,700)
janela.set_title("ChronoLab")
mouse=Window.get_mouse()
teclado=Window.get_keyboard()
fundo=Sprite("midia//fundoMenu.png",1)
fundo2=Sprite("midia//Menu.png",54)
fundo2.set_sequence_time(0,54,50,True)
fundo_ctrl = Sprite("midia//fundo_menu2.png")

jogar = Sprite("midia//jogar.png",2)
controles = Sprite("midia//controles.png",2)
sair = Sprite("midia//sair.png",2)
jogar.set_sequence_time(0,1,120,True)
controles.set_sequence_time(0,1,120,True)
sair.set_sequence_time(0,1,120,True)


jogar.x=janela.width/2 - jogar.width/2
jogar.y=janela.height/1.5

controles.x=janela.width/2 - controles.width/2
controles.y=janela.height/1.335

sair.x=janela.width/2 - sair.width/2
sair.y=janela.height/1.2

menu_frames=[0,0,0,0]
for i in range(4):
    menu_frames[i]=Sprite("midia//menu_frame.png")
andar = Sprite("midia//andando_bob.png",8)
andar.set_sequence_time(0,8,100,True)
ataque = Sprite("midia//batendo_bob2.png",8)
ataque.set_sequence_time(0,8,75,True)
player_parry = Sprite("midia//Parry.png",1)
pular = Sprite("midia//pulando.png",11)
pular.set_sequence_time(0,11,65,True)
ad = Sprite("midia//a d.png")
l = Sprite("midia//l.png")
k = Sprite("midia//k.png")
space = Sprite("midia//space.png")

andar.x = janela.width/4 - andar.width/2
menu_frames[0].x= janela.width/4 - menu_frames[0].width/2   #andar.x-menu_frames[0].width/2+andar.width/2
ataque.x = janela.width/4 - andar.width/1.55
menu_frames[1].x= menu_frames[0].x
pular.x = 3 * janela.width/4 - andar.width/4
menu_frames[2].x= 3 * janela.width/4 - menu_frames[0].width/2
player_parry.x = 3 * janela.width/4 - andar.width/5
menu_frames[3].x= 3 * janela.width/4 - menu_frames[0].width/2
andar.y = janela.height/4
menu_frames[0].y= janela.height/4 - menu_frames[0].height/4 #andar.y-menu_frames[0].height/2+andar.height/2
pular.y = janela.height/4
menu_frames[1].y= 3 * janela.height/4 - menu_frames[0].height/3
ataque.y = 2.55 * janela.height/4
menu_frames[2].y= menu_frames[0].y
player_parry.y = 2.95 * janela.height/4
menu_frames[3].y=menu_frames[1].y
ad.x = menu_frames[0].x + menu_frames[0].width/2 - ad.width/2
l.x = menu_frames[1].x + menu_frames[1].width/2 - l.width/2
k.x = menu_frames[3].x + menu_frames[3].width/2 - k.width/2
space.x = menu_frames[2].x + menu_frames[2].width/2 - space.width/2
ad.y = menu_frames[0].y - ad.height
l.y = menu_frames[1].y - l.height
k.y = menu_frames[3].y - k.height
space.y = menu_frames[2].y - space.height



music_menu = Sound("midia//musica_menu2.wav")
music_menu.play()
music_menu.set_volume(7)

global delay_jogar
delay_jogar=-5
global state
state = "menu"

def Menu_principal():
    global delay_jogar
    global state
    if mouse.is_over_area([jogar.x,jogar.y],[jogar.x+jogar.width,jogar.y+jogar.height]):
        jogar.set_curr_frame(1)
        if delay_jogar==-5 and mouse.is_button_pressed(1):
            delay_jogar=2.7
    else:
        jogar.set_curr_frame(0)
    if mouse.is_over_area([controles.x,controles.y],[controles.x+controles.width,controles.y+controles.height]):
        controles.set_curr_frame(1)
        if delay_jogar==-5 and mouse.is_button_pressed(1):
            state = "tutorial"
    else:
        controles.set_curr_frame(0)
    if mouse.is_over_area([sair.x,sair.y],[sair.x+sair.width,sair.y+sair.height]):
        sair.set_curr_frame(1)
        if delay_jogar==-5 and mouse.is_button_pressed(1):
            janela.close()
    else:
        sair.set_curr_frame(0)


    if state=="menu":
        if delay_jogar!=-5:
            delay_jogar-=janela.delta_time()
            fundo2.update()
            fundo2.draw()
            if delay_jogar<0:
                music_menu.stop()
                delay_jogar=-5
                return 1
        else:
            fundo.draw()
            jogar.draw()
            controles.draw()
            sair.draw()
    else:
        fundo_ctrl.draw()
        for frame in menu_frames:
            frame.draw()
        ataque.draw()
        pular.draw()
        player_parry.draw()
        andar.draw()
        ataque.update()
        pular.update()
        andar.update()
        ad.draw()
        k.draw()
        l.draw()
        space.draw()
        if teclado.key_pressed("esc"):
            state="menu"



    janela.update()


    return 0


import random
from portas_e_paredes import *
from PPlay.sound import *

janela = Window(1200,700)
janela.set_title("ChronoLab")
teclado=Window.get_keyboard()

fire_snd = Sound("midia//fireball.mp3")
hit_snd = Sound("midia//hit.wav")
boss_snd = Sound("midia//musica boss.mp3")
fundo_snd = Sound("midia//musica_fundo2.mp3")
parry_snd = Sound("midia//parry.mp3")
sword_snd = Sound("midia//sword_5.wav")
porta_snd = Sound("midia//porta.mp3")
brk_glass1 = Sound("midia//brk_glass1.mp3")
brk_glass2 = Sound("midia//brk_glass2.mp3")
brk_glass3 = Sound("midia//brk_glass3.mp3")
gas_leak = Sound("midia//gas_leak.mp3")
step1 = Sound("midia//Step_1.mp3")
step2 = Sound("midia//Step_2.mp3")
Cenario = GameImage("midia//teste3_3.png")
plats =[0]*40
for i in range (len(plats)):
    plats[i] = GameImage("midia//chao_268px.png")
portas=[0]*17
for i in range (len(portas)):
    portas[i] = Sprite("midia//Scifi DoorGRN SpriteSheet.png",12)
    portas[i].set_sequence_time(0,12,70,True)
portas[3] = Sprite("midia//ptortaD.png")
portas[5] = Sprite("midia//ptortaD.png")
portas[2] = Sprite("midia//ptortaE.png")
portas[6] = Sprite("midia//ptortaE.png")
barra_vida = Sprite("midia//BarraDeVidaGRN.png",6)
barra_vida.set_sequence_time(0,6,100,True)
blipR1=[0]*10
blipR2=[0]*10
for i in range(len(blipR1)):
    blipR1[i] = Sprite("midia//blip_plat.png",8)
    blipR1[i].set_sequence_time(0,8,70,True)
    blipR2[i] = Sprite("midia//blip_plat2.png", 8)
    blipR2[i].set_sequence_time(0, 8, 70, True)
paredes = [0]*19 #16
for i in range (len(paredes)) :
    paredes[i]= Sprite("midia//parede.png",1)
paredes[1]= Sprite("midia//parede2.png",1)
paredes[3]= Sprite("midia//parede2.png",1)
paredes[4]= Sprite("midia//parede2.png",1)
paredes[6]= Sprite("midia//parede2.png",1)
paredes[11]=Sprite("midia//parede2P.png",1)
paredes[11].y=-1000
paredes[15]=Sprite("midia//parede2P.png",1)
paredes[15].y=-1000
paredes[13]=Sprite("midia//parede2P.png",1)
paredes[13].y=-1000
paredes[17]=Sprite("midia//parede2P.png",1)
paredes[17].y=-1000
paredes[12]=Sprite("midia//paredeP.png",1)
paredes[12].y=-1000
paredes[16]=Sprite("midia//paredeP.png",1)
paredes[16].y=-1000
paredes[18]=Sprite("midia//paredeP.png",1)
paredes[18].y=-1000
paredes[14]=Sprite("midia//paredeP.png",1)
paredes[14].y=-1000

olho_interage = Sprite("midia//interact.png",1)
hurt_ui = Sprite("midia//hurt_ui.png",6)
hurt_ui.set_sequence_time(0,6,120,True)
tank= Sprite("midia//tank-2.png",1)
tank2= Sprite("midia//tank-3.png",1)
tank3 =Sprite("midia//tank3.png",4)
tank3.set_sequence_time(0,4,120,True)
mesa = Sprite("midia//Mesa.png",2)
mesa.set_sequence_time(0,1,120,True)
maq_tempo = Sprite("midia//maquina_tempo.png",1)
corpo = Sprite("midia//dead.png")
calendario = Sprite("midia//calendario.png")
#ataque_player=[]
#ataque= Sprite("ataque_dir.png",4)
#ataque.set_sequence_time(0,4,60,True)
boss2 = Sprite("midia//boss2-idle.png",13)
boss2.set_sequence_time(0,13,120,True)
boss2_atkD = Sprite("midia//boss2-dash.png",16)
boss2_atkD.set_sequence_time(0,16,120,True)
boss2_stunD = Sprite("midia//boss2-dashstun.png",16)
boss2_stunD.set_sequence_time(0,16,120,True)
boss2E = Sprite("midia//boss2-idle2.png",13)
boss2E.set_sequence_time(0,13,120,True)
boss2_atkE = Sprite("midia//boss2-dash2.png",16)
boss2_atkE.set_sequence_time(0,16,120,True)
boss2_stunE = Sprite("midia//boss2-dashstun2.png",16)
boss2_stunE.set_sequence_time(0,16,120,True)

cuidado = Sprite("midia//Cuidado.png",1)
hit_effect=Sprite("midia//hit_effect.png",4)
hit_effect.set_sequence_time(0,4,120,True)
smoke_effect=Sprite("midia//fumaca.png",14)
smoke_effect.set_sequence_time(0,14,120,True)

inimigos_hp=[]
inimigos_pode_mover=[]
inimigo_orientation=[]
inimigos = []
inimigosE = []
inimigos_atacandoD = []
inimigos_atacandoE = []
inimigos_andandoD = []
inimigos_andandoE = []
inimigos_parryD = []
inimigos_parryE = []
inimigos_parry_delay=[]
for i in range (6):
    inimigos.append(Sprite("BlueWorm//Idle.png",9))
    inimigos[i].set_sequence_time(0,9,150,True)
    inimigosE.append(Sprite("BlueWorm//IdleE.png", 9))
    inimigosE[i].set_sequence_time(0, 9, 150, True)
    inimigos_atacandoD.append(Sprite("BlueWorm//Attack.png", 16))
    inimigos_atacandoD[i].set_sequence_time(0, 16, 100, True)
    inimigos_atacandoE.append(Sprite("BlueWorm//AttackE.png", 16))
    inimigos_atacandoE[i].set_sequence_time(0, 16, 100, True)
    inimigos_andandoD.append(Sprite("BlueWorm//Walk.png", 9))
    inimigos_andandoD[i].set_sequence_time(0, 9, 150, True)
    inimigos_andandoE.append(Sprite("BlueWorm//WalkE.png", 9))
    inimigos_andandoE[i].set_sequence_time(0, 9, 150, True)
    inimigos_parryD.append(Sprite("BlueWorm//Parried.png",5))
    inimigos_parryD[i].set_sequence_time(0, 5, 150, True)
    inimigos_parryE.append(Sprite("BlueWorm//ParriedE.png",5))
    inimigos_parryE[i].set_sequence_time(0, 5, 150, True)
    inimigos_hp.append(0)  #5
    inimigo_orientation.append("E")
    inimigos_pode_mover.append(True)
    inimigos_parry_delay.append(0)
    #inimigos[i].x, inimigos[i].y = -1000, -1000
inimigos_hp[0]=5
explosao = Sprite("midia//Explosion3x.png",7)
explosao.set_sequence_time(0,7,150,True)
explosaoBoss = Sprite("midia//Explosion5x.png",7)
explosaoBoss.set_sequence_time(0,7,150,True)
inimigos_ataques = []
fade = Sprite("midia//Fade.png",25)
fade.set_sequence_time(0,25,30,True)
fadeinstart = Sprite("midia//fade_out2.png",24)
fadeinstart.set_sequence_time(0,24,120,False)
caixa_dialogo = Sprite("midia//dialog_bubble.png",1) #colocar animacao da caixa de dialogo dps
caixa_dialogo.y=janela.height/5
caixa_dialogo_fundo=Sprite("midia//dialog_bubble_background.png",1)
caixa_dialogo_fundo.y=janela.height/5
tampa_texto=[Sprite("midia//tapa_texto.png",1),Sprite("midia//tapa_texto.png",1),Sprite("midia//tapa_texto.png",1)]
rosto_dialogo=[Sprite("midia//player_dialog1.png",1),Sprite("midia//Pers_mogado.png",1)]
buracos=[0]*10
for i in range (len(buracos)) :
    buracos[i] = Sprite("midia//buraco.png",1)
colisores_parede=[0]*35
for i in range(len(colisores_parede)):
    colisores_parede[i] = Sprite("midia//parede_colisor.png",1)

#player_paradoD = Sprite("bob.png",1)
player_paradoD = Sprite("midia//parado_idle.png",7)
player_paradoD.set_sequence_time(0,7,125,True)
player_paradoE = Sprite("midia//parado_idleE.png",7)
player_paradoE.set_sequence_time(0,7,125,True)
player_andandoD = Sprite("midia//andando_bob.png",8)
player_andandoD.set_sequence_time(0,8,100,True)
player_andandoE = Sprite("midia//andando_bobE.png",8)
player_andandoE.set_sequence_time(0,8,100,True)
player_atacando = Sprite("midia//batendo_bob2.png",8)
player_atacando.set_sequence_time(0,8,75,True)
player_atacandoE = Sprite("midia//batendo_bob2E.png",8)
player_atacandoE.set_sequence_time(0,8,75,True)
player_parry = Sprite("midia//Parry.png",1)
player_parryE = Sprite("midia//ParryE.png",1)
player_hitbox = Sprite("midia//bob_hitbox.png",1)
player_pulando = Sprite("midia//pulando.png",11)
player_pulando.set_sequence_time(0,11,65,True)
player_pulandoE = Sprite("midia//pulandoE.png",11)
player_pulandoE.set_sequence_time(0,11,65,True)
#player_parry.set_sequence_time()
chaves_obtidas=[0,0,0,0]

fundo_fim = Sprite("midia//corredor_fim.png",148)
fundo_fim.set_sequence_time(0,147,20,True)
andando_fim = Sprite("midia//andando_bob.png",8)
andando_fim.set_sequence_time(0,8,75,True)
fadin2 = Sprite("midia//fade_in.png",24)
fadin2.set_sequence_time(0,24,120,False)
fadout2 = Sprite("midia//fade_out2.png",24)
fadout2.set_sequence_time(0,24,120,False)

player_paradoD.x = janela.width/2 - player_paradoD.width/2
player_paradoD.y = janela.height/2 - player_paradoD.height/2
define_portas(portas)
define_parede(paredes)
define_plataformas(plats)
define_buracos(buracos)
define_colisores(colisores_parede)
define_blips(blipR1,blipR2)
barra_vida.x = barra_vida.width/8
barra_vida.y = barra_vida.height/4
cuidado.y = -1000

boss2.x = janela.width * 8
boss2.y = -1000
tank3.x = tank.width * 5.5
tank3.y = -1000#janela.height - tank.height * 1.25
tank2.x = tank.width * 7
tank2.y = -1000#janela.height - tank.height * 1.25
mesa.y=-100
mesa.x=janela.width
maq_tempo.x = tank.width * 3
maq_tempo.y = -1000
corpo.x = janela.width * 3 + plats[2].width*4
calendario.x = tank3.x + tank.width #+ calendario.width * 1.5
inimigos[0].x = janela.width * 1.2
inimigos[0].y = janela.height / 1.4 + 10 + player_paradoD.height - inimigos[0].height
tampa_texto[0].x=tampa_texto[1].x=tampa_texto[2].x=janela.width/4
tampa_texto[0].y=janela.height/4.2
tampa_texto[1].y=janela.height/3.4
tampa_texto[2].y=janela.height/2.85
warp = [Sprite("midia//buracoWarp.png",1),Sprite("midia//buracoWarp.png",1)]
warp[0].x = janela.width * 3 + plats[2].width * 10.75
warp[1].x = janela.width * 3 + plats[2].width * 0.9

for rosto in rosto_dialogo:
    rosto.x=janela.width/20
    rosto.y=janela.height/4 + 2

andando_fim.y = janela.height / 1.4 + 10
andando_fim.x = janela.width/2 - andando_fim.width/2


global conta_hit
global parry_cooldown
global parry_duration
global caindo_buraco
global rosto_dialogo_id
global camera_presaV
global camera_presaH
global text_dialogo
global prox_dialogo
global mostrar_dialogo
global pode_mover
global pode_interagir
global grav
global player_velx
global player_vely
global pulando
global fall
global posx_camera
global coyoteCooldown
global pulo_cooldown
global click_teclado_cooldown
global inimigos_ataques_cooldown
global player_ataques_cooldown
global sala
global player_animation
global inimigo_animation
global inimigo_velx
global player_hp
global fade_delay
global tempo_fade
global invencibilidade_cooldown
global ritmo_delay
global boss2_state
global boss2_atk_delay
global boss2_inner_atk_delay
global boss2_orientation
global boss2_atk_count
global num_dashs
global boss2_hp
global comeca_jogo
global porta_som_toca
global em_interagivel
global hurt_ui_delay
global started
global start_time
global fim_de_jogo
global acabou
global fade2delay
global musica_boss_tocando
global step_snd_delay
global atk_snd_delay

grav = 700

player_velx= 400
player_vely=0
pulando=0   #estar no ar
fall=0  #pulo dinâmico
posx_camera=0
coyoteCooldown=0
pulo_cooldown = 0
click_teclado_cooldown=3
inimigos_ataques_cooldown=0
player_ataques_cooldown=0
sala=0
player_orientation = "D"
player_animation = "parado"
inimigo_animation = ["paradoE"]*len(inimigos)
inimigo_velx= player_velx/1.8
player_hp=5
fade_delay=-1
tempo_fade = -1
pode_interagir=True
pode_mover=True
mostrar_dialogo=False
prox_dialogo=0
dialogos_lidos=[0,0,0,0] #switch para nao mostrar mais um dialogo quando terminado  #0 - nao lido, 1 - lido
text_dialogo=0
rosto_dialogo_id = 0
camera_presaH=False
camera_presaV=True
caindo_buraco=False
parry_duration = 1.5
parry_cooldown = 2
invencibilidade_cooldown = 1.5
conta_hit=True
ritmo_delay=1
bossfight=[0,0]  #0->inativo, 1->ocorrendo, 2->terminou
boss2_state="parado"
boss2_atk_delay=0
boss2_inner_atk_delay=0
boss2_orientation="D"
boss2_atk_count=0
num_dashs=5
boss2_hp=35
comeca_jogo=0
porta_som_toca=False
em_interagivel=False
hurt_ui_delay = 1
started=False
start_time=500000
fim_de_jogo=False
acabou=0
fade2delay=-1
musica_boss_tocando=False
step_snd_delay=1
atk_snd_delay=1


def movimentoCameraH(vel):
    #move a camera
    Cenario.x -= vel
    for plat in plats:
        plat.x -= vel
    for porta in portas:
        porta.x -= vel
    for parede in paredes:
        parede.x -=vel
    tank3.x -=vel
    tank2.x -= vel
    for inimigo in inimigos:
        inimigo.x -=vel
    #for inim_atk in inimigos_ataques:
    #    inim_atk.x -=vel
    #for atk in ataque_player:
    #    atk.x -= vel
    for buraco in buracos:
        buraco.x -=vel
    for colisores in colisores_parede:
        colisores.x -=vel
    for blips in blipR1:
        blips.x -= vel
    for blips in blipR2:
        blips.x -= vel
    boss2.x -= vel
    cuidado.x-=vel
    hit_effect.x -= vel
    explosao.x -=vel
    explosaoBoss.x -= vel
    for w in warp:
        w.x-=vel
    mesa.x-=vel
    maq_tempo.x -= vel
    corpo.x -=vel
    calendario.x -=vel

def movimentoCameraV(vel):
    # move a camera
    player_paradoD.y -=vel
    Cenario.y -= vel
    for plat in plats:
        plat.y -= vel
    for porta in portas:
        porta.y -= vel
    for parede in paredes:
        parede.y -= vel
    tank3.y -= vel
    tank2.y -= vel
    for inimigo in inimigos:
        inimigo.y -= vel
    #for inim_atk in inimigos_ataques:
    #    inim_atk.y -= vel
    #for atk in ataque_player:
    #    atk.y -= vel
    for buraco in buracos:
        buraco.y -= vel
    for colisores in colisores_parede:
        colisores.y -=vel
    for blips in blipR1:
        blips.y -=vel
    for blips in blipR2:
        blips.y -=vel
    boss2.y -= vel
    cuidado.y -=vel
    hit_effect.y -=vel
    explosao.y -=vel
    explosaoBoss.x -= vel
    for w in warp:
        w.y-=vel
    mesa.y -= vel
    maq_tempo.y -= vel
    corpo.y -= vel
    calendario.y -=vel

def check_camera_state():  #Atualiza a variavel camera_presaH (que diz se a camera mexe ou nao, nesse caso estamos limitando para nao passar da parede)
    global camera_presaH
    if sala == 0:
        if player_paradoD.x - paredes[3].x < janela.width/2 or paredes[0].x-player_paradoD.x < janela.width/4:
            camera_presaH=True
        else:
            camera_presaH=False
    elif sala == 1 or sala==5:
        if player_paradoD.x - paredes[1].x < janela.width/2 or paredes[2].x-player_paradoD.x < janela.width/4:
            camera_presaH=True
        else:
            camera_presaH=False
    elif sala == 2:
        if player_paradoD.x - paredes[4].x < janela.width / 2 or paredes[5].x - player_paradoD.x < janela.width / 4:
            camera_presaH = True
        else:
            camera_presaH = False
    elif sala == 3:
        if player_paradoD.x - paredes[4].x < janela.width / 2 or paredes[10].x - player_paradoD.x < janela.width / 4:
            camera_presaH = True
        else:
            camera_presaH = False
    elif sala == 6:
        if player_paradoD.x - paredes[6].x < janela.width / 2 or paredes[8].x - player_paradoD.x < janela.width / 4:
            camera_presaH = True
        else:
            camera_presaH = False
    elif sala == 7:
        if player_paradoD.x - paredes[6].x*8 < janela.width / 2 or paredes[9].x - player_paradoD.x < janela.width / 4:
            camera_presaH = True
        else:
            camera_presaH = False
    elif sala == 8 or sala==11:
        if player_paradoD.x - paredes[15].x < janela.width/2 or paredes[16].x-player_paradoD.x < janela.width/4:
            camera_presaH=True
        else:
            camera_presaH=False
    if sala == 9:
        if player_paradoD.x - paredes[11].x < janela.width/2 or paredes[12].x-player_paradoD.x < janela.width/4:
            camera_presaH=True
        else:
            camera_presaH=False
    elif sala == 10:
        if player_paradoD.x - paredes[13].x < janela.width / 2 or paredes[14].x - player_paradoD.x < janela.width / 4:
            camera_presaH = True
        else:
            camera_presaH = False

def teclado_click(Tec):
    global click_teclado_cooldown
    click_teclado_cooldown-=1
    if teclado.key_pressed(Tec) and click_teclado_cooldown < 0:
        click_teclado_cooldown = 3
        return 1
    if teclado.key_pressed(Tec):
        click_teclado_cooldown = 3
    return 0


def milissegundos(s):
    return janela.delta_time() *s

def colide_parede():
    # 1 -> colide parede direita,  2 -> colide parede esquerda
    if sala==0:
        if player_paradoD.x > paredes[0].x + paredes[0].width/3 - player_paradoD.width/1.5 and player_paradoD.collided(paredes[0]):
            return 1
        if player_paradoD.x < paredes[3].x + paredes[3].width/1.5 - player_paradoD.width/3 and player_paradoD.collided(paredes[3]):
            return 2
    elif sala==1 or sala==5:
        if player_paradoD.x > paredes[2].x + paredes[2].width/3 - player_paradoD.width/1.5 and player_paradoD.collided(paredes[2]):
            return 1
        if player_paradoD.x < paredes[1].x + paredes[1].width/1.5 - player_paradoD.width/3 and player_paradoD.collided(paredes[1]):
            return 2
    elif sala==2:
        if player_paradoD.x > paredes[5].x + paredes[5].width/3 - player_paradoD.width/1.5 and player_paradoD.collided(paredes[5]):
            return 1
        if player_paradoD.x < paredes[4].x + paredes[4].width/1.5 - player_paradoD.width/3 and player_paradoD.collided(paredes[4]):
            return 2
    elif sala==3:
        if player_paradoD.x > paredes[10].x + paredes[10].width/3 - player_paradoD.width/1.5 and player_paradoD.collided(paredes[10]):
            return 1
        if player_paradoD.x < paredes[4].x + paredes[4].width/1.5 - player_paradoD.width/3 and player_paradoD.collided(paredes[4]):
            return 2
    elif sala==6:
        if player_paradoD.x < paredes[6].x and player_paradoD.collided(paredes[6]):
            return 2
        if player_paradoD.x > paredes[8].x + paredes[8].width/1.5 - player_paradoD.width/1.5 and player_paradoD.collided(paredes[8]):
            return 1
        for col in colisores_parede:
            if col.x>0 and col.x< janela.width and player_paradoD.collided(col):
                if player_paradoD.x > col.x:
                    return 2
                else:
                    return 1
    elif sala==7:
        if player_paradoD.x < paredes[6].x and player_paradoD.collided(paredes[6]):
            return 2
        if player_paradoD.x > paredes[9].x + paredes[9].width/1.5 - player_paradoD.width/1.5 and player_paradoD.collided(paredes[9]):
            return 1
        for i in range(25,len(colisores_parede)):
            if colisores_parede[i].x>0 and colisores_parede[i].x< janela.width and player_paradoD.collided(colisores_parede[i]):
                if player_paradoD.x > colisores_parede[i].x:
                    return 2
                else:
                    return 1
    elif sala==8:
        if player_paradoD.x > paredes[16].x + paredes[16].width/3 - player_paradoD.width/1.5 and player_paradoD.collided(paredes[16]):
            return 1
        if player_paradoD.x < paredes[15].x + paredes[15].width/1.5 - player_paradoD.width/3 and player_paradoD.collided(paredes[15]):
            return 2
    elif sala==9:
        if player_paradoD.x > paredes[12].x + paredes[12].width/3 - player_paradoD.width/1.5 and player_paradoD.collided(paredes[12]):
            return 1
        if player_paradoD.x < paredes[11].x + paredes[11].width/1.5 - player_paradoD.width/3 and player_paradoD.collided(paredes[11]):
            return 2
    elif sala==10:
        if player_paradoD.x > paredes[14].x + paredes[14].width/3 - player_paradoD.width/1.5 and player_paradoD.collided(paredes[14]):
            return 1
        if player_paradoD.x < paredes[13].x + paredes[13].width/1.5 - player_paradoD.width/3 and player_paradoD.collided(paredes[13]):
            return 2
    elif sala==11:
        if player_paradoD.x > paredes[18].x + paredes[18].width/3 - player_paradoD.width/1.5 and player_paradoD.collided(paredes[18]):
            return 1
        if player_paradoD.x < paredes[17].x + paredes[17].width/1.5 - player_paradoD.width/3 and player_paradoD.collided(paredes[17]):
            return 2

    return 0

'''
def bate():
    global player_ataques_cooldown
    
    if player_orientation=="D":
        if len(ataque_player) == 0 and player_ataques_cooldown<0:
            player_ataques_cooldown = 160 * janela.delta_time()
            ataque_player.append(Sprite("ataque_dir.png",4))
            ataque_player[0].set_sequence_time(0,4,60,True)
    elif player_orientation == "E":
        if len(ataque_player) == 0 and player_ataques_cooldown < 0:
            player_ataques_cooldown = 160 * janela.delta_time()
            ataque_player.append(Sprite("ataque_esq.png", 4))
            ataque_player[0].set_sequence_time(0, 4, 60, True)

        #ataque_player[0].play()
    if len(ataque_player) > 0:
        if len(inimigos)>0 and ataque_player[0].get_curr_frame() >=2 and ataque_player[0].collided(inimigos[0]):
            del inimigos[0]

        if ataque_player[0].get_curr_frame() < 4: #enquanto a animção nao tiver acabado, ela toca até acabar
            ataque_player[0].y = player_paradoD.y
            ataque_player[0].draw()
            ataque_player[0].update()
            if player_orientation=="D":
                ataque_player[0].x = player_paradoD.x + player_paradoD.width
            else:
                ataque_player[0].x = player_paradoD.x - player_paradoD.width

            if ataque_player[0].get_curr_frame() == 3:  #Se está no ultimo frame, manda o ataque pra longe, pra evitar colisao
                ataque_player[0].draw()
                ataque_player[0].set_curr_frame(0)
                ataque_player[0].pause()
                del ataque_player[0]
'''


def bate():
    global player_ataques_cooldown
    global player_animation
    global conta_hit
    global boss2_hp

    if player_atacando.get_curr_frame() == 0:
        sword_snd.play()
        sword_snd.set_volume(10)
    if player_ataques_cooldown < 0:
        player_ataques_cooldown = 160 * janela.delta_time()
    player_animation = "batendo"

    if sala == 7:
        if conta_hit and 5 > player_atacando.get_curr_frame() > 2 and player_atacando.collided(boss2) and boss2_hp>0:
            boss2_hp-=1
            conta_hit = False
            hit_effect.x = boss2.x + hit_effect.width/3
            hit_effect.y = boss2.y

    elif len(inimigos) > 0:
        for i in range(len(inimigos)):
            if conta_hit and 5 > player_atacando.get_curr_frame() > 2 and player_atacando.collided(inimigos[i]) and inimigos_hp[i]>0:
                #del inimigos[0]
                conta_hit=False
                inimigos_hp[i]-=1
                hit_effect.x=inimigos[i].x
                hit_effect.y=inimigos[i].y



    if player_atacando.get_curr_frame() == 8:
        player_atacando.set_curr_frame(0)
        player_atacando.pause()
        player_atacandoE.set_curr_frame(0)
        player_atacandoE.pause()
        player_animation="parado"

def toma_dano():
    global player_hp
    global invencibilidade_cooldown
    global hurt_ui_delay
    if invencibilidade_cooldown<0:
        player_hp-=1
        invencibilidade_cooldown = 1
        barra_vida.update()
        hurt_ui_delay=0.7  #1.5
        hurt_ui.set_curr_frame(0)
        hit_snd.play()

def draw_inimigo_animation(state,id):
    if state == "paradoD":
        inimigos[id].update()
        inimigos[id].draw()
    elif state == "paradoE":
        inimigosE[id].update()
        inimigosE[id].draw()
    elif state == "andandoD":
        inimigos_andandoD[id].update()
        inimigos_andandoD[id].draw()
    elif state == "andandoE":
        inimigos_andandoE[id].update()
        inimigos_andandoE[id].draw()
    elif state == "batendoD":
        inimigos_atacandoD[id].update()
        inimigos_atacandoD[id].draw()
    elif state == "batendoE":
        inimigos_atacandoE[id].update()
        inimigos_atacandoE[id].draw()
    elif state == "parryE":
        if inimigos_parryE[id].get_curr_frame()<5:
            inimigos_parryE[id].update()
        inimigos_parryE[id].draw()
    elif state == "parryD":
        if inimigos_parryD[id].get_curr_frame() < 5:
            inimigos_parryD[id].update()
        inimigos_parryD[id].draw()

def atualiza_inimigo():
    global sala
    global inimigo_animation
    global player_animation
    global player_hp
    global invencibilidade_cooldown
    global parry_cooldown
    global atk_snd_delay
    atk_snd_delay-=janela.delta_time()
    if sala==0:
        inimigos_parryD[0].x = inimigos_parryE[0].x = inimigos_atacandoE[0].x = inimigos_atacandoD[0].x = inimigos_andandoD[0].x = inimigos_andandoE[0].x = inimigosE[0].x = inimigos[0].x
        inimigos_parryD[0].y = inimigos_parryE[0].y = inimigos_atacandoE[0].y = inimigos_atacandoD[0].y = inimigos_andandoD[0].y = inimigos_andandoE[0].y = inimigosE[0].y = inimigos[0].y
        if inimigos_hp[0] > 0:
            if atk_snd_delay<0 and (inimigo_animation[0] == "batendoD" or inimigo_animation[0] == "batendoE") and (inimigos_atacandoE[0].get_curr_frame() == 10 or inimigos_atacandoD[0].get_curr_frame() == 10):
                fire_snd.play()
                fire_snd.set_volume(10)
                atk_snd_delay=1
            if (inimigo_animation[0]=="batendoD" or inimigo_animation[0]=="batendoE") and inimigos_atacandoE[0].collided(player_hitbox) and (10<=inimigos_atacandoE[0].get_curr_frame()<=14 or 10<=inimigos_atacandoD[0].get_curr_frame()<=14):
                if player_animation=="parry":
                    parry_cooldown = 0.5
                    inimigos_parry_delay[0] = 1.5
                    inimigos_atacandoD[0].set_curr_frame(0)
                    inimigos_atacandoE[0].set_curr_frame(0)
                    parry_snd.play()
                else:
                    parry_cooldown = 0.1
                    toma_dano()
            if inimigos_parry_delay[0]>0:
                if inimigo_orientation[0] == "D":
                    inimigo_animation[0] = "parryD"
                else:
                    inimigo_animation[0] = "parryE"
                inimigos_parry_delay[0]-=janela.delta_time()
                inimigos_pode_mover[0]=False
            else:
                inimigos_parryD[0].set_curr_frame(0)
                inimigos_parryE[0].set_curr_frame(0)

            if inimigos_hp[0]==0:
                explosao.x = inimigos[0].x
                explosao.y = inimigos[0].y
                inimigos_hp[0]-=1


    elif sala==2:
        i=4
        inimigos_parryD[i].x = inimigos_parryE[i].x = inimigos_atacandoE[i].x = inimigos_atacandoD[i].x = inimigos_andandoD[i].x = inimigos_andandoE[i].x = inimigosE[i].x = inimigos[i].x
        inimigos_parryD[i].y = inimigos_parryE[i].y = inimigos_atacandoE[i].y = inimigos_atacandoD[i].y = inimigos_andandoD[i].y = inimigos_andandoE[i].y = inimigosE[i].y = inimigos[i].y
        if inimigos_hp[i] > 0:
            if atk_snd_delay<0 and (inimigo_animation[i] == "batendoD" or inimigo_animation[i] == "batendoE") and (inimigos_atacandoE[i].get_curr_frame() == 10 or inimigos_atacandoD[i].get_curr_frame() == 10):
                fire_snd.play()
                fire_snd.set_volume(10)
                atk_snd_delay=1
            if (inimigo_animation[i] == "batendoD" or inimigo_animation[i] == "batendoE") and inimigos_atacandoE[i].collided(player_hitbox) and (10 <= inimigos_atacandoE[i].get_curr_frame() <= 14 or 10 <= inimigos_atacandoD[i].get_curr_frame() <= 14):
                if player_animation == "parry":
                    parry_cooldown = 0.5
                    inimigos_parry_delay[i] = 1.5
                    inimigos_atacandoD[i].set_curr_frame(0)
                    inimigos_atacandoE[i].set_curr_frame(0)
                    parry_snd.play()
                else:
                    parry_cooldown = 0.1
                    toma_dano()
            if inimigos_parry_delay[i] > 0:
                if inimigo_orientation[i] == "D":
                    inimigo_animation[i] = "parryD"
                else:
                    inimigo_animation[i] = "parryE"
                inimigos_parry_delay[i] -= janela.delta_time()
                inimigos_pode_mover[i] = False
            else:
                inimigos_parryD[i].set_curr_frame(0)
                inimigos_parryE[i].set_curr_frame(0)

            if inimigos_hp[i] == 0:
                explosao.x = inimigos[i].x
                explosao.y = inimigos[i].y
                inimigos_hp[i] -= 1


    elif sala==5:
        i=5
        inimigos_parryD[i].x = inimigos_parryE[i].x = inimigos_atacandoE[i].x = inimigos_atacandoD[i].x = inimigos_andandoD[i].x = inimigos_andandoE[i].x = inimigosE[i].x = inimigos[i].x
        inimigos_parryD[i].y = inimigos_parryE[i].y = inimigos_atacandoE[i].y = inimigos_atacandoD[i].y = inimigos_andandoD[i].y = inimigos_andandoE[i].y = inimigosE[i].y = inimigos[i].y
        if inimigos_hp[i] > 0:
            if atk_snd_delay<0 and (inimigo_animation[i] == "batendoD" or inimigo_animation[i] == "batendoE") and (inimigos_atacandoE[i].get_curr_frame() == 10 or inimigos_atacandoD[i].get_curr_frame() == 10):
                fire_snd.play()
                fire_snd.set_volume(10)
                atk_snd_delay=1
            if (inimigo_animation[i] == "batendoD" or inimigo_animation[i] == "batendoE") and inimigos_atacandoE[i].collided(player_hitbox) and (10 <= inimigos_atacandoE[i].get_curr_frame() <= 14 or 10 <= inimigos_atacandoD[i].get_curr_frame() <= 14):
                if player_animation == "parry":
                    parry_cooldown = 0.5
                    inimigos_parry_delay[i] = 1.5
                    inimigos_atacandoD[i].set_curr_frame(0)
                    inimigos_atacandoE[i].set_curr_frame(0)
                    parry_snd.play()
                else:
                    parry_cooldown = 0.1
                    toma_dano()
            if inimigos_parry_delay[i] > 0:
                if inimigo_orientation[i] == "D":
                    inimigo_animation[i] = "parryD"
                else:
                    inimigo_animation[i] = "parryE"
                inimigos_parry_delay[i] -= janela.delta_time()
                inimigos_pode_mover[i] = False
            else:
                inimigos_parryD[i].set_curr_frame(0)
                inimigos_parryE[i].set_curr_frame(0)

            if inimigos_hp[i] == 0:
                explosao.x = inimigos[i].x
                explosao.y = inimigos[i].y
                inimigos_hp[i] -= 1


    elif sala==6:
        for i in range(1,4):
            if inimigos_hp[i]>0:
                #if -janela.width/2<inimigos[i].x<janela.width*1.5:
                inimigos_parryD[i].x = inimigos_parryE[i].x = inimigos_atacandoE[i].x = inimigos_atacandoD[i].x = inimigos_andandoD[i].x = inimigos_andandoE[i].x = inimigosE[i].x = inimigos[i].x
                inimigos_parryD[i].y = inimigos_parryE[i].y = inimigos_atacandoE[i].y = inimigos_atacandoD[i].y = inimigos_andandoD[i].y = inimigos_andandoE[i].y = inimigosE[i].y = inimigos[i].y
                if atk_snd_delay < 0 and (inimigo_animation[i] == "batendoD" or inimigo_animation[i] == "batendoE") and (inimigos_atacandoE[i].get_curr_frame() == 10 or inimigos_atacandoD[i].get_curr_frame() == 10):
                    fire_snd.play()
                    fire_snd.set_volume(10)
                    atk_snd_delay = 1
                if (inimigo_animation[i] == "batendoD" or inimigo_animation[i] == "batendoE") and inimigos_atacandoE[i].collided(player_hitbox) and (10 <= inimigos_atacandoE[i].get_curr_frame() <= 14 or 10 <= inimigos_atacandoD[i].get_curr_frame() <= 14):
                    if player_animation == "parry":
                        parry_cooldown = 0.5
                        inimigos_parry_delay[i] = 1.5
                        inimigos_atacandoD[i].set_curr_frame(0)
                        inimigos_atacandoE[i].set_curr_frame(0)
                        parry_snd.play()
                    else:
                        parry_cooldown = 0.1
                        toma_dano()
                    fire_snd.play()
                if inimigos_parry_delay[i] > 0:
                    if inimigo_orientation[i] == "D":
                        inimigo_animation[i] = "parryD"
                    else:
                        inimigo_animation[i] = "parryE"
                    inimigos_parry_delay[i] -= janela.delta_time()
                    inimigos_pode_mover[i] = False
                else:
                    inimigos_parryD[i].set_curr_frame(0)
                    inimigos_parryE[i].set_curr_frame(0)

                if inimigos_hp[i] == 0:
                    explosao.x = inimigos[i].x
                    explosao.y = inimigos[i].y
                    inimigos_hp[i] -= 1


'''
def inimigo_ataque(inimigo):
    global inimigos_ataques_cooldown
    global player_hp
    if len(inimigos_ataques) == 0 and inimigos_ataques_cooldown < 0:
        inimigos_ataques_cooldown = 800 * janela.delta_time()

        ataque_inimigo = Sprite("ataque_dir.png",4)
        ataque_inimigo.set_sequence_time(0,4,60,True)
        inimigos_ataques.append(ataque_inimigo)
        inimigos_ataques[len(inimigos_ataques)-1].y = inimigo.y
    if len(inimigos_ataques)>0:
        if inimigos_ataques[len(inimigos_ataques) - 1].collided(player_paradoD):
            player_hp-=1
        if inimigos_ataques[len(inimigos_ataques) - 1].get_curr_frame() < 4: #enquanto a animção nao tiver acabado, ela toca até acabar
            inimigos_ataques[len(inimigos_ataques) - 1].draw()
            inimigos_ataques[len(inimigos_ataques) - 1].update()
            if distancia[i] < 0:
                inimigos_ataques[len(inimigos_ataques) - 1].x = inimigo.x + inimigo.width
            else:
                inimigos_ataques[len(inimigos_ataques) - 1].x = inimigo.x
            if inimigos_ataques[len(inimigos_ataques) - 1].get_curr_frame() == 3:
                inimigos_ataques[len(inimigos_ataques) - 1].draw()
                inimigos_ataques[len(inimigos_ataques) - 1].set_curr_frame(0)
                inimigos_ataques[len(inimigos_ataques) - 1].pause()
                del inimigos_ataques[len(inimigos_ataques) - 1]
'''


def draw_player_animation(state):
    global player_orientation
    global player_vely
    global pulando
    if state == "paradoD":
        player_paradoD.update()
        player_paradoD.draw()
    elif state == "paradoE":
        player_paradoE.update()
        player_paradoE.draw()
    elif state == "andandoD":
        player_andandoD.update()
        player_andandoE.update()
        if player_orientation == "D":
            player_andandoD.draw()
        else:
            player_andandoE.draw()
    elif state == "batendo":
        player_atacando.update()
        player_atacandoE.update()
        if player_orientation == "D":
            player_atacando.draw()
        else:
            player_atacandoE.draw()
    elif state == "parry":
        if player_orientation=="D":
            player_parry.draw()
        else:
            player_parryE.draw()
    elif state == "pulando":
        player_pulando.update()
        player_pulandoE.update()
        if player_orientation=="D":
            player_pulando.draw()
        else:
            player_pulandoE.draw()

        if -100<player_vely<100 and pulando==1:
            player_pulando.set_curr_frame(3)
            player_pulandoE.set_curr_frame(3)
        elif player_vely<0 and pulando==1:
            player_pulando.set_curr_frame(1)
            player_pulandoE.set_curr_frame(1)
        elif player_vely>0:
            if player_pulando.get_curr_frame()>=5:
                player_pulando.update()
                player_pulandoE.update()
            elif 1<=player_pulando.get_curr_frame()<=4:
                player_pulando.set_curr_frame(5)
                player_pulandoE.set_curr_frame(5)





def mudar_sala(room):
    global sala
    buracos[0].y = -janela.height / 2
    for plat in plats:
        plat.y=-1000
    for i in range(len(inimigos)):
        inimigos_hp[i]=0
    for i in range(len(blipR1)):
        blipR1[i].y=-1000
        blipR2[i].y=-1000
    for porta in portas:
        porta.y=-1000
    for parede in paredes:
        parede.y=-1000
    for col in colisores_parede:
        col.y=-1000
    for buraco in buracos:
        buraco.y=-1000
    mesa.y=-1000
    tank3.y=-1000
    tank2.y=-1000
    maq_tempo.y=-1000
    corpo.y=-1000
    calendario.y= -1000

    if room==1:
        maq_tempo.y = janela.height - maq_tempo.height * 1.23
        Cenario.y = -janela.height
        portas[0].y = -janela.height / 2
        portas[1].y = janela.height/2 - portas[1].height/20
        portas[2].y = -janela.height / 2
        paredes[1].y = 0
        paredes[2].y = 0
        tank3.y = janela.height - tank.height * 1.25
        tank2.y = janela.height - tank.height * 1.25
        calendario.y = tank3.y + calendario.height*3
    elif room==0:
        inimigos_hp[0] = 5
        inimigos[0].y = janela.height / 1.4 + 10 + player_paradoD.height - inimigos[0].height
        inimigos[0].x = janela.width * 0.8
        portas[0].y = janela.height/2 - portas[0].height/20
        portas[2].y = janela.height / 2 + portas[0].height / 10
        Cenario.y = 0
        paredes[0].y = 0
        paredes[3].y = 0
        paredes[1].y = 1000
        paredes[2].y = 1000
        tank3.y = -janela.height * 1.8
        tank2.y = -janela.height * 1.8


    elif room==2:
        buracos[0].y = janela.height - buracos[0].height
        portas[4].y =janela.height / 2 - portas[0].height / 20
        portas[3].y = portas[6].y = janela.height / 2 + portas[0].height / 10
        Cenario.y = 0
        paredes[5].y = 0
        paredes[4].y = 0
        paredes[1].y = 1000
        paredes[2].y = 1000
        tank.y = -janela.height * 1.8
        tank2.y = -janela.height * 1.8
        plats[36].y = plats[37].y = janela.height / 2 + plats[0].height*2.3
        plats[38].y = plats[37].y - plats[0].height*4.2
        warp[0].y=-warp[0].height/2
        inimigos_hp[4]=5
        inimigos[4].x= portas[4].x + portas[4].width*4
        inimigos[4].y= janela.height / 1.4 + 10 + player_paradoD.height - inimigos[0].height

    elif room==3:

        Cenario.y = -janela.height
        paredes[4].y = paredes[10].y = 0
        warp[1].y = janela.height - warp[1].height/2
        corpo.y= janela.height - corpo.height*1.5

    elif room == 5:
        Cenario.y = -janela.height
        paredes[1].y = 0
        paredes[2].y = 0
        portas[5].y = janela.height / 2 + portas[0].height / 10
        mesa.y = janela.height - mesa.height*1.5
        inimigos_hp[5] = 5
        inimigos[5].x = mesa.x - inimigos[5].width
        inimigos[5].y = janela.height / 1.4 + 10 + player_paradoD.height - inimigos[0].height

    elif room == 6:
        for porta in portas:
            porta.y = 1000
        portas[7].y = janela.height - portas[7].height
        portas[8].y = janela.height - portas[7].height/2
        Cenario.y = -janela.height * 4.65
        for i in range(6):
            paredes[i].y=1000
        paredes[6].y = janela.height/2
        paredes[8].y = janela.height/2
        tank.y = -janela.height * 1.8
        tank2.y = -janela.height * 1.8
        buracos[1].y = buracos[2].y = buracos[3].y = buracos[4].y = buracos[5].y = buracos[6].y = buracos[7].y = buracos[8].y=  janela.height * 1.2
        plats[1].y = plats[2].y = janela.height
        plats[3].y = plats[4].y = plats[5].y = plats[6].y = janela.height * 1.135
        for i in range(12,34):
            plats[i].y = janela.height * 1.135
        #plats[13].y = plats[14].y = plats[15].y = plats[16].y = janela.height/1.8
        plats[18].y = janela.height/2.4
        plats[23].y = plats[29].y = janela.height * 0.94
        #plats[7].y = janela.height/1.8
        plats[8].y = plats[9].y = plats[10].y = janela.height/1.54
        colisores_parede[0].y = janela.height * 1 #perfeito
        colisores_parede[1].y = janela.height * 0.9
        colisores_parede[2].y = janela.height * 0.7
        colisores_parede[3].y = janela.height * 0.7
        colisores_parede[4].y = janela.height * 0.9
        colisores_parede[5].y = janela.height * 1.1
        colisores_parede[6].y = colisores_parede[10].y = janela.height * 0.5
        colisores_parede[7].y = colisores_parede[11].y = janela.height * 0.7
        colisores_parede[8].y = colisores_parede[12].y = janela.height * 0.9
        colisores_parede[9].y = colisores_parede[13].y = janela.height * 1.1
        colisores_parede[25].y = janela.height * 0.48
        colisores_parede[14].y = janela.height * 0
        colisores_parede[15].y = janela.height * 0.2
        colisores_parede[16].y = janela.height * 0.4
        colisores_parede[17].y = colisores_parede[19].y = janela.height * 0.6
        colisores_parede[18].y = colisores_parede[20].y = janela.height * 0.8
        colisores_parede[21].y = colisores_parede[22].y = colisores_parede[23].y = colisores_parede[24].y = janela.height * 0.95
        blipR1[0].y = janela.height/1.3
        blipR2[0].y = janela.height/1.7
        blipR1[1].y = janela.height/1.6
        blipR2[1].y = janela.height/1.2
        blipR2[3].y = janela.height/1.2
        blipR1[2].y = janela.height / 1.0
        blipR2[2].y = janela.height / 1.4
        blipR1[3].y = janela.height / 1.6
        blipR1[4].y = janela.height / 2
        blipR2[4].y = janela.height / 1.5
        blipR1[5].y = janela.height / 1.2
        for i in range(1,4):
            inimigos_hp[i]=5
            inimigos[i].x= plats[18 + i*4].x
            inimigos[i].y= janela.height

    elif room == 7:
        for porta in portas:
            porta.y = -1000
        portas[9].y = janela.height * 0.4
        Cenario.y = -janela.height * 5.65
        for i in range(8):
            paredes[i].y = -1000
        paredes[6].y = janela.height/3
        paredes[9].y = janela.height
        tank.y = -janela.height * 1.8
        tank2.y = -janela.height * 1.8
        for buraco in buracos:
            buraco.y = -1000
        for i in range(34):
            plats[i].y = -1000
        plats[34].y = janela.height - plats[0].height * 3.5
        plats[35].y = plats[2].y = plats[3].y = plats[4].y = plats[5].y = plats[6].y = janela.height * 1.68
        for i in range(25):
            colisores_parede[i].y = -1000
        blipR2[8].y = blipR1[9].y = blipR2[9].y = janela.height
        blipR1[6].y = blipR2[6].y = blipR1[8].y = janela.height * 1.2
        blipR2[5].y = blipR1[7].y = blipR2[7].y = janela.height * 1.4
        colisores_parede[25].y = janela.height - plats[0].height * 3.4
        colisores_parede[26].y = janela.height + plats[0].height
        colisores_parede[27].y = janela.height + plats[0].height * 5
        colisores_parede[28].y = janela.height + plats[0].height * 9
        boss2.y = janela.height * 1.5
        boss2.x = janela.width

    elif room == 8:
        maq_tempo.y = janela.height - maq_tempo.height * 1.23
        Cenario.y = -janela.height*3 +2
        paredes[15].y = 0
        paredes[16].y = 0
        portas[1].y = janela.height / 2 - portas[0].height / 20

    elif room == 9:
        portas[0].y = janela.height / 2 - portas[0].height / 20
        portas[2].y = janela.height / 2 + portas[0].height / 10
        Cenario.y = -janela.height*2 +2
        paredes[11].y = 0
        paredes[12].y = 0

    elif room == 10:
        portas[3].y = janela.height / 2 + portas[0].height / 10
        portas[4].y = janela.height / 2 - portas[0].height / 20
        Cenario.y = -janela.height*2.42 -2
        paredes[13].y = 0
        paredes[14].y = 0

    elif room == 11:
        Cenario.y = -janela.height*3 +2
        paredes[17].y = 0
        paredes[18].y = 0
        portas[5].y = janela.height / 2 + portas[0].height / 10
        mesa.y = janela.height - mesa.height * 1.5

    sala=room

def fade_screen(s):
    global pode_mover
    global pode_interagir
    global fade_delay
    if fade_delay >= 0:
        if fade.get_curr_frame()<12:
            fade.update()
        elif fade_delay < s:
            fade_delay += janela.delta_time()
        elif fade.get_curr_frame()<24:
            fade.update()
        else:
            fade.set_curr_frame(1)
            fade_delay = -1
            pode_interagir=True
            pode_mover=True
        fade.draw()

def dialogo(texto):
    global mostrar_dialogo
    global text_dialogo
    mostrar_dialogo = True
    text_dialogo = texto

def dialogo_update(texto): #max_por_linha como parametro?
    global mostrar_dialogo
    global prox_dialogo
    global pode_mover
    pode_mover=False
    max_por_linha=41
    #mostrar_dialogo = True
    if prox_dialogo!=0:
        texto=prox_dialogo

    tamanho = len(texto)
    if tamanho < max_por_linha:
        l1=texto[0:]
        l2=""
        l3=""
        if (teclado_click("E")):
            for tampa in tampa_texto:
                tampa.x=janela.width/4
            mostrar_dialogo=False
            pode_mover = True
            prox_dialogo = 0
    elif tamanho < max_por_linha*2:
        l1=texto[0:max_por_linha] #+ "-"
        l2=texto[max_por_linha:]
        l3=""
        if (teclado_click("E")):
            for tampa in tampa_texto:
                tampa.x=janela.width/4
            mostrar_dialogo = False
            pode_mover = True
            prox_dialogo = 0
    elif tamanho < max_por_linha*3:
        l1 = texto[0:max_por_linha] #+ "-"
        l2 = texto[max_por_linha:max_por_linha*2] #+ "-"
        l3 = texto[max_por_linha*2:]
        if (teclado_click("E")):
            for tampa in tampa_texto:
                tampa.x=janela.width/4
            mostrar_dialogo = False
            pode_mover = True
            prox_dialogo=0
    else:
        l1 = texto[0:max_por_linha] #+ "-"
        l2 = texto[max_por_linha:max_por_linha*2] #+ "-"
        l3 = texto[max_por_linha*2:max_por_linha*3]
        if(teclado_click("E")):
            prox_dialogo=texto[max_por_linha*3:]
            for tampa in tampa_texto:
                tampa.x=janela.width/4

    #movendo os tampa textos
    if tampa_texto[0].x < janela.width * 0.88:
        tampa_texto[0].x += janela.delta_time() * 400
    elif tampa_texto[1].x < janela.width * 0.88:
        tampa_texto[1].x += janela.delta_time() * 400
    elif tampa_texto[2].x < janela.width * 0.88:
        tampa_texto[2].x += janela.delta_time() * 400
    #QUANDO AS CAIXAS PRETAS QUE BLOQUEAM O TEXTO ENCOSTARAM PARAREM DE SE MOVER, prox_dialogo=0, mostrar_dialogo=False

    janela.draw_text(l1,janela.width/4,janela.height/4.2,50,(255,255,255),font_name="Futura",bold=False,italic=False)
    janela.draw_text(l2,janela.width/4,janela.height/3.4,50,(255,255,255),font_name="Futura",bold=False,italic=False)
    janela.draw_text(l3,janela.width/4,janela.height/2.85,50,(255,255,255),font_name="Futura",bold=False,italic=False)

def respawn():
    global sala
    global invencibilidade_cooldown
    global player_hp
    global boss2_state
    global boss2_hp
    invencibilidade_cooldown = 3
    player_hp=5
    barra_vida.set_curr_frame(0)
    if sala == 0:
        player_paradoD.y = janela.height / 1.4 + 10
        if portas[0].x <= janela.width / 2:
            while (portas[0].x <= janela.width / 2):
                movimentoCameraH((-1))
        else:
            while (portas[0].x + portas[0].width / 2 >= janela.width / 2):
                movimentoCameraH(1)
    elif sala==2:
        player_paradoD.y = janela.height / 1.4 + 10
        if paredes[4].x <= 0:
            while(paredes[4].x <= 0):
                movimentoCameraH((-1))
        player_paradoD.x = paredes[4].x + paredes[6].width*1.1

    elif sala==6:
        player_paradoD.x = portas[0].width / 2
        player_paradoD.y = 0
        while (paredes[6].x < 0):
            movimentoCameraH((-1) * (player_velx * janela.delta_time()))
        while Cenario.y < -janela.height * 4.75:
            movimentoCameraV((-janela.delta_time()))
    if sala==7:
        player_paradoD.x = player_paradoD.width / 2
        player_paradoD.y = janela.height / 2
        while (paredes[6].x < -paredes[6].width/1.5):
            movimentoCameraH(-1)
        while (Cenario.y < -janela.height * 5.65):
            movimentoCameraV(-1)
        boss2_state="parado"
        boss2.x = janela.width
        boss2_hp = 35
        if bossfight[1]!=2:
            bossfight[1]=0
            paredes[6].x -= plats[0].width / 1.95


def atualiza_buraco():
    global caindo_buraco
    global tempo_fade
    global fade_delay
    global pode_interagir
    global pode_mover
    global camera_presaV
    global player_vely

    if sala==2:
        if player_paradoD.collided(buracos[0]) and caindo_buraco==False and (player_paradoD.x + player_paradoD.width/3 > buracos[0].x and player_paradoD.x + 2*player_paradoD.width/3 < buracos[0].x+buracos[0].width ):
            caindo_buraco=True
        if not(player_paradoD.collided(buracos[0])) and player_paradoD.y + player_paradoD.height < janela.height and not (player_paradoD.x + player_paradoD.width / 3 > buracos[0].x and player_paradoD.x + 2 * player_paradoD.width / 3 < buracos[0].x + buracos[0].width):
            caindo_buraco=False
    elif sala==6:
        for buraco in buracos:
            if player_paradoD.collided(buraco) and caindo_buraco == False and (player_paradoD.x + player_paradoD.width / 3 > buraco.x and player_paradoD.x + 2 * player_paradoD.width / 3 < buraco.x + buraco.width):
                caindo_buraco = True
            if player_paradoD.collided(buraco) or player_paradoD.y + player_paradoD.height * 1.3 > janela.height:
                camera_presaV = True

    if caindo_buraco and player_paradoD.y > janela.height:
        if fade_delay < 0:
            pode_mover = False
            pode_interagir = False
            tempo_fade = 0.5
            fade_delay = 0
        if fade_delay > 0 and caindo_buraco:
            respawn()
            player_paradoD.y = 0
            player_vely = 0
            caindo_buraco=False

def draw_boss(B):
    global boss2_state
    global sala
    global boss2_orientation
    if B==2:
        if boss2_orientation=="E":
            if boss2_state=="parado":
                boss2.draw()
                boss2.update()
            elif boss2_state=="ataque1":
                boss2_atkD.draw()
                boss2_atkD.update()
            elif boss2_state=="stun":
                boss2_stunD.draw()
                boss2_stunD.update()
                boss2_stunE.update()
                if boss2_stunD.get_curr_frame()>=15:
                    boss2_stunD.set_curr_frame(9)
                    boss2_stunE.set_curr_frame(9)
        else:
            if boss2_state=="parado":
                boss2E.draw()
                boss2E.update()
            elif boss2_state=="ataque1":
                boss2_atkE.draw()
                boss2_atkE.update()
            elif boss2_state=="stun":
                boss2_stunE.draw()
                boss2_stunE.update()
                boss2_stunD.update()
                if boss2_stunE.get_curr_frame()>=15:
                    boss2_stunE.set_curr_frame(9)
                    boss2_stunD.set_curr_frame(9)


def atualiza_boss(num):
    global boss2_state
    global boss2_atk_delay
    global boss2_inner_atk_delay
    global boss2_orientation
    global boss2_atk_count
    global num_dashs
    global rosto_dialogo_id
    delta = janela.delta_time()
    boss2_atk_delay -= delta
    boss2_inner_atk_delay -= delta
    cuidado.y = -1000


    if num == 2:
        boss2E.x,boss2E.y = boss2_atkE.x,boss2_atkE.y = boss2_stunE.x,boss2_stunE.y = boss2_stunD.x,boss2_stunD.y = boss2_atkD.x,boss2_atkD.y = boss2.x,boss2.y
        if boss2_state=="parado":
            if boss2.y + boss2.height > blipR1[9].y:
                boss2.y-= delta * 400
            if boss2.x > blipR1[6].x and boss2_orientation=="E": #1.2
                boss2.x -= delta * 500
            elif boss2.x < blipR1[8].x and boss2_orientation=="D":
                boss2.x += delta * 500
            elif boss2_atk_delay<0:
                num_dashs = random.randint(5, 8)
                boss2_state="ataque1"
        elif boss2_state=="stun":
            if boss2_atk_delay < 0:
                boss2_state="parado"
                boss2_atk_delay = 5
                boss2_stunD.set_curr_frame(0)
                boss2_stunE.set_curr_frame(0)
                if boss2_orientation == "E":
                    boss2_orientation = "D"
                else:
                    boss2_orientation = "E"
            elif boss2.y + boss2.height < plats[2].y and boss2_atk_delay<4.2:
                boss2.y+=2


        elif boss2_state=="ataque1" and boss2_atk_delay<0:
            if boss2_atk_count>=num_dashs :
                if boss2.x > plats[35].x and boss2_orientation=="E":  #2
                    boss2.x -= delta * 800
                    cuidado.y = boss2.y
                    if player_paradoD.y - boss2.height/2 < boss2.y < player_paradoD.y + player_paradoD.height * 0.8 and boss2.collided(player_paradoD):
                        toma_dano()
                elif boss2.x < paredes[9].x and boss2_orientation=="D":
                    boss2.x += delta * 800
                    cuidado.y = boss2.y
                    if player_paradoD.y - boss2.height/2 < boss2.y < player_paradoD.y + player_paradoD.height * 0.8 and boss2.collided(player_paradoD):
                        toma_dano()
                elif boss2_atk_delay < 0:
                    boss2_atk_delay = 5
                    boss2_state = "stun"
                    boss2_atk_count = 0
            else:
                if boss2_orientation=="E": #2.5
                    boss2.x -= delta * 1000
                    if boss2.x > janela.width:
                        cuidado.y = boss2.y
                    if boss2_atk_count>0 and player_paradoD.y - boss2.height/2 < boss2.y < player_paradoD.y + player_paradoD.height* 0.8 and boss2.collided(player_paradoD):
                        toma_dano()
                elif boss2_orientation=="D":
                    boss2.x += delta * 1000
                    if boss2.x + boss2.width/2 < 0:
                        cuidado.y = boss2.y
                    if boss2_atk_count>0 and player_paradoD.y - boss2.height/2 < boss2.y < player_paradoD.y + player_paradoD.height* 0.8 and boss2.collided(player_paradoD):
                        toma_dano()
                if boss2.x >= paredes[9].x + boss2.width*2.5:
                    boss2.y = blipR1[9].y - boss2.height + janela.height* (0.2 * random.randint(0,3))
                    boss2_orientation="E"
                    boss2_atk_count+=1
                elif boss2.x < paredes[6].x - boss2.width*1.5:
                    boss2.y = blipR1[9].y - boss2.height + janela.height* (0.2 * random.randint(0,3))#blipR1[9 - random.randint(0,2)].y - boss2.height
                    boss2_orientation = "D"
                    boss2_atk_count += 1

        if boss2_hp<=0:
            bossfight[1] = 2
            explosaoBoss.x = boss2.x + boss2.width/2 - explosaoBoss.width/2
            explosaoBoss.y = boss2.y + boss2.height/2 - explosaoBoss.height/2
            cuidado.x = -1000
            cuidado.y= -1000
            paredes[6].x -= plats[0].width / 1.95    #1.95
            rosto_dialogo_id=1
            dialogo("Finalmente, agora é só colocar isso na   máquina                                  *Você pega o nucleo do corpo*")
            chaves_obtidas[3]=1




def jogo():
    global invencibilidade_cooldown
    global parry_cooldown
    global parry_duration
    global caindo_buraco
    global rosto_dialogo_id
    global camera_presaV
    global camera_presaH
    global mostrar_dialogo
    global pode_mover
    global tempo_fade
    global pode_interagir
    global fade_delay
    global distancia
    global inimigo_animation
    global inimigo_orientation
    global player_hp
    global player_animation
    global player_orientation
    global player_vely
    global pulo_cooldown
    global coyoteCooldown
    global pulando
    global fall
    global player_ataques_cooldown
    global inimigos_ataques_cooldown
    global text_dialogo
    global conta_hit
    global ritmo_delay
    global comeca_jogo
    global porta_som_toca
    global em_interagivel
    global hurt_ui_delay
    global started
    global start_time
    global fim_de_jogo
    global acabou
    global fade2delay
    global musica_boss_tocando
    global step_snd_delay
    deltatempo = janela.delta_time()
    coyote = 40 * deltatempo  #nao é usado?
    #Sincronizando todas as animações do jogador em pilha
    player_pulandoE.x,player_pulandoE.y = player_pulando.x,player_pulando.y = player_parryE.x,player_parryE.y =player_parry.x,player_parry.y = player_paradoE.x,player_paradoE.y = player_paradoD.x,player_paradoD.y
    player_atacando.x, player_atacando.y = player_atacandoE.x, player_atacandoE.y = player_paradoD.x - player_paradoD.width/2,player_paradoD.y + player_paradoD.height - player_atacando.height
    player_atacandoE.x = player_paradoD.x - player_paradoD.width*1.7
    player_hitbox.x, player_hitbox.y = player_paradoD.x + player_paradoD.width/2 - player_hitbox.width/2, player_paradoD.y
    player_andandoD.x,player_andandoD.y = player_paradoD.x + player_paradoD.width/1.5 - player_andandoD.width, player_paradoD.y - 1
    player_andandoE.x, player_andandoE.y = player_paradoE.x + player_paradoD.width/4, player_paradoD.y - 1
    olho_interage.x, olho_interage.y = player_paradoD.x + player_paradoD.width/2 - olho_interage.width/2, player_paradoD.y - olho_interage.height*1.5
    invencibilidade_cooldown-=janela.delta_time()
    em_interagivel=False

    check_camera_state()
    acabou = 0
    if comeca_jogo==0:
        fim_de_jogo=0
        comeca_jogo=1
    if bossfight[1]!=1 and started and not fundo_snd.is_playing():
        fundo_snd.play()
        fundo_snd.set_volume(3)
    if bossfight[1]==1 and not musica_boss_tocando:
        boss_snd.play()
        boss_snd.set_volume(3)
        musica_boss_tocando=True
        fundo_snd.stop()
    if bossfight[1]==2 and musica_boss_tocando:
        boss_snd.stop()
        musica_boss_tocando=False


    if sala == 7:
        paredes[6].y = player_paradoD.y - paredes[6].height/2
        #trigger bossfight2
        if player_paradoD.x > blipR1[7].x and bossfight[1]==0:
            boss2.x,boss2.y = blipR1[9].x,blipR1[9].y - boss2.height + janela.height* (0.2 * random.randint(0,3))
            bossfight[1] = 1
            paredes[6].x += plats[0].width / 1.95



    fadeinstart.update()
    if not(started):
        if sala==0:
            tank3.set_curr_frame(0)
            player_paradoD.x = -100
            pode_mover=False
            pode_interagir=False
            mudar_sala(1)
            while tank3.x + tank3.width > janela.width/2:
                movimentoCameraH(1)
        elif start_time>=0:
            start_time-=deltatempo
            if start_time<3 and tank3.get_curr_frame()==0:
                tank3.set_curr_frame(1)
                brk_glass1.play()
            elif start_time<2 and tank3.get_curr_frame()==1:
                tank3.set_curr_frame(2)
                brk_glass2.play()
            elif start_time<=0 and tank3.get_curr_frame()==2:
                tank3.set_curr_frame(3)
                brk_glass3.play()
                gas_leak.play()
                smoke_effect.x, smoke_effect.y = tank3.x + tank3.width / 2 - smoke_effect.width / 2, tank3.y + tank3.height / 2 - smoke_effect.height / 2
                smoke_effect.update()

        else:
            smoke_effect.x,smoke_effect.y = tank3.x + tank3.width/2 - smoke_effect.width/2,tank3.y + tank3.height/2 - smoke_effect.height/2
            smoke_effect.update()
            if 5>smoke_effect.get_curr_frame()>3:
                player_paradoD.x = tank3.x + tank3.width/2
        if 1 < fadeinstart.get_curr_frame() < 6:
            start_time = 7
        if smoke_effect.get_curr_frame()==13:
            pode_mover = True
            pode_interagir = True
            started = True
            dialogo("...                                      Onde eu estou?...                                                                     ...                                    Apenas lembro de ter entrado numa      maquina do lugar que me contrataram e... Falando nisso, cadê todo mundo?                                                                                            *Percebe o calendário velho*              Ano 2950??? E isso que esse calendario  está bem largado                         Por quanto tempo dormi afinal??          *Ao levantar, você se apoia em um bastão  verde*                                    Hmm... Acho que vou ficar com isso, é   melhor garantir minha segurança com algo")

    #O que acontece quando jogador morre
    if player_hp<=0:
        if fade_delay < 0:
            pode_mover = False
            pode_interagir = False
            tempo_fade = 0.5
            fade_delay = 0
        if fade_delay > 0:
            respawn()
            player_hp=5

    #permite que o jogador de 1 de dano por animação de hit, em vez de 1 de dano por frame
    if player_atacando.get_curr_frame()==0:
        conta_hit=True

    if sala==0:
        inimigo_orientation[0]="E"

    if player_animation!="andandoD":
        player_andandoD.set_curr_frame(0)

    if player_orientation=="D":
        player_animation="paradoD"
    else:
        player_animation="paradoE"

    som_step=random.randint(0,1)
    step_snd_delay-=deltatempo
    if teclado.key_pressed("D"):
        if pode_mover:
            #Se esta encostando na parede  (1 -> indo p/direita, 2-> indo p/esquerda)
            player_animation = "andandoD"
            player_orientation="D"
            if (colide_parede() == 1):
                player_paradoD.x=player_paradoD.x #faz nada
            #Se não, ele andad
            else:
                if (player_paradoD.x + player_paradoD.width/2 > janela.width/2 + player_paradoD.width) and camera_presaH==False:
                    movimentoCameraH(player_velx * janela.delta_time())
                else:
                    player_paradoD.x += player_velx * janela.delta_time()
            if pulando==0 and step_snd_delay < 0:
                step_snd_delay = 0.5
                if som_step == 0:
                    step1.play()
                    step1.set_volume(8)
                else:
                    step2.play()
                    step2.set_volume(8)
    elif teclado.key_pressed("A"):
        if pode_mover:
            # Se esta encostando na parede
            player_animation = "andandoD"
            player_orientation = "E"
            if (colide_parede() == 2):
                player_paradoD.x = player_paradoD.x  # faz nada
            # Se não, ele anda
            else:
                if (player_paradoD.x + player_paradoD.width/2 < janela.width/2 - player_paradoD.width) and camera_presaH==False:
                    movimentoCameraH((-1) * (player_velx * janela.delta_time()))
                else:
                    player_paradoD.x -= player_velx * janela.delta_time()
            if pulando == 0 and step_snd_delay < 0:
                step_snd_delay = 0.5
                if som_step == 0:
                    step1.play()
                    step1.set_volume(5)
                else:
                    step2.play()
                    step2.set_volume(5)

    atualiza_buraco()

    #Gravidade
    if camera_presaV:
        player_paradoD.y += player_vely * 4 * deltatempo + (grav * 2 * (deltatempo ** 2)) /2
    else:
        movimentoCameraV(player_vely * 6 * deltatempo + (grav * 2 * (deltatempo ** 2)) / 2)
    player_vely += grav * deltatempo

    #comportamento das portas
    if mostrar_dialogo==False and (teclado_click("E") or fade_delay>0):
        tempo_fade = 0.5
        rosto_dialogo_id=0 #personagem default

        if sala == 0 and player_paradoD.collided(portas[0]) and pode_interagir==True:
            portas[0].update()
            pode_mover = False
            if fade_delay<0:
                fade_delay=0
            if fade_delay>0:
                mudar_sala(1)
                portas[0].set_curr_frame(0)
                pode_interagir=False
                porta_som_toca = False
            if not porta_som_toca:
                porta_snd.play()
                porta_som_toca = True
        elif sala == 1 and player_paradoD.collided(portas[1]) and pode_interagir==True:
            portas[1].update()
            pode_mover = False
            if fade_delay < 0:
                fade_delay = 0
            if fade_delay > 0:
                mudar_sala(0)
                portas[1].set_curr_frame(0)
                pode_interagir=False
                porta_som_toca = False
            if not porta_som_toca:
                porta_snd.play()
                porta_som_toca = True

        elif sala == 0 and player_paradoD.collided(portas[2]) and pode_interagir==True:
            pode_mover = False
            if fade_delay < 0:
                fade_delay = 0
            if fade_delay > 0:
                mudar_sala(2)
                player_paradoD.x=janela.width/8
                while (paredes[4].x >= -paredes[4].width/2):
                    movimentoCameraH((1) * (player_velx * janela.delta_time()))
                pode_interagir=False
                porta_som_toca = False
            if not porta_som_toca:
                porta_snd.play()
                porta_som_toca = True
        elif sala == 2 and player_paradoD.collided(portas[3]) and pode_interagir==True:
            pode_mover = False
            if fade_delay < 0:
                fade_delay = 0
            if fade_delay > 0:
                mudar_sala(0)
                player_paradoD.x=janela.width - player_paradoD.width*2.5
                while (paredes[0].x + paredes[0].width/1.5 <= janela.width):
                    movimentoCameraH((-1) * (player_velx * janela.delta_time()))
                pode_interagir=False
                porta_som_toca = False
            if not porta_som_toca:
                porta_snd.play()
                porta_som_toca = True
        elif sala == 2 and player_paradoD.collided(portas[4]) and pode_interagir==True:
            portas[4].update()
            pode_mover = False
            if fade_delay < 0:
                fade_delay = 0
            if fade_delay > 0:
                mudar_sala(5)
                portas[4].set_curr_frame(0)
                player_paradoD.x= player_paradoD.width*5
                while (paredes[1].x < 0):
                    movimentoCameraH(-1)
                pode_interagir=False
                porta_som_toca = False
            if not porta_som_toca:
                porta_snd.play()
                porta_som_toca = True
        elif sala == 5 and player_paradoD.collided(portas[5]) and pode_interagir==True:
            pode_mover = False
            if fade_delay < 0:
                fade_delay = 0
            if fade_delay > 0:
                mudar_sala(2)
                while (portas[4].x > janela.width/2 + portas[4].width/2):
                    movimentoCameraH(1)
                    player_paradoD.x = janela.width/2
                pode_interagir=False
                porta_som_toca = False
            if not porta_som_toca:
                porta_snd.play()
                porta_som_toca = True

        elif sala == 2 and player_paradoD.collided(portas[6]) and pode_interagir==True:
            if chaves_obtidas[2]==True:
                pode_mover = False
                if fade_delay < 0:
                    fade_delay = 0
                if fade_delay > 0:
                    mudar_sala(6)
                    player_paradoD.x = portas[0].width/4
                    player_paradoD.y = janela.height/2
                    while (paredes[6].x < 0):
                        movimentoCameraH((-1) * (player_velx * janela.delta_time()))
                    pode_interagir=False
                    porta_som_toca = False
                if not porta_som_toca:
                    porta_snd.play()
                    porta_som_toca = True
            else:
                dialogo("Parece que eu preciso de uma 'Chave       Vermelha'")
        elif sala==6 and player_paradoD.collided(portas[7]) and pode_interagir==True:
            portas[7].update()
            pode_mover = False
            if fade_delay < 0:
                fade_delay = 0
            if fade_delay > 0:
                mudar_sala(2)
                portas[7].set_curr_frame(0)
                player_paradoD.x = janela.width - player_paradoD.width*3
                player_paradoD.y = janela.height / 2
                while (paredes[5].x + paredes[5].width/1.5 > janela.width):
                    movimentoCameraH((1) * (player_velx * janela.delta_time()))
                pode_interagir = False
                porta_som_toca = False
            if not porta_som_toca:
                porta_snd.play()
                porta_som_toca = True
        elif sala==6 and player_paradoD.collided(portas[8]) and pode_interagir==True:
            portas[8].update()
            pode_mover = False
            if fade_delay < 0:
                fade_delay = 0
            if fade_delay > 0:
                mudar_sala(7)
                portas[8].set_curr_frame(0)
                player_paradoD.x = player_paradoD.width/2
                player_paradoD.y = janela.height / 2
                while (paredes[6].x < 0):
                    movimentoCameraH((-1) * (player_velx * janela.delta_time()))
                pode_interagir = False
                porta_som_toca = False
            if not porta_som_toca:
                porta_snd.play()
                porta_som_toca = True
        elif sala==7 and player_paradoD.collided(portas[9]) and pode_interagir==True:
            portas[9].update()
            pode_mover = False
            if fade_delay < 0:
                fade_delay = 0
            if fade_delay > 0:
                mudar_sala(6)
                portas[9].set_curr_frame(0)
                player_paradoD.x = janela.width - paredes[8].width/2
                player_paradoD.y = janela.height / 2
                while (paredes[8].x > janela.width - paredes[8].width/1.5):
                    movimentoCameraH((1) * (player_velx * janela.delta_time()))
                pode_interagir = False
                porta_som_toca = False
            if not porta_som_toca:
                porta_snd.play()
                porta_som_toca = True
        elif sala==8 and player_paradoD.collided(portas[1]) and pode_interagir==True:
            portas[1].update()
            pode_mover = False
            if fade_delay < 0:
                fade_delay = 0
            if fade_delay > 0:
                mudar_sala(9)
                portas[1].set_curr_frame(0)
                pode_interagir = False
                porta_som_toca = False
            if not porta_som_toca:
                porta_snd.play()
                porta_som_toca = True
        elif sala == 0 and player_paradoD.collided(portas[0]) and pode_interagir==True:
            portas[0].update()
            pode_mover = False
            if fade_delay<0:
                fade_delay=0
            if fade_delay>0:
                mudar_sala(8)
                portas[0].set_curr_frame(0)
                pode_interagir=False
                porta_som_toca = False
            if not porta_som_toca:
                porta_snd.play()
                porta_som_toca = True
        elif sala == 9 and player_paradoD.collided(portas[0]) and pode_interagir==True:
            portas[0].update()
            pode_mover = False
            if fade_delay<0:
                fade_delay=0
            if fade_delay>0:
                mudar_sala(8)
                portas[0].set_curr_frame(0)
                pode_interagir=False
                porta_som_toca = False
            if not porta_som_toca:
                porta_snd.play()
                porta_som_toca = True
        elif sala == 9 and player_paradoD.collided(portas[2]) and pode_interagir==True:
            if chaves_obtidas[1]==True:
                pode_mover = False
                if fade_delay < 0:
                    fade_delay = 0
                if fade_delay > 0:
                    mudar_sala(10)
                    player_paradoD.x=janela.width/8
                    while (paredes[4].x >= -paredes[4].width/2):
                        movimentoCameraH((1) * (player_velx * janela.delta_time()))
                    pode_interagir=False
                    porta_som_toca = False
                if not porta_som_toca:
                    porta_snd.play()
                    porta_som_toca = True
            else:
                dialogo("Parece que eu preciso de uma 'Chave       Amarela'")
        elif sala == 10 and player_paradoD.collided(portas[3]) and pode_interagir==True:
            pode_mover = False
            if fade_delay < 0:
                fade_delay = 0
            if fade_delay > 0:
                mudar_sala(9)
                player_paradoD.x=janela.width - player_paradoD.width*2.5
                while (paredes[0].x + paredes[0].width/1.5 <= janela.width):
                    movimentoCameraH((-1) * (player_velx * janela.delta_time()))
                pode_interagir=False
                porta_som_toca = False
            if not porta_som_toca:
                porta_snd.play()
                porta_som_toca = True
        elif sala == 10 and player_paradoD.collided(portas[4]) and pode_interagir==True:
            if chaves_obtidas[0]==True:
                portas[4].update()
                pode_mover = False
                if fade_delay < 0:
                    fade_delay = 0
                if fade_delay > 0:
                    mudar_sala(11)
                    portas[4].set_curr_frame(0)
                    player_paradoD.x= player_paradoD.width*5
                    while (paredes[1].x < 0):
                        movimentoCameraH(-1)
                    pode_interagir=False
                    porta_som_toca = False
                if not porta_som_toca:
                    porta_snd.play()
                    porta_som_toca = True
            else:
                dialogo("Parece que eu preciso de uma 'Chave       Verde'")

        elif sala == 11 and player_paradoD.collided(portas[5]) and pode_interagir==True:
            pode_mover = False
            if fade_delay < 0:
                fade_delay = 0
            if fade_delay > 0:
                mudar_sala(10)
                while (portas[4].x > janela.width/2 + portas[4].width/2):
                    movimentoCameraH(1)
                    player_paradoD.x = janela.width/2
                pode_interagir=False
                porta_som_toca = False
            if not porta_som_toca:
                porta_snd.play()
                porta_som_toca = True



        elif sala==1 and player_paradoD.collided(maq_tempo) and pode_interagir==True:
            if chaves_obtidas[3]==1:
                fadin2.update()
                pode_mover=False
            elif chaves_obtidas[0]==1:
                pode_mover = False
                if fade_delay < 0:
                    fade_delay = 0
                if fade_delay > 0:
                    mudar_sala(8)
                    pode_interagir = False
                    mesa.set_curr_frame(1)
                    if dialogos_lidos[0]==0:
                        dialogo("A maquina não me mandou para o tempo      certo...   Vou precisar de outra peça,  pelo visto")
                        dialogos_lidos[0]=1
            else:
                dialogo("Está escrito que é uma maquina temporal..É UMA MAQUINA DO TEMPO?!                                                           Nossa... Realmente estou no futuro                                                                                        Eu poderia usar isso para voltar, mas    parece estar faltando algo para funcionar")

        elif sala==8 and player_paradoD.collided(maq_tempo) and pode_interagir==True:
            pode_mover = False
            if fade_delay < 0:
                fade_delay = 0
            if fade_delay > 0:
                mudar_sala(1)
                pode_interagir = False
                mesa.set_curr_frame(0)


        if sala==1 and player_paradoD.collided(tank2) :
            #mostrar_dialogo = True
            #text_dialogo = "É uma espécie de máquina maluca futurista...Por que estão usando isso?"
            rosto_dialogo_id = 0
            #dialogo("É uma espécie de máquina maluca futurista...Por que estão usando isso?")
            dialogo("É uma máquina parecida da que eu saí, mas parece estar quebrada")
        elif sala==1 and player_paradoD.collided(tank3):
            rosto_dialogo_id = 0
            dialogo("Foi daqui que eu saí, ainda está frio")
        elif sala==5 and player_paradoD.collided(mesa):
            rosto_dialogo_id = 0
            if chaves_obtidas[0] == 1:
                dialogo("A mesa continua capenga, tive sorte do   bihete estar intacto")
            else:
                dialogo("Parece uma mesa bem acabada...           me pergunto se ainda tem algo nela                                                  *Você abre uma gaveta e acha anotações*                                                                                    'Os experimentos conseguiram escapar,   é urgente conseguirmos um núcleo estável para voltar no tempo e concertar isso'  'Droga, se o segundo filho não tivesse a roubado... eu avisei que era má ideia    experimentar em escalas tão grandes'     'Eu preciso conseguir construir outro, se não temos que arrumar um jeito de pegar de volta dele...'                          *Você obteve 'Chave Verde'  e             'Núcleo Instável' da gaveta*                                                   Essa peça deve fazer a maquina funcionar, mas acho que nao como devia...")
                chaves_obtidas[0] = 1
        elif sala==11 and player_paradoD.collided(mesa):
            rosto_dialogo_id = 0
            if chaves_obtidas[2]==1:
                rosto_dialogo_id = 1
                dialogo("A estrutura está bem sólida, realmente   é uma bela mesa!")
            else:
                dialogo("Tem uma nota na gaveta, que coincidência  *Você lê a nota*                                                                  'Em breve vamos começar os projetos, não poderia estar mais animado'                                                      'Nossos principais experimentos vão ser  os filhos da empresa,pelo o que disseram'                                          'Algo sobre animais mutantes fundidos,   muito interessante!'                                                             'Só me lembro de um que vai ser um       jacaré unido à um mosquito, estou animado para ver como vai ficar'                 Então é isso que a outra nota quis dizer com 'o segundo filho'?                   Devo tomar cuidado...                   *Você obteve 'Chave Vermelha' da gaveta *")
                chaves_obtidas[2]=1
        elif sala==3 and player_paradoD.collided(corpo):
            rosto_dialogo_id = 0
            if chaves_obtidas[1]==1:
                dialogo("Descanse em paz")
            else:
                dialogo("Meu Deus, finalmente achei alguém!       Ei, acorda, a gente tem que sair daqui                                              ...            ele está gelado          espera... será que é ele o autor daquela nota?                                    Pelo visto ele não vai mais precisar     disso                               *Você obteve 'Chave Amarela' do corpo*")
                chaves_obtidas[1]=1

    if sala==2 and player_paradoD.collided(warp[0]):
        pode_mover = False
        if fade_delay < 0:
            fade_delay = 0
            warp[0].y= player_paradoD.y
        if fade_delay > 0:
            mudar_sala(3)
            player_paradoD.y = janela.height / 2
            while (paredes[4].x + paredes[4].width < 0):
                movimentoCameraH(-1)
            player_paradoD.x = janela.width / 2
            pode_interagir = False
    elif sala==3 and player_paradoD.collided(warp[1]):
        pode_mover = False
        if fade_delay < 0:
            fade_delay = 0
        if fade_delay > 0:
            mudar_sala(2)
            player_paradoD.y = janela.height / 2
            while (warp[0].x > janela.width/2):
                movimentoCameraH(1)
            player_paradoD.x = janela.width / 2
            pode_interagir = False

    '''
    if player_paradoD.collided(portas[0]) and teclado_click("I"):
        dialogo("Woooooooooow uma porta! WOOOOOW Q PORTA LINDAAAAA WOOOOOOOOOOOOOOOOOOOW adoro portas! <3 obrigado porta!")
    if player_paradoD.collided(portas[1]) and teclado_click("I"):
        dialogo("Heh, é hora de voltar por essa porta, mal podia esperar para isso *freaky*")
        rosto_dialogo_id=1
    '''

    if teclado_click("L") or player_atacando.get_curr_frame()!=0:
        bate()

    player_ataques_cooldown -= 1 * deltatempo

    if teclado_click("K") and parry_cooldown<0:
        parry_cooldown=1.5
        parry_duration=0.3
    if parry_duration>0:
        player_animation="parry"
        parry_duration-=janela.delta_time()
    parry_cooldown-=janela.delta_time()


    if sala!=0 and sala!=1 and sala!=2 and sala!=5 and sala!=3 and sala!=8 and sala!=9 and sala!=10 and sala!=11: #camera sobe                                                                                                        #camera desce
        if (player_paradoD.y < janela.height/4 and player_vely * 4 * deltatempo + (grav * 2 * (deltatempo ** 2)) / 2 < 0) or (player_paradoD.y > janela.height / 1.8 and player_vely * 4 * deltatempo + (grav * 2 * (deltatempo ** 2)) / 2 > 0):
            camera_presaV=False
        else:
            camera_presaV=True
    else:
        camera_presaV=True
        if not caindo_buraco and player_paradoD.y > janela.height / 1.4 + 10:  # encostando no "Chão"
            player_paradoD.y = janela.height / 1.4 + 10
            pulando = 0
            fall = 0
            player_vely = 0
            pulo_cooldown -= deltatempo


    if sala == 6:
        for i in range(0,34):
            if plats[i].x > -plats[i].width and plats[i].x < janela.width:
                if player_paradoD.y + player_paradoD.height - 10 < plats[i].y and player_paradoD.collided(plats[i]):
                    player_paradoD.y = plats[i].y - player_paradoD.height
                    pulando = 0
                    fall = 0
                    player_vely=0
                    coyoteCooldown = milissegundos(50)
                    pulo_cooldown -= deltatempo
                elif player_paradoD.y < janela.height / 1.4 + 10 or caindo_buraco:
                    pulando = 1
                    coyoteCooldown -= deltatempo
                    #quando estiver no interv do coyote E nao tiver pulado ainda, pode pular
                    if coyoteCooldown > 0 and fall == 0:
                        pulando = 0
            if plats[i].x + plats[i].width>player_paradoD.x>plats[i].x and player_paradoD.y > buracos[4].y:
                player_paradoD.y = plats[i].y - player_paradoD.height*1.1
                player_vely=0
                while player_paradoD.y < janela.height/2:
                    movimentoCameraV(-1)

        for i in range(len(blipR1)):
            if blipR1[0].get_curr_frame() < 4:
                if blipR1[i].x > -blipR1[i].width and blipR1[i].x < janela.width:
                    if player_paradoD.y + player_paradoD.height - 10 < blipR1[i].y and player_paradoD.collided(blipR1[i]):
                        player_paradoD.y = blipR1[i].y - player_paradoD.height
                        pulando = 0
                        fall = 0
                        player_vely=0
                        coyoteCooldown = milissegundos(50)
                        pulo_cooldown -= deltatempo
            else:
                if blipR2[i].x > -blipR2[i].width and blipR2[i].x < janela.width:
                    if player_paradoD.y + player_paradoD.height - 10 < blipR2[i].y and player_paradoD.collided(blipR2[i]):
                        player_paradoD.y = blipR2[i].y - player_paradoD.height
                        pulando = 0
                        fall = 0
                        player_vely=0
                        coyoteCooldown = milissegundos(50)
                        pulo_cooldown -= deltatempo

    elif sala == 7:
        for i in range(1,7):
            if plats[i].x > -plats[i].width and plats[i].x < janela.width and plats[i].y>player_paradoD.y + player_paradoD.height*0.8:
                if player_paradoD.y + player_paradoD.height - 10 < plats[i].y and player_paradoD.collided(plats[i]):
                    player_paradoD.y = plats[i].y - player_paradoD.height
                    pulando = 0
                    fall = 0
                    player_vely=0
                    coyoteCooldown = milissegundos(50)
                    pulo_cooldown -= deltatempo
                elif player_paradoD.y < janela.height / 1.4 + 10 or caindo_buraco:
                    pulando = 1
                    coyoteCooldown -= deltatempo
                    #quando estiver no interv do coyote E nao tiver pulado ainda, pode pular
                    if coyoteCooldown > 0 and fall == 0:
                        pulando = 0
                #if player_paradoD.y ==

        for i in range(34,36):
            if plats[i].x > -plats[i].width and plats[i].x < janela.width:
                if player_paradoD.y + player_paradoD.height - 10 < plats[i].y and player_paradoD.collided(plats[i]):
                    player_paradoD.y = plats[i].y - player_paradoD.height
                    pulando = 0
                    fall = 0
                    player_vely=0
                    coyoteCooldown = milissegundos(50)
                    pulo_cooldown -= deltatempo
                elif player_paradoD.y < janela.height / 1.4 + 10 or caindo_buraco:
                    pulando = 1
                    coyoteCooldown -= deltatempo
                    #quando estiver no interv do coyote E nao tiver pulado ainda, pode pular
                    if coyoteCooldown > 0 and fall == 0:
                        pulando = 0
        for i in range(5,len(blipR1)):
            if blipR1[0].get_curr_frame() < 4:
                if blipR1[i].x > -blipR1[i].width and blipR1[i].x < janela.width:
                    if player_paradoD.y + player_paradoD.height - 10 < blipR1[i].y and player_paradoD.collided(blipR1[i]):
                        player_paradoD.y = blipR1[i].y - player_paradoD.height
                        pulando = 0
                        fall = 0
                        player_vely=0
                        coyoteCooldown = milissegundos(50)
                        pulo_cooldown -= deltatempo
            else:
                if blipR2[i].x > -blipR2[i].width and blipR2[i].x < janela.width:
                    if player_paradoD.y + player_paradoD.height - 10 < blipR2[i].y and player_paradoD.collided(blipR2[i]):
                        player_paradoD.y = blipR2[i].y - player_paradoD.height
                        pulando = 0
                        fall = 0
                        player_vely=0
                        coyoteCooldown = milissegundos(50)
                        pulo_cooldown -= deltatempo

        if player_paradoD.y + player_paradoD.height * 0.8 > plats[4].y:
            player_paradoD.y = plats[4].y - player_paradoD.height * 1.2
            while player_paradoD.y < janela.height/2:
                movimentoCameraV(-1)


    elif sala == 2:
        for i in range(36,39):
            if plats[i].x > -plats[i].width and plats[i].x < janela.width:
                if player_paradoD.y + player_paradoD.height - 10 < plats[i].y and player_paradoD.collided(plats[i]):
                    player_paradoD.y = plats[i].y - player_paradoD.height
                    pulando = 0
                    fall = 0
                    player_vely=0
                    coyoteCooldown = milissegundos(50)
                    pulo_cooldown -= deltatempo
                elif player_paradoD.y < janela.height / 1.4 + 10 or caindo_buraco:
                    pulando = 1
                    coyoteCooldown -= deltatempo
                    #quando estiver no interv do coyote E nao tiver pulado ainda, pode pular
                    if coyoteCooldown > 0 and fall == 0:
                        pulando = 0



    else:
        if player_paradoD.y < janela.height / 1.4 + 10 or caindo_buraco:
            pulando = 1
            coyoteCooldown -= deltatempo
            # quando estiver no interv do coyote E nao tiver pulado ainda, pode pular
            if coyoteCooldown > 0 and fall == 0:
                pulando = 0


    if teclado.key_pressed("SPACE"):
        if pulando==0 and pulo_cooldown<0 and pode_mover:
            player_vely = -300  #-300
            pulando=1
            fall=1
            pulo_cooldown = milissegundos(30)
            player_animation="pulando"
    elif fall==1 and player_vely < 0:
        player_vely=0
        fall=0

    if player_pulando.get_curr_frame()>0:
        player_animation = "pulando"
        if pulando==0 and player_pulando.get_curr_frame()<8:
            player_pulando.set_curr_frame(9)
            player_pulandoE.set_curr_frame(9)

    #desenhando o olho de interagir
    for porta in portas:
        if not em_interagivel and player_paradoD.collided(porta):
            em_interagivel=True
    if player_paradoD.collided(tank) or player_paradoD.collided(tank2) or player_paradoD.collided(mesa) or player_paradoD.collided(maq_tempo):
        em_interagivel=True


    # inimigo se move em direção ao jogador e para em sua frente
    if sala==0 or sala==6 or sala==2 or sala==5:
        distancia=[0]*len(inimigos)
        for i in range(len(inimigos)):
            distancia[i] = inimigos[i].x + inimigos[i].width / 2 - (player_paradoD.x + player_paradoD.width / 2)
            #   visao_inimigo  > ditancia > limite de seu mov
            if janela.width / 2.5 > distancia[i] > player_paradoD.width * 1.5 and inimigos_pode_mover[i] and not(colisores_parede[24].x +colisores_parede[0].width*1.5>inimigos[i].x>colisores_parede[24].x -colisores_parede[0].width*0.5) and not(colisores_parede[22].x +colisores_parede[0].width*1.5>inimigos[i].x>colisores_parede[22].x -colisores_parede[0].width*0.5):  # distancia[i] < janela.width/4 and distancia[i] > 0  #visao do inim é o janela.widith/N
                inimigos[i].x -= inimigo_velx * deltatempo
                inimigo_animation[i]="andandoE"
                inimigo_orientation[i]="E"
            elif -janela.width / 2.5 < distancia[i] < -player_paradoD.width * 1.5 and inimigos_pode_mover[i] and not(colisores_parede[21].x +colisores_parede[0].width*1.5>inimigos[i].x + inimigos[i].width>colisores_parede[21].x -colisores_parede[0].width*0.5) and not(colisores_parede[23].x +colisores_parede[0].width*1.5>inimigos[i].x+ inimigos[i].width>colisores_parede[23].x -colisores_parede[0].width*0.5):
                inimigos[i].x += inimigo_velx * deltatempo
                inimigo_animation[i] = "andandoD"
                inimigo_orientation[i] = "D"
            # Se estiver close_range do player_paradoD, ataca
            elif inimigos[i].x > player_paradoD.x and distancia[i] < janela.width / 2.5 and not(colisores_parede[24].x +colisores_parede[0].width*1.5>inimigos[i].x>colisores_parede[24].x -colisores_parede[0].width*0.5) and not(colisores_parede[22].x +colisores_parede[0].width*1.5>inimigos[i].x>colisores_parede[22].x -colisores_parede[0].width*0.5):
                #inimigo_ataque(inimigo)
                inimigo_orientation[i] = "E"
                inimigo_animation[i]="batendoE"
                inimigos_pode_mover[i] = False
            elif inimigos[i].x < player_paradoD.x and -distancia[i] < janela.width / 2.5 and not(colisores_parede[21].x +colisores_parede[0].width*1.5>inimigos[i].x + inimigos[i].width>colisores_parede[21].x -colisores_parede[0].width*0.5) and not(colisores_parede[23].x +colisores_parede[0].width*1.5>inimigos[i].x+ inimigos[i].width>colisores_parede[23].x -colisores_parede[0].width*0.5):
                inimigo_orientation[i] = "D"
                inimigo_animation[i]="batendoD"
                inimigos_pode_mover[i]=False
            elif inimigo_orientation[i] == "D":
                inimigo_animation[i] = "paradoD"
            else:
                inimigo_animation[i] = "paradoE"

            if inimigos_atacandoD[i].get_curr_frame()!=0:
                inimigo_orientation[i] = "D"
                inimigo_animation[i] = "batendoD"
                inimigos_pode_mover[i] = False
            elif inimigos_atacandoE[i].get_curr_frame()!=0:
                inimigo_orientation[i] = "E"
                inimigo_animation[i] = "batendoE"
                inimigos_pode_mover[i] = False
            else:
                inimigos_atacandoD[i].set_curr_frame(0)
                inimigos_atacandoE[i].set_curr_frame(0)
                inimigos_pode_mover[i] = True


    atualiza_inimigo()
    #inimigos_ataques_cooldown -= 1 * deltatempo

    # atualiza os blipsR1 e R2
    if ritmo_delay <= 0:
        for blips in blipR1:
            blips.update()
        for blips in blipR2:
            blips.update()
        ritmo_delay = 1
    else:
        ritmo_delay -= janela.delta_time()


    if fim_de_jogo==0:
        #Desenhando e atualizando
        #porta.update()
        Cenario.draw()
        for buraco in buracos:
            buraco.draw()
        for i in range(len(paredes)):
            if i!=6 and i!=8 and i!=9:
                paredes[i].draw()
        for i in range(len(portas)):
            if i!=8 and i!=9 and i!=7:
                portas[i].draw()
        mesa.draw()
        for i in range(len(inimigos)):
            if inimigos_hp[i]>0:
                draw_inimigo_animation(inimigo_animation[i],i)

        if hit_effect.x > 0:
            hit_effect.draw()
            hit_effect.update()
        if hit_effect.get_curr_frame()>=3:
            hit_effect.x=-10000
        if explosao.x > 0:
            explosao.draw()
            explosao.update()
        if explosao.get_curr_frame()>=6:
            explosao.x=-10000
        if explosaoBoss.x > 0:
            explosaoBoss.draw()
            explosaoBoss.update()
        if explosaoBoss.get_curr_frame()>=6:
            explosaoBoss.x=-10000


        for w in warp:
            w.draw()
        corpo.draw()
        tank3.draw()
        tank2.draw()
        calendario.draw()
        maq_tempo.draw()
        for blips in blipR1:
            blips.draw()
        for blips in blipR2:
            blips.draw()
        #player_paradoD.draw()
        draw_player_animation(player_animation)
        if em_interagivel:
            olho_interage.draw()
        for plat in plats:
            plat.draw()

        if bossfight[1]==1:
            atualiza_boss(2)
            draw_boss(2)

        barra_vida.draw()
        for colisores in colisores_parede:
            colisores.draw()
        cuidado.draw()
        if not started and smoke_effect.get_curr_frame()!=0:
            smoke_effect.draw()
        fadeinstart.draw()

        hurt_ui_delay-=deltatempo
        if hurt_ui_delay>0:
            hurt_ui.draw()
            hurt_ui.update()

        fade2delay-=deltatempo
        if fadin2.get_curr_frame()!=0:
            fadin2.draw()
            fadin2.update()
        if fadin2.get_curr_frame()==22:
            fade2delay=2
        elif fadin2.get_curr_frame()>=23 and fade2delay<0:
            fim_de_jogo = 1
            fadout2.update()


        '''
        # Jogado bate (antigo)
        if teclado_click("L") or len(ataque_player) > 0:
            bate()
        player_ataques_cooldown -=1 * deltatempo
        '''
        #player_hitbox.draw()


    else:
        fundo_fim.draw()
        fundo_fim.update()
        andando_fim.draw()
        andando_fim.update()
        if fadout2.get_curr_frame()!=0:
            fadout2.draw()
            fadout2.update()
            fundo_snd.pause()
        if 22>fadout2.get_curr_frame()>=20:
            dialogo("Após restaurar a máquina e voltar à seu  presente,  você reporta a companhia às    autoridades                              Pouco tempo depois, o local é fechado    Você conseguiu impedir o futuro perigoso da empresa                                Obrigado por jogar! :D")
        if not fadout2.is_playing() and not mostrar_dialogo:
            acabou = 1
            comeca_jogo=0
            fadout2.set_curr_frame(0)
            fadin2.set_curr_frame(0)
            chaves_obtidas[0]=chaves_obtidas[1]=chaves_obtidas[2]=chaves_obtidas[3]=0




    if mostrar_dialogo:
        caixa_dialogo_fundo.draw()
        dialogo_update(text_dialogo)
        for tampa in tampa_texto:
            tampa.draw()
        rosto_dialogo[rosto_dialogo_id].draw()
        caixa_dialogo.draw()

    fade_screen(tempo_fade)




    janela.update()

    return acabou


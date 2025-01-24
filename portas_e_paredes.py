from PPlay.gameimage import *
from PPlay.window import *
from PPlay.sprite import *

janela = Window(1200,700)
janela.set_title("ChronoLab")

def define_portas(portas):
    portas[0].x = janela.width + portas[0].width / 2
    portas[0].y = janela.height / 2 - portas[0].height / 20
    portas[1].x = janela.width + portas[0].width / 2
    portas[1].y = portas[0].y + janela.height
    portas[2].x = janela.width * 2 + portas[0].width * 2.51
    portas[2].y = janela.height / 2 - portas[0].height / 20
    portas[3].x = janela.width * 3 - portas[3].width*2.8
    portas[3].y = janela.height / 2 - portas[0].height / 20
    for i in range(5,len(portas),1):
        portas[i].y = -janela.height
    portas[4].y = janela.height / 2 - portas[0].height / 20
    portas[4].x = janela.width * 4.3
    portas[5].x = portas[0].width * 1.8
    portas[6].y = janela.height / 2 - portas[0].height / 20
    portas[6].x = janela.width * 6 + portas[0].width*0.57
    portas[7].x = 0
    portas[8].x = janela.width * 7.2
    portas[9].x = -portas[9].width/2

def define_parede(paredes):
    paredes[0].x = janela.width * 2.2
    paredes[1].y = janela.height
    paredes[2].y = janela.height
    paredes[2].x = janela.width * 1.25
    paredes[4].x = janela.width * 2.64
    paredes[5].x = janela.width * 6
    paredes[6].y = paredes[7].y = paredes[17].y = 1000
    paredes[7].x = janela.width * 15
    paredes[8].x = janela.width * 7 + paredes[0].width/8
    paredes[9].x = janela.width * 1.26
    paredes[10].x = janela.width * 3.9
    paredes[11].x = paredes[15].x = 0
    paredes[12].x = janela.width * 2.2
    paredes[13].x = janela.width * 2.64
    paredes[14].x = janela.width * 6
    paredes[16].x = janela.width * 1.25
    paredes[18].x = janela.width * 1.25


def define_plataformas(plats):
    #plats[0].x = janela.width / 1.5
    #plats[0].y = janela.height / 1.35
    for i in range(1,len(plats)):
        plats[i].y = 1000
    plats[1].x = plats[2].width*0.18
    plats[2].x = plats[2].width*1.32
    plats[3].x = plats[2].width*2.46
    plats[4].x = plats[2].width * 3.6
    plats[5].x = plats[2].width * 4.74
    plats[6].x = plats[2].width * 5.88
    #plats[7].x = plats[2].width * 4.74
    plats[8].x = plats[2].width * 6.4
    plats[9].x = plats[2].width * 7.4
    plats[10].x = plats[2].width * 7.8
    plats[11].x = plats[2].width * 3.6
    #plats[12].x = plats[2].width * 7.54
    #plats[13].x = plats[2].width * (8.68 + 1.14 * 1)
    #plats[14].x = plats[2].width * (8.68 + 1.14 * 2)
    #plats[15].x = plats[2].width * (8.68 + 1.14 * 3)
    #plats[16].x = plats[2].width * (8.68 + 1.14 * 4)
    #plats[17].x = plats[2].width * (8.68 + 1.14 * 5)
    plats[18].x = plats[2].width * (15.25)
    plats[19].x = plats[2].width * (16.3)
    plats[20].x = plats[2].width * (16.3 + 1.14 * 1)
    plats[21].x = plats[2].width * (16.3 + 1.14 * 2)
    plats[22].x = plats[2].width * (16.3 + 1.14 * 3)
    plats[23].x = plats[2].width * (20.6)
    plats[24].x = plats[2].width * (21.6)
    plats[25].x = plats[2].width * (21.6 + 1.14 * 1)
    plats[26].x = plats[2].width * (21.6 + 1.14 * 2)
    plats[27].x = plats[2].width * (21.6 + 1.14 * 3)
    plats[28].x = plats[2].width * (21.6 + 1.14 * 4)
    plats[29].x = plats[2].width * (27.05)
    plats[30].x = plats[2].width * (27.05 + 1.14 * 1)
    plats[31].x = plats[2].width * (27.05 + 1.14 * 2)
    plats[32].x = plats[2].width * (27.05 + 1.14 * 3)
    plats[33].x = plats[2].width * (27.05 + 1.14 * 4)
    plats[34].x = -plats[2].width/2.1
    plats[35].x = plats[2].width * 0.5
    #room2
    plats[36].x = janela.width * 3 + plats[2].width * 1.46
    plats[37].x = plats[38].x = janela.width * 3 + plats[2].width * 10.75


def define_buracos(buracos):
    buracos[0].x = janela.width * 3 + Sprite("midia//Scifi DoorGRN SpriteSheet.png",12).width * 3.35
    buracos[0].y = janela.height - buracos[0].height
    for i in range(1,len(buracos)):
        buracos[i].y = 1000
    buracos[1].x = GameImage("midia//chao_268px.png").width * 8.8
    buracos[2].x = GameImage("midia//chao_268px.png").width * (8.8 + 0.8 * 1)
    buracos[3].x = GameImage("midia//chao_268px.png").width * (8.8 + 0.8 * 2)
    buracos[4].x = GameImage("midia//chao_268px.png").width * (8.8 + 0.8 * 3)
    buracos[5].x = GameImage("midia//chao_268px.png").width * (8.8 + 0.8 * 4)
    buracos[6].x = GameImage("midia//chao_268px.png").width * (8.8 + 0.8 * 5)
    buracos[7].x = GameImage("midia//chao_268px.png").width * (8.8 + 0.8 * 6)
    buracos[8].x = GameImage("midia//chao_268px.png").width * (8.8 + 0.8 * 7)

def define_colisores(colpa):
    for col in colpa:
        col.y=1000
    colpa[0].x = GameImage("midia//chao_268px.png").width * 2.3
    colpa[1].x = GameImage("midia//chao_268px.png").width * 6.4
    colpa[2].x = colpa[1].x
    colpa[3].x = GameImage("midia//chao_268px.png").width * 8.7
    colpa[4].x = colpa[3].x
    colpa[5].x = colpa[3].x
    colpa[6].x = GameImage("midia//chao_268px.png").width * 15.25
    colpa[7].x = colpa[6].x
    colpa[8].x = colpa[6].x
    colpa[9].x = colpa[6].x
    colpa[10].x = GameImage("midia//chao_268px.png").width * 16.18
    colpa[25].x = colpa[10].x
    colpa[11].x = colpa[10].x
    colpa[12].x = colpa[10].x
    colpa[13].x = colpa[10].x
    colpa[14].x = GameImage("midia//chao_268px.png").width * 17.65
    colpa[15].x = colpa[14].x
    colpa[16].x = colpa[14].x
    colpa[17].x = colpa[14].x
    colpa[18].x = colpa[14].x
    colpa[19].x = GameImage("midia//chao_268px.png").width * 18.45
    colpa[20].x = colpa[19].x
    colpa[21].x = GameImage("midia//chao_268px.png").width * 20.56
    colpa[22].x = GameImage("midia//chao_268px.png").width * 21.57
    colpa[23].x = GameImage("midia//chao_268px.png").width * 27.02
    colpa[24].x = GameImage("midia//chao_268px.png").width * 28.03
    colpa[25].x = colpa[26].x = colpa[27].x = colpa[28].x = GameImage("midia//chao_268px.png").width * 0.5

def define_blips(blipR1,blipR2):
    for i in range(len(blipR1)):
        blipR1[i].y = blipR2[i].y = -1000
    blipR1[0].x = GameImage("midia//chao_268px.png").width * 3
    blipR2[0].x = GameImage("midia//chao_268px.png").width * (3.6 + 1.14)
    blipR1[1].x = GameImage("midia//chao_268px.png").width * 9
    blipR2[1].x = GameImage("midia//chao_268px.png").width * 9
    blipR2[3].x = GameImage("midia//chao_268px.png").width * 10
    blipR1[2].x = GameImage("midia//chao_268px.png").width * 12.4
    blipR2[2].x = GameImage("midia//chao_268px.png").width * 12.4
    blipR1[3].x = GameImage("midia//chao_268px.png").width * 14
    blipR1[4].x = GameImage("midia//chao_268px.png").width * 16.4
    blipR2[4].x = GameImage("midia//chao_268px.png").width * 16.4
    blipR1[5].x = GameImage("midia//chao_268px.png").width * 16.4
    blipR1[6].x = blipR2[5].x = blipR2[8].x = GameImage("midia//chao_268px.png").width * 1.5
    blipR1[7].x = blipR2[6].x = blipR1[9].x = GameImage("midia//chao_268px.png").width * 3.1
    blipR1[8].x = blipR2[7].x = blipR2[9].x = GameImage("midia//chao_268px.png").width * 4.7







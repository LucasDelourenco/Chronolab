from PPlay.gameimage import *
from PPlay.window import *
from PPlay.keyboard import *
from jogo import *
from Menu import *

janela = Window(1200,700)
janela.set_title("ChronoLab")
tela=0
fim=0
Cenario = GameImage("midia//teste3_3.png")

while True:
    if tela==0:
        tela = Menu_principal()
    elif tela==1:
        fim=jogo()
        if fim==1:
            fim=0
            tela=0



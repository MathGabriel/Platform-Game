import random
import math
import pgzero
import pygame

#configurações
WIDTH = 610
HEIGHT = 600
azul = 150
azul_afrente = True
groundcolour = 0,0,139
chao = Rect ((0,580), (1000,20))

#Champion
campeao = Actor('stive.png',(300,250))
campeao_x_velocidade = 0
campeao_y_velocidade = 0
gravidade = 1
pulo = False
pulei = False
permitir_x = True
cronometro = []
#plataformas
plataforma1 = Rect((270,480),(80,10))
# plataforma2 = Rect((50,400),(100,10))
# plataforma3 = Rect((500,400),(100,10))
plataforma4 = Rect((150,300),(80,10))
plataforma5 = Rect((400,300),(80,10))
plataforma6 = Rect((100,200),(80,10))
plataforma7 = Rect((450,200),(80,10))
plataforma8 = Rect((0,80),(80,10))
plataforma9 = Rect((510,80),(80,10))

#lista de plataformas
# plataformas = [chao,plataforma1,plataforma2,plataforma3,plataforma4,plataforma5,plataforma6,plataforma7,plataforma8,plataforma9]
plataformas = [chao,plataforma1,plataforma4,plataforma5,plataforma6,plataforma7,plataforma8,plataforma9]

# Pontuação
dinheiro_x = [270,150,400,100,450,50,510,500]
dinheiro_y = [70,170,170,70,270,370,370,470]
d_xy = random.randint(0,7)
dinheiro = Actor('dinheiro',(dinheiro_x[d_xy],dinheiro_y[d_xy]))
pontos = 0

#função de desenho
def draw():
    # screen.fill((0, 163, 163))
    screen.fill((173,216, azul))
    screen.blit('montanha',(0,233))
    #loop para desenhar as plataformas e o chao
    for i in plataformas:
        screen.draw.filled_rect(i,groundcolour)
    campeao.draw()
    dinheiro.draw()

#funcao ficar atualizando
def update():
    backgroundcolorfade()
    campeao_mover()

def campeao_mover():
    global campeao_x_velocidade, campeao_y_velocidade, pulo, gravidade, pulei, cronometro, permitir_x

    # face para frente
    if campeao_x_velocidade == 0 and not pulei:
        campeao.image = "stive"

    #gravidade 
    if collidecheck():
        gravidade = 1
        campeao.y -= 1
        permitir_x = True
        cronometro = []
    if not collidecheck():
        campeao.y += gravidade
        if gravidade <= 20:
            gravidade += 0.5
        cronometro.append(pygame.time.get_ticks())
        if len(cronometro) > 5 and not pulei:
            permitir_x = False
            campeao.image = "jump"
            if len(cronometro) > 20:
                campeao.image = "jump_caindo_meio"
                if len(cronometro) > 30:
                    campeao.image = "jump_caindo"

    #movimento esquerda 
    if(keyboard.left) and permitir_x:
        if (campeao.x > 40) and (campeao_x_velocidade > -8):
            campeao_x_velocidade -= 2
            campeao.image = "run_left"
            if (keyboard.left) and pulei:
                campeao.image = "run_left"
    #movimento direita
    if(keyboard.right) and permitir_x:
        if (campeao.x < 580) and (campeao_x_velocidade < 8):
            campeao_x_velocidade += 2
            campeao.image = "run"
            if (keyboard.right) and pulei:
                campeao.image = "run"
    campeao.x += campeao_x_velocidade

    #Velocidade do campeao
    if campeao_x_velocidade > 0:
        campeao_x_velocidade -= 1
    if campeao_x_velocidade < 0:
            campeao_x_velocidade += 1
    #code para que o boneco nao saia da tela ao andar
    if campeao.x < 50 or campeao.x > 580:
        campeao_x_velocidade = 0

    #funcao para pular
    if(keyboard.space) and collidecheck() and not pulei:
        pulo = True
        pulei = True
        clock.schedule_unique(pulo_continuo, 0.5)
        campeao.image = "jump"
        campeao_y_velocidade = 95

    if pulo and campeao_y_velocidade > 25:
        campeao_y_velocidade = campeao_y_velocidade - ((100 - campeao_y_velocidade)/2)
        campeao.y -= campeao_y_velocidade/3 #altura do pulo
    else:
        campeao_y_velocidade = 0
        pulo = False

def collidecheck():
    collide = False
    for i in plataformas:
        if campeao.colliderect(i):
            collide = True
    return collide

def pulo_continuo():
    global pulei
    pulei = False


def backgroundcolorfade():
    global azul, azul_afrente
    if azul < 255 and azul_afrente:
        azul += 1
    else:
        azul_afrente = False
    if azul > 130 and not azul_afrente:
        azul -= 1
    else:
        azul_afrente = True
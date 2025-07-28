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

#plataformas
plataforma1 = Rect((270,500),(100,10))
plataforma2 = Rect((50,400),(100,10))
plataforma3 = Rect((500,400),(100,10))
plataforma4 = Rect((150,300),(100,10))
plataforma5 = Rect((400,300),(100,10))
plataforma6 = Rect((100,200),(100,10))
plataforma7 = Rect((450,200),(100,10))
plataforma8 = Rect((0,100),(100,10))
plataforma9 = Rect((510,100),(100,10))

#lista de plataformas
plataformas = [chao,plataforma1,plataforma2,plataforma3,plataforma4,plataforma5,plataforma6,plataforma7,plataforma8,plataforma9]

#função de desenho
def draw():
    # screen.fill((0, 163, 163))
    screen.fill((173,216, azul))
    screen.blit('montanha',(0,233))
    #loop para desenhar as plataformas e o chao
    for i in plataformas:
        screen.draw.filled_rect(i,groundcolour)
    campeao.draw()

#funcao ficar atualizando
def update():
    backgroundcolorfade()
    campeao_mover()

def campeao_mover():
    global campeao_x_velocidade, campeao_y_velocidade, pulo, gravidade

    #gravidade 
    if collidecheck():
        gravidade = 1
        campeao.y -= 1
    if not collidecheck():
        campeao.y += gravidade
        if gravidade <= 20:
            gravidade += 0.5

    #movimento esquerda e direita
    if(keyboard.left):
        if (campeao.x > 40) and (campeao_x_velocidade > -8):
            campeao_x_velocidade -= 2
    if(keyboard.right):
        if (campeao.x < 580) and (campeao_x_velocidade < 8):
            campeao_x_velocidade += 2
    campeao.x += campeao_x_velocidade

    if campeao_x_velocidade > 0:
        campeao_x_velocidade -= 1
    if campeao_x_velocidade < 0:
            campeao_x_velocidade += 1
    #code para que o boneco nao saia da tela
    if campeao.x < 50 or campeao.x > 580:
        campeao_x_velocidade = 0

def collidecheck():
    collide = False
    for i in plataformas:
        if campeao.colliderect(i):
            collide = True
    return collide

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



# boneco = Actor('stive.png')
# boneco.topright = 0, 10

# #funcao fazer o alien e o fundo aparecer
# def draw():
#     screen.fill((0, 163, 163))
#     boneco.draw()

# def update():
#     boneco.left += 2
#     if boneco.left > WIDTH:
#         boneco.right = 0

# def on_mouse_down(pos):
#     if boneco.collidepoint(pos):
#         sounds.pulo1.play()
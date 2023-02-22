import math
import pygame 
import numpy as np
import random
from imagens import *

pygame.init()

# Tamanho da tela e definição do FPS
pos = np.array([1024,768])
screen = pygame.display.set_mode(pos)
clock = pygame.time.Clock()
FPS = 60  # Frames per Second

pontuacao = 0
vida = 3

#obtendo o fonte usada na pontuação
font = pygame.font.SysFont(None, 30)

BLACK = (0, 0, 0)
COR_PERSONAGEM = (30, 200, 20)

# Inicializar posicoes
s0 = np.array([100, 364])
v0 = np.array([15, -15])
a = np.array([0, 0.15])
v = v0
s = s0
planeta = np.array([pos[0]-500, pos[1]-364])

# Personagem
personagem = pygame.Surface((10, 10))  # Tamanho do personagem
personagem.fill(COR_PERSONAGEM)  # Cor do personagem

#detector de colisão
inimigo_morto = True

rodando = True



# circle_surface = pygame.Surface(barros.get_size(), pygame.SRCALPHA)
# mask = pygame.draw.circle(circle_surface, (0, 0, 0, 255), (barros.get_width() // 2, barros.get_height() // 2), barros.get_width() // 2)
# inimigo = pygame.Surface(barros.get_size(), pygame.SRCALPHA)
# inimigo.blit(barros, (0, 0))
# inimigo.blit(circle_surface, (0, 0), special_flags=pygame.BLEND_RGBA_MIN)





tela_jogo = True
while tela_jogo:
    screen.blit(jelado, (0, 0))
    text = font.render('Jelado Wars', False, (0, 0, 0))
    text_baixo = font.render('Escolha um personagem', False, (0, 0, 0))
    textRect = text.get_rect()
    screen.blit(text_baixo, (370,45))
    textRect.center = (480, 30)
    screen.blit(text, textRect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            tela_jogo = False
            rodando = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            tela_jogo = False
            pygame.display.update()

    pygame.display.update()





while rodando:

    # Capturar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
    
    if inimigo_morto == True:
        posicao_inimigo = (random.randint(500, 1020), random.randint(100, 700))
        inimigo_morto = False


    #evento so acontecer quando clicar com o mouse
    if event.type == pygame.MOUSEBUTTONDOWN:

        while True:
            if s[0]<0 or s[0]>1024 or s[1]<0 or s[1]>768: # Se eu chegar ao limite da tela, reinicio a posição do personagem
                v0 = (pygame.mouse.get_pos() - s0)
                v0 = v0 / np.linalg.norm(v0) * 100
                v0 = v0 + 3*np.random.randn(2)
                s, v = s0, v0
                break

            # Controlar frame rate
            clock.tick(FPS)          


            C = 20000 # constante gravitacional * massa planeta
            direcao_a = planeta - s
            d = np.linalg.norm(direcao_a)
            direcao_a = direcao_a / d
            mag_a = C / d**2
            a = direcao_a * mag_a
            v = v + a
            s = s + 0.25 * v

            # Desenhar fundo
            screen.blit(background, (0, 0))


            rect = pygame.Rect(s, (10, 10))  # First tuple is position, second is size.
            screen.blit(personagem, rect)
            planet = pygame.draw.circle(screen, "red", planeta, 10, 10)

            if inimigo_morto == False:
                # screen.blit(inimigo, posicao_inimigo)
                inimigo = pygame.draw.circle(screen, "green", posicao_inimigo, 20, 20)


            if inimigo.collidepoint(s):
                inimigo_morto = True  
                pontuacao+=1
                print(pontuacao)

    # Update!
              #blitando a pontuação na tela
            text = font.render('Pontos:' + str(pontuacao), False, (255,255,255))
            textRect = text.get_rect()
            textRect.center = (100, 100)
            screen.blit(text, textRect)
            pygame.display.update()

# Terminar tela
pygame.quit()
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


#variável pra contar as tentativas do jogador
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
#loop do jogo
rodando = True


#variáveis que definem se o jogo será no modo fácil ou difícil
modo_facil = False
modo_dificil = False


#sorteia a foto dos personagens
sorteador_planetas_1 = random.choice([barros, enzo]) 

# Tocar música
pygame.mixer.music.load('audios\musica_fundo.mp3')
pygame.mixer.music.play(-1)

tela_morreu = False
teste = 0

#loop da tela inicial
tela_jogo = True
while tela_jogo:


    screen.blit(jelado, (0, 0))

    pos_mouse = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            tela_jogo = False
            rodando = False
            teste = 1
        if event.type == pygame.MOUSEBUTTONDOWN:
            tela_jogo = False
            pygame.display.update()
        if event.type == pygame.MOUSEBUTTONDOWN and pos_mouse[0]< 963 and pos_mouse[0]> 812 and pos_mouse[1]< 673 and pos_mouse[1]> 611:
            tela_jogo = False
            rodando = False
            teste = 1
            pygame.display.update()
        if event.type == pygame.MOUSEBUTTONDOWN and pos_mouse[0]< 874 and pos_mouse[0]> 746 and pos_mouse[1]< 539 and pos_mouse[1]> 490:
            tela_jogo = False
            modo_facil = True
            pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN and pos_mouse[0]< 1011 and pos_mouse[0]> 890 and pos_mouse[1]< 539 and pos_mouse[1]> 486:
            tela_jogo = False
            modo_dificil = True
            pygame.display.update()

        elif modo_dificil ==  False and modo_facil == False and teste == 0:
            tela_jogo = True

    pygame.display.update()



    if modo_facil == True:
        tentativas = 5
        pontuacao = 0
        #loop do jogo
        while rodando:

            # Capturar eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    rodando = False

            screen.blit(background, (100, 320), pygame.Rect(100, 320, 90, 90))
            mouse_pos = pygame.mouse.get_pos()
            # Calcular ângulo entre o canhão e o mouse
            dx = mouse_pos[0] - canhao_rect.center[0]
            dy = mouse_pos[1] - canhao_rect.center[1]
            angle = np.degrees(np.arctan2(-dy, dx))
            # Rotacionar imagem do canhão para o ângulo calculado
            canhao_rot = pygame.transform.rotate(canhao, angle)
            canhao_rect_rot = canhao_rot.get_rect(center=canhao_rect.center)
            # Desenhar imagem rotacionada do canhão na tela
            screen.blit(canhao_rot, (100, 320),canhao_rect_rot)
            pygame.display.update()

            #evento so acontecer quando clicar com o mouse
            if event.type == pygame.MOUSEBUTTONDOWN:

                if tentativas < 1:
                    modo_facil = False
                    tela_morreu = True
                    break
                else:
                    tentativas -= 1

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
                    screen.blit(canhao_rot, (100, 320),canhao_rect_rot)



                    rect = pygame.Rect(s, (10, 10))
                    screen.blit(personagem, rect)
                    planet = pygame.draw.circle(screen, "red", planeta, 20, 20)

                    if inimigo_morto == True:
                        #sorteia nova posição do inimigo
                        posicao_inimigo = (random.randint(500, 1020), random.randint(100, 700))

                        #sortea novo inimigo
                        sorteador_inimigos = random.choice([ergio, guri, lucca, magno, vaz, wever, celao, alfredo, leo])

                        #declara estado do inimigo como vivo
                        inimigo_morto = False

                    if inimigo_morto == False:
                        # screen.blit(inimigo, posicao_inimigo)
                        inimigo = pygame.draw.circle(screen, "green", posicao_inimigo, 20, 20)

                        #feito
                        if sorteador_inimigos == ergio:
                            screen.blit(ergio, (posicao_inimigo[0]-29, posicao_inimigo[1]-31))

                        #Feito
                        if sorteador_inimigos == guri:
                            screen.blit(guri, (posicao_inimigo[0]-33, posicao_inimigo[1]-45))

                        if sorteador_inimigos == lucca:
                            screen.blit(lucca, (posicao_inimigo[0]-33, posicao_inimigo[1]-45))
                        if sorteador_inimigos == magno:
                            screen.blit(magno, (posicao_inimigo[0]-33, posicao_inimigo[1]-45))
                        if sorteador_inimigos == vaz:
                            screen.blit(vaz, (posicao_inimigo[0]-33, posicao_inimigo[1]-45))
                        if sorteador_inimigos == wever:
                            screen.blit(wever, (posicao_inimigo[0]-29, posicao_inimigo[1]-31))
                        if sorteador_inimigos == celao:
                            screen.blit(celao, (posicao_inimigo[0]-29, posicao_inimigo[1]-31))
                        if sorteador_inimigos == alfredo:
                            screen.blit(alfredo, (posicao_inimigo[0]-29, posicao_inimigo[1]-31))
                        if sorteador_inimigos == leo:
                            screen.blit(leo, (posicao_inimigo[0]-29, posicao_inimigo[1]-31))



                    if inimigo.collidepoint(s):
                        inimigo_morto = True  
                        pontuacao+=1
                        tentativas = 5
                        rodando = True



                    #blitando a pontuação na tela
                    text = font.render('Pontos:' + str(pontuacao), False, (255,255,255))
                    textRect = text.get_rect()
                    textRect.center = (100, 100)
                    screen.blit(text, textRect)
                    text_tentativas = font.render('Tentativas:' + str(tentativas), False, (255,255,255))
                    textRect_tentativas = text_tentativas.get_rect()
                    textRect_tentativas.center = (100, 150)
                    screen.blit(text_tentativas, textRect_tentativas)

                    #blitando skins dos planetas
                    screen.blit(sorteador_planetas_1, ([pos[0]-525, pos[1]-390]))
                    pygame.display.update()

        if tela_morreu == True:
            tela_jogo_morreu = True
            while tela_jogo_morreu:
                screen.blit(Jelado_morreu, (0, 0))
                pos_mouse = pygame.mouse.get_pos()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        tela_jogo_morreu = False
                        rodando = False
                    if event.type == pygame.MOUSEBUTTONDOWN and pos_mouse[0]< 835 and pos_mouse[0]> 538 and pos_mouse[1]< 674 and pos_mouse[1]> 601:
                        tela_jogo_morreu = False
                        tela_jogo = True
                        modo_facil = False
                        pygame.display.update()
                    pygame.display.update()
            # Atualizar tela
            pygame.display.update()





    if modo_dificil == True:
        tentativas = 10
        pontuacao = 0


        barros_planeta = np.array([400, 400])
        enzo_planeta = np.array([600, 300])

        def gravidade(constante, planeta):
            direcao_a = planeta - s # constante gravitacional * massa planeta
            d = np.linalg.norm(direcao_a)
            direcao_a = direcao_a / d
            mag_a = constante / d**2
            a = direcao_a * mag_a
            return a

        while rodando:
            # Capturar eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    rodando = False
            
            screen.blit(background2, (100, 320), pygame.Rect(100, 320, 90, 90))
            mouse_pos = pygame.mouse.get_pos()
            # Calcular ângulo entre o canhão e o mouse
            dx = mouse_pos[0] - canhao_rect.center[0]
            dy = mouse_pos[1] - canhao_rect.center[1]
            angle = np.degrees(np.arctan2(-dy, dx))
            # Rotacionar imagem do canhão para o ângulo calculado
            canhao_rot = pygame.transform.rotate(canhao, angle)
            canhao_rect_rot = canhao_rot.get_rect(center=canhao_rect.center)
            # Desenhar imagem rotacionada do canhão na tela
            screen.blit(canhao_rot, (100, 320),canhao_rect_rot)
            pygame.display.update()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if tentativas < 1:
                    modo_dificil = False
                    tela_morreu = True
                    break
                else:
                    tentativas -= 1

                while True:
                    # Capturar eventos
                    if s[0]<5 or s[0]>pos[0] or s[1]<5 or s[1]>pos[1]: # Se eu chegar ao limite da tela, reinicio a posição do personagem
                        v0 = (pygame.mouse.get_pos() - s0)
                        v0 = v0 / np.linalg.norm(v0) * 100
                        v0 = v0 + 3 * np.random.randn(2)
                        s, v = s0, v0
                        break

                    # Controlar frame rate
                    clock.tick(FPS)

                    # Desenhar fundo
                    screen.blit(background2, (0, 0))
                    screen.blit(canhao_rot, (100, 320),canhao_rect_rot)
                    pygame.display.update()

                    # Processar posicoes
                    ac_barros = gravidade(40000, barros_planeta)
                    ac_enzo = gravidade(70000, enzo_planeta)
                    a = ac_barros + ac_enzo
                    v = v + a
                    s = s + 0.25 * v

                    # Desenhar personagem
                    rect = pygame.Rect(s, (10, 10))  # First tuple is position, second is size.
                    screen.blit(personagem, rect)
                    planet = pygame.draw.circle(screen, "red", barros_planeta, 20, 20)
                    planet2 = pygame.draw.circle(screen, "blue", enzo_planeta , 20, 20)

                    if inimigo_morto == True:
                        #sorteia nova posição do inimigo
                        posicao_inimigo = (random.randint(500, 1020), random.randint(100, 700))

                        #sortea novo inimigo
                        sorteador_inimigos = random.choice([ergio, guri, lucca, magno, vaz, wever, celao, alfredo, leo])

                        #declara estado do inimigo como vivo
                        inimigo_morto = False

                    if inimigo_morto == False:
                        # screen.blit(inimigo, posicao_inimigo)
                        inimigo = pygame.draw.circle(screen, "green", posicao_inimigo, 20, 20)

                        #feito
                        if sorteador_inimigos == ergio:
                            screen.blit(ergio, (posicao_inimigo[0]-29, posicao_inimigo[1]-31))

                        #Feito
                        if sorteador_inimigos == guri:
                            screen.blit(guri, (posicao_inimigo[0]-33, posicao_inimigo[1]-45))

                        if sorteador_inimigos == lucca:
                            screen.blit(lucca, (posicao_inimigo[0]-33, posicao_inimigo[1]-45))
                        if sorteador_inimigos == magno:
                            screen.blit(magno, (posicao_inimigo[0]-33, posicao_inimigo[1]-45))
                        if sorteador_inimigos == vaz:
                            screen.blit(vaz, (posicao_inimigo[0]-33, posicao_inimigo[1]-45))
                        if sorteador_inimigos == wever:
                            screen.blit(wever, (posicao_inimigo[0]-29, posicao_inimigo[1]-31))
                        if sorteador_inimigos == celao:
                            screen.blit(celao, (posicao_inimigo[0]-29, posicao_inimigo[1]-31))
                        if sorteador_inimigos == alfredo:
                            screen.blit(alfredo, (posicao_inimigo[0]-29, posicao_inimigo[1]-31))
                        if sorteador_inimigos == leo:
                            screen.blit(leo, (posicao_inimigo[0]-29, posicao_inimigo[1]-31))



                    if inimigo.collidepoint(s):
                        inimigo_morto = True  
                        pontuacao+=1
                        tentativas = 10
                        rodando = True



                    #blitando a pontuação na tela
                    text = font.render('Pontos:' + str(pontuacao), False, (255,255,255))
                    textRect = text.get_rect()
                    textRect.center = (100, 100)
                    screen.blit(text, textRect)
                    text_tentativas = font.render('Tentativas:' + str(tentativas), False, (255,255,255))
                    textRect_tentativas = text_tentativas.get_rect()
                    textRect_tentativas.center = (100, 150)
                    screen.blit(text_tentativas, textRect_tentativas)


                    screen.blit(barros, ([pos[0]-448, pos[1]-490]))
                    screen.blit(enzo, ([pos[0]-650, pos[1]-390]))
                    # Update!
                    pygame.display.update()

        if tela_morreu == True:
            tela_jogo_morreu = True
            while tela_jogo_morreu:
                screen.blit(Jelado_morreu, (0, 0))
                pos_mouse = pygame.mouse.get_pos()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        tela_jogo_morreu = False
                        rodando = False
                    if event.type == pygame.MOUSEBUTTONDOWN and pos_mouse[0]< 835 and pos_mouse[0]> 538 and pos_mouse[1]< 674 and pos_mouse[1]> 601:
                        tela_jogo_morreu = False
                        tela_jogo = True
                        modo_facil = False
                        pygame.display.update()
                    pygame.display.update()
            # Atualizar tela
            pygame.display.update()
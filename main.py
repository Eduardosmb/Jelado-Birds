import math
import pygame 
import numpy as np

pygame.init()

# Tamanho da tela e definição do FPS
pos = np.array([1024,768])
screen = pygame.display.set_mode(pos)
clock = pygame.time.Clock()
FPS = 60  # Frames per Second

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

rodando = True
while rodando:
    # Capturar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

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


            # # Processar posicoes
            # v = v + a
            # s = s + 0.1 * v

            # Desenhar fundo
            screen.fill(BLACK)


            rect = pygame.Rect(s, (10, 10))  # First tuple is position, second is size.
            screen.blit(personagem, rect)
            planet = pygame.draw.circle(screen, "red", planeta, 10, 10)

            # Desenhar personagem
            # rect = pygame.Rect(s, (10, 10))  # First tuple is position, second is size.
            # screen.blit(personagem, rect)

    # Update!
            pygame.display.update()

# Terminar tela
pygame.quit()
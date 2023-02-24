import pygame

background = pygame.image.load('imagens/galaxia.png')
background = pygame.transform.scale(background, (1024, 768))


canhao = pygame.image.load('imagens/canhao.png')
canhao = pygame.transform.scale(canhao, (60, 60))
canhao_rect = canhao.get_rect()

jelado = pygame.image.load('imagens/jelado.png')
jelado = pygame.transform.scale(jelado, (1024, 768))

Jelado_morreu = pygame.image.load('imagens/jelado_tela_morreu.png')
Jelado_morreu = pygame.transform.scale(Jelado_morreu, (1024, 768))

alfredo = pygame.image.load('imagens/alfredo.png')

barros = pygame.image.load('imagens/barros.png')
barros = pygame.transform.scale(barros, (50, 50))

celao = pygame.image.load('imagens/celao.png')

enzo = pygame.image.load('imagens/enzo.png')
enzo = pygame.transform.scale(enzo, (50, 50))

ergio = pygame.image.load('imagens/ergio.png')
ergio = pygame.transform.scale(ergio, (58, 58))

guri = pygame.image.load('imagens/guri.png')
guri = pygame.transform.scale(guri, (65, 65))


lucca = pygame.image.load('imagens/lucca.png')
lucca = pygame.transform.scale(lucca, (65, 65))

magno = pygame.image.load('imagens/magno.png')
magno = pygame.transform.scale(magno, (65, 65))

vaz = pygame.image.load('imagens/vaz.png')
vaz = pygame.transform.scale(vaz, (65, 65))

wever = pygame.image.load('imagens/wever.png')
wever = pygame.transform.scale(wever, (58, 58))
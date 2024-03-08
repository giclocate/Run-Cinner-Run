import pygame
from pygame.locals import *
from sys import exit
import os


diretorio_principal = os.path.dirname(__file__)
diretorio_imagens = os.path.join(diretorio_principal, 'imagens')

LARGURA = 640
ALTURA = 480

BRANCO = (255,255,255)

tela = pygame.display.set_mode((LARGURA, ALTURA))

pygame.display.set_caption('Projeto P1')

# separar os frames da spritesheet
sprite_sheet = pygame.image.load(os.path.join(diretorio_imagens, 'alunosprite.png')).convert_alpha()
nuvem_sprite_sheet = pygame.image.load(os.path.join(diretorio_imagens, 'clouds-small.png')).convert_alpha()
# convert_alpha vai ignorar a transparência


# sprite do aluno
class Aluno(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imagens_aluno = []
        for i in range(7):
            img = sprite_sheet.subsurface((i * 46,0), (46,50))
            img = pygame.transform.scale(img, (46*3, 46*3))
            self.imagens_aluno.append(img)
        
        self.index_lista = 0    
        self.image = self.imagens_aluno[int(self.index_lista)]
        self.rect = self.image.get_rect()
        self.rect.center = (100,ALTURA - 130)
    
    # método update    
    def update(self):
        if self.index_lista > 6:
            self.index_lista = 0
        self.index_lista+= 0.25 
        self.image = self.imagens_aluno[int(self.index_lista)]
        
# ignora esse da nuvem pq tá incompleto    
class Nuvens(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = nuvem_sprite_sheet.subsurface((0,0), (512, 128))
        self.image = pygame.transform.scale(self.image, (512*2, 128*2))
        self.rect = self.image.get_rect()
        self.rect.center = (30, 30)
        
    def update(self):
        if self.rect.topright[0] < 0:
            self.rect.x = LARGURA
        self.rect.x -= 10

# adicionando as sprites    
all_sprites = pygame.sprite.Group()
aluno = Aluno()
all_sprites.add(aluno)

nuvem = Nuvens()
all_sprites.add(nuvem)


relogio = pygame.time.Clock()
while True:
    relogio.tick(30)
    tela.fill(BRANCO)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

#adicionando na tela as sprites criadas
    all_sprites.draw(tela)
    all_sprites.update()

    pygame.display.flip()

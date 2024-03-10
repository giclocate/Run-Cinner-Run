import pygame
from pygame.locals import *
from sys import exit
import os
from random import randrange
pygame.mixer.init()

diretorio_principal = os.path.dirname(__file__)
diretorio_imagens = os.path.join(diretorio_principal, 'imagens')
diretorio_sons = os.path.join(diretorio_principal, 'Sounds')
LARGURA = 640
ALTURA = 480

BRANCO = (255,255,255)

tela = pygame.display.set_mode((LARGURA, ALTURA))

pygame.display.set_caption('Projeto P1')

# separar os frames da spritesheet
sprite_sheet = pygame.image.load(os.path.join(diretorio_imagens, 'alunosprite.png')).convert_alpha()
nuvem_sprite_sheet = pygame.image.load(os.path.join(diretorio_imagens, 'clouds-small.png')).convert_alpha()
ground_sprite_sheet = pygame.image.load(os.path.join(diretorio_imagens, 'Basic_Ground.png')).convert_alpha()
# convert_alpha vai ignorar a transparência


# sprite do aluno
class Aluno(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.som_pulo = pygame.mixer.Sound(os.path.join(diretorio_sons, 'SFX_Jump_09.wav'))
        self.som_queda = pygame.mixer.Sound(os.path.join(diretorio_sons, 'jumpland.wav'))
        self.som_pulo.set_volume(1)
        self.imagens_aluno = []
        for i in range(7):
            img = sprite_sheet.subsurface((i * 46,0), (46,50))
            img = pygame.transform.scale(img, (46*3, 46*3))
            self.imagens_aluno.append(img)
        
        self.index_lista = 0    
        self.image = self.imagens_aluno[int(self.index_lista)]
        self.rect = self.image.get_rect()
        self.pos_y_inicial = ALTURA - 125 - (138//2)  #Variavel pra poder saber a posição inicial do personagem e poder realizar o pulo
        self.rect.center = (100,ALTURA - 125)
        self.pulo = False
    def pular(self):
        self.pulo = True
        self.som_pulo.play()
    # método update    
    def update(self):
        #quando é teclado a barra de espaço o self.pulo == True daí vamos animar o movimento
        if self.pulo == True:
            if self.rect.y <= 200:
                self.pulo = False
            self.rect.y -= 20
        else:
            if self.rect.y < self.pos_y_inicial:
                self.rect.y += 20    
            else:
                self.rect.y = self.pos_y_inicial
                
                
        if self.index_lista > 6:
            self.index_lista = 0
        self.index_lista+= 0.25 
        self.image = self.imagens_aluno[int(self.index_lista)]
        
#classe das nuvens atualizada   
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

#classe do chão
class Ground(pygame.sprite.Sprite):
    def __init__(self, pos_x ):
        pygame.sprite.Sprite.__init__(self)
        self.image = ground_sprite_sheet.subsurface((0,0), (32,32))
        self.image = pygame.transform.scale(self.image, (32 * 2, 32 * 2))
        self.rect = self.image.get_rect()
        self.rect.y = ALTURA - 64
        self.rect.x = pos_x * 64

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


for i in range(LARGURA*3//64):
    ground = Ground(i)
    all_sprites.add(ground)

#Eventos do jogo
relogio = pygame.time.Clock()
while True:
    relogio.tick(30)
    tela.fill(BRANCO)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            #eric: Se for teclada o espaço ele "pula"
            if event.key == K_SPACE:
                if aluno.rect.y != aluno.pos_y_inicial: #if para evitar que o aluno fique pulando no ar
                    pass
                else:
                    aluno.pular()
#adicionando na tela as sprites criadas
    all_sprites.draw(tela)
    all_sprites.update()

    pygame.display.flip()

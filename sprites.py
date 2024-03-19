import pygame
from pygame.locals import *
import os
import random
from random import choice


pygame.mixer.init()
pygame.font.init()

diretorio_principal = os.path.dirname(__file__)
diretorio_imagens = os.path.join(diretorio_principal, 'assets\imagens')
diretorio_sons = os.path.join(diretorio_principal, 'assets\Sounds')
diretorio_background = os.path.join(diretorio_principal, diretorio_sons, 'assets\Background')

#Definições de tela
LARGURA = 640
ALTURA = 480
pontos = 0
tempo = 0

BRANCO = (255,255,255)

tela = pygame.display.set_mode((LARGURA, ALTURA))

pygame.display.set_caption('Projeto P1')

#Limites de spawn de objetos

y_minimo, y_maximo = 200, 250

# separar os frames da spritesheet
sprite_sheet = pygame.image.load(os.path.join(diretorio_imagens, 'alunosprite.png')).convert_alpha()
nuvem_sprite_sheet = pygame.image.load(os.path.join(diretorio_imagens, 'clouds-small.png')).convert_alpha()
ground_sprite_sheet = pygame.image.load(os.path.join(diretorio_imagens, 'Basic_Ground.png')).convert_alpha()
rock_sprite = pygame.image.load(os.path.join(diretorio_imagens, 'Rock Pile.png')).convert_alpha()
water_sprite = pygame.image.load(os.path.join(diretorio_imagens, 'Water Bottle.png')).convert_alpha()
cafe_sprite = pygame.image.load(os.path.join(diretorio_imagens, 'Coffee.png')).convert_alpha()
livro_sprite = pygame.image.load(os.path.join(diretorio_imagens, 'Book2.png')).convert_alpha()
fundo = pygame.image.load(os.path.join(diretorio_imagens, 'sky.png')).convert_alpha()
# convert_alpha vai ignorar a transparência


#Erio: função para sortear um número e para pegar um som aleatório de colisão
escolha_som_colisao = choice([0, 1, 2, 3, 4]) 
if escolha_som_colisao == 0:
    som_colisao = pygame.mixer.Sound(os.path.join(diretorio_sons, 'gta-v-wasted-death-sound.mp3'))
elif escolha_som_colisao == 1:
    som_colisao = pygame.mixer.Sound(os.path.join(diretorio_sons, 'uh-steve-minecraft-online-audio-converter.mp3'))
elif escolha_som_colisao == 2:
    som_colisao = pygame.mixer.Sound(os.path.join(diretorio_sons, 'dark-souls-you-died-sound-effect_hm5sYFG.mp3'))
elif escolha_som_colisao == 3:
    som_colisao = pygame.mixer.Sound(os.path.join(diretorio_sons, 'bruh-sound-effect-2-320-kbps.mp3'))
elif escolha_som_colisao == 4:
    som_colisao = pygame.mixer.Sound(os.path.join(diretorio_sons, 'emotional-damage-meme.mp3'))    
som_colisao.set_volume(1)

#Som de coleta de objeto
som_coleta_objeto = pygame.mixer.Sound(os.path.join(diretorio_sons, 'Pickup_Coin.wav'))
som_coleta_objeto.set_volume(1)

#Eric: variável para indicar que é game over, provando que colidiu com o objeto de rocha
colidiu = False

#criei essa variavel para quando implementarmos os objetos conseguirmos mexer nisso melhor
velocidade_jogo = 10

# sprite do aluno
class Aluno(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.som_pulo = pygame.mixer.Sound(os.path.join(diretorio_sons, 'SFX_Jump_09.wav'))
        self.som_queda = pygame.mixer.Sound(os.path.join(diretorio_sons, 'jumpland.wav')) #som da queda, ainda está com defeito (Eric)
        self.som_pulo.set_volume(1)
        self.imagens_aluno = []
        for i in range(7):
            img = sprite_sheet.subsurface((i * 46,0), (46,50))
            img = pygame.transform.scale(img, (46*3, 46*3))
            self.imagens_aluno.append(img)
        
        self.index_lista = 0    
        self.image = self.imagens_aluno[int(self.index_lista)]
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
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
            if self.rect.y <= 150:
                self.pulo = False
            self.rect.y -= 20
        else:
            if self.rect.y < self.pos_y_inicial:
                self.rect.y += 10
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
        
        
#classe pedra
class Rock(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = rock_sprite.subsurface((0,0), (160,160))
        self.image = pygame.transform.scale(self.image, (160/3, 160/3))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.center = (LARGURA,ALTURA - 88 )
    def update(self):
        if self.rect.topright[0] < 0:
            self.rect.x = LARGURA
        self.rect.x -= velocidade_jogo
        
#classe da água  
class Water(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = water_sprite.subsurface((0,0), (16,16))
        self.image = pygame.transform.scale(self.image, (16*2, 16*2))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = LARGURA
        self.rect.y = random.randint(y_minimo, y_maximo)

    def update(self):
        if self.rect.topright[0] < 0:
            self.rect.x = LARGURA
            self.rect.y = random.randint(y_minimo, y_maximo)
        self.rect.x -= velocidade_jogo

#classe do café        
class Coffee(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = cafe_sprite.subsurface((0,0), (16,16))
        self.image = pygame.transform.scale(self.image, (16*2, 16*2))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = LARGURA
        self.rect.y = random.randint(y_minimo, y_maximo)
        
    def update(self):
        if self.rect.topright[0] < 0:
            self.rect.x = LARGURA
            self.rect.y = random.randint(y_minimo, y_maximo)
        self.rect.x -= velocidade_jogo

#classe do livro
class Livro(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = livro_sprite.subsurface((0,0), (48,48))
        self.image = pygame.transform.scale(self.image, (20*2, 20*2))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = LARGURA
        self.rect.y = random.randint(y_minimo, y_maximo)
        
    def update(self):
        if self.rect.topright[0] < 0:
            self.rect.x = LARGURA
            self.rect.y = random.randint(y_minimo, y_maximo)
        self.rect.x -= velocidade_jogo

def bg():
    escala = pygame.transform.scale(fundo, (LARGURA, ALTURA))
    tela.blit(escala,(0,0))

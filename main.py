import pygame
from pygame.locals import *
from sys import exit
import os
from random import randrange
pygame.mixer.init()
pygame.font.init()


diretorio_principal = os.path.dirname(__file__)
diretorio_imagens = os.path.join(diretorio_principal, 'imagens')
diretorio_sons = os.path.join(diretorio_principal, 'Sounds')
diretorio_background = os.path.join(diretorio_principal, diretorio_sons, 'Background')
LARGURA = 640
ALTURA = 480
pontos = 0
tempo = 0

BRANCO = (255,255,255)

tela = pygame.display.set_mode((LARGURA, ALTURA))

pygame.display.set_caption('Projeto P1')

# separar os frames da spritesheet
sprite_sheet = pygame.image.load(os.path.join(diretorio_imagens, 'alunosprite.png')).convert_alpha()
nuvem_sprite_sheet = pygame.image.load(os.path.join(diretorio_imagens, 'clouds-small.png')).convert_alpha()
ground_sprite_sheet = pygame.image.load(os.path.join(diretorio_imagens, 'Basic_Ground.png')).convert_alpha()
rock_sprite = pygame.image.load(os.path.join(diretorio_imagens, 'Rock Pile.png')).convert_alpha()
# convert_alpha vai ignorar a transparência

som_colisao = pygame.mixer.Sound(os.path.join(diretorio_sons, 'gta-v-wasted-death-sound.mp3'))
som_colisao.set_volume(1)
colidiu = False
#criei essa variavel para quando implementarmos os objetos conseguirmos mexer nisso melhor
velocidade_jogo = 10

#essa funcao vai exibr a pontuacao e game over
def exibe_mensagem(msg, tamanho, cor):
    fonte = pygame.font.SysFont('comicsanssms', tamanho, True, False)
    mensagem = f'{msg}'
    texto_formatado = fonte.render(mensagem, True, cor)
    return texto_formatado

    
    

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
                self.rect.y += 15    
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

rock = Rock()
all_sprites.add(rock)


# criando o grupo onde vai ser inserido os obstáculos que colidirem
group_obstacles = pygame.sprite.Group()
group_obstacles.add(rock)


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
                


    colisoes = pygame.sprite.spritecollide(aluno, group_obstacles, False, pygame.sprite.collide_mask) 
    
    all_sprites.draw(tela)

    if colisoes and colidiu == False:
        som_colisao.play()
        colidiu = True

    if colidiu == True:
        game_over = exibe_mensagem('VOCÊ PERDEU :(', 40, (0,0,0)) #game over
        tela.blit(game_over, (LARGURA//2, ALTURA//2))
        pass
    else:
        tempo +=0.05
        all_sprites.update()
        #adicionando na tela as sprites criadas
        #pontuacao
        texto_tempo = exibe_mensagem(int(tempo), 40, (255,0,0))
        texto_pontos = exibe_mensagem(int(pontos), 40, (0,0,0))
        
    tela.blit(texto_tempo, (520, 30))#mostra o tempo na tela
    tela.blit(texto_pontos, (300, 30))#mostra pontuação na tela

    pygame.display.flip()




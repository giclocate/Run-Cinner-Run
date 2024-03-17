import pygame
from pygame.locals import *
from sys import exit
<<<<<<< HEAD
from sprites import Aluno, Nuvens, Ground, Rock, Water
from utils import exibe_mensagem
from random import choice

=======
import os
from random import randrange, choice
>>>>>>> f4ab3d287f0a73769c21f18a0a9b9d9db995438c
pygame.mixer.init()
pygame.font.init()

def main():
    pygame.init()
    tela = pygame.display.set_mode((640, 480))
    pygame.display.set_caption('Projeto P1')
    relogio = pygame.time.Clock()

    all_sprites = pygame.sprite.Group()
    group_obstacles = pygame.sprite.Group()
    group_object = pygame.sprite.Group()

    aluno = Aluno()
    nuvem = Nuvens()
    rock = Rock()
    water = Water()

    all_sprites.add(aluno, nuvem, rock, water)

    for i in range(640 * 3 // 64):
        ground = Ground(i)
        all_sprites.add(ground)

<<<<<<< HEAD
    group_obstacles.add(rock)
    group_object.add(water)

    escolha_som_colisao = choice([0, 1, 2, 3, 4]) 
    if escolha_som_colisao == 0:
        som_colisao = pygame.mixer.Sound('assets/Sounds/gta-v-wasted-death-sound.mp3')
    elif escolha_som_colisao == 1:
        som_colisao = pygame.mixer.Sound('assets/Sounds/uh-steve-minecraft-online-audio-converter.mp3')
    elif escolha_som_colisao == 2:
        som_colisao = pygame.mixer.Sound('assets/Sounds/dark-souls-you-died-sound-effect_hm5sYFG.mp3')
    elif escolha_som_colisao == 3:
        som_colisao = pygame.mixer.Sound('assets/Sounds/bruh-sound-effect-2-320-kbps.mp3')
    elif escolha_som_colisao == 4:
        som_colisao = pygame.mixer.Sound('assets/Sounds/emotional-damage-meme-.mp3')
=======
# separar os frames da spritesheet
sprite_sheet = pygame.image.load(os.path.join(diretorio_imagens, 'alunosprite.png')).convert_alpha()
nuvem_sprite_sheet = pygame.image.load(os.path.join(diretorio_imagens, 'clouds-small.png')).convert_alpha()
ground_sprite_sheet = pygame.image.load(os.path.join(diretorio_imagens, 'Basic_Ground.png')).convert_alpha()
rock_sprite = pygame.image.load(os.path.join(diretorio_imagens, 'Rock Pile.png')).convert_alpha()
water_sprite = pygame.image.load(os.path.join(diretorio_imagens, 'Water Bottle.png')).convert_alpha()
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
    som_colisao = pygame.mixer.Sound(os.path.join(diretorio_sons, 'emotional-damage-meme-.mp3'))    
som_colisao.set_volume(1)

#Som de coleta de objeto
som_coleta_objeto = pygame.mixer.Sound(os.path.join(diretorio_sons, 'Pickup_Coin.wav'))
som_coleta_objeto.set_volume(1)

#Eric: variável para indicar que é game over, provando que colidiu com o objeto de rocha
colidiu = False

#criei essa variavel para quando implementarmos os objetos conseguirmos mexer nisso melhor
velocidade_jogo = 10
>>>>>>> f4ab3d287f0a73769c21f18a0a9b9d9db995438c

    som_colisao.set_volume(0)
    som_coleta_objeto = pygame.mixer.Sound('assets/Sounds/Pickup_Coin.wav')
    som_coleta_objeto.set_volume(0)

    colidiu = False
    tempo = 0
    pontos = 0

<<<<<<< HEAD
    while True:
        relogio.tick(30)
        tela.fill((255, 255, 255))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    if aluno.rect.y != aluno.pos_y_inicial:
                        pass
                    else:
                        aluno.pular()

        colisoes = pygame.sprite.spritecollide(aluno, group_obstacles, False, pygame.sprite.collide_mask) 
        objetos = pygame.sprite.spritecollide(aluno, group_object, True, pygame.sprite.collide_mask) 
        all_sprites.draw(tela)

        if not objetos:
            pontos += 20
            som_coleta_objeto.play()

        if colisoes and not colidiu:
            som_colisao.play()
            colidiu = True

        if colidiu:
            game_over = exibe_mensagem('VOCÊ PERDEU :(', 40, (0,0,0)) #game over
            tela.blit(game_over, (640//2, 480//2))
        else:
            tempo += 0.05
            all_sprites.update()

        texto_tempo = exibe_mensagem(int(tempo), 40, (255, 0, 0))
        texto_pontos = exibe_mensagem(int(pontos), 40, (0, 0, 0))
        tela.blit(texto_tempo, (520, 30))
        tela.blit(texto_pontos, (300, 30))

        pygame.display.flip()

if __name__ == '__main__':
    main()
=======
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
        # Eric: quando é teclado a barra de espaço o self.pulo == True daí vamos animar o movimento
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

#classe da água
class Water(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = water_sprite.subsurface((0,0), (16,16))
        self.image = pygame.transform.scale(self.image, (16*2, 16*2))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.center = (LARGURA,ALTURA - 180)

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

water = Water()
all_sprites.add(water)


# criando o grupo onde vai ser inserido os obstáculos que colidirem
group_obstacles = pygame.sprite.Group()
group_obstacles.add(rock)


# criando o grupo onde vai ser inserido os objetos que vão interagir com o boneco
group_object = pygame.sprite.Group()
group_object.add(water)


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
    objetos = pygame.sprite.spritecollide(aluno, group_object, True, pygame.sprite.collide_mask) 
    all_sprites.draw(tela)


    if objetos == False:
        texto_pontos += 20
        som_coleta_objeto.play()

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
>>>>>>> f4ab3d287f0a73769c21f18a0a9b9d9db995438c

import pygame
from pygame.locals import *
from sys import exit
from sprites import Aluno, Nuvens, Ground, Rock, Water, Coffee
from utils import exibe_mensagem
from random import choice

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
    cafe = Coffee()

    all_sprites.add(aluno, nuvem, rock, water, cafe)

    velocidade_jogo = 10

    for i in range(640 * 3 // 64):
        ground = Ground(i)
        all_sprites.add(ground)

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
        som_colisao = pygame.mixer.Sound('assets/Sounds/emotional-damage-meme.mp3')

    som_colisao.set_volume(1)
    som_coleta_objeto = pygame.mixer.Sound('assets/Sounds/Pickup_Coin.wav')
    som_coleta_objeto.set_volume(1)
    
    colidiu = False
    tempo = 0
    pontos = 1000

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
            # Movimentação do componente
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and aluno.rect.x > 0:
            aluno.rect.x -= 10
        if keys[pygame.K_RIGHT] and aluno.rect.x < 640 - 138:
            aluno.rect.x += 10        

        colisoes = pygame.sprite.spritecollide(aluno, group_obstacles, False, pygame.sprite.collide_mask) 
        objetos = pygame.sprite.spritecollide(aluno, group_object, True, pygame.sprite.collide_mask) 
        all_sprites.draw(tela)
        
        tipos_objetos = [Water, Coffee]
        contador_objetos = 0
        
        if objetos:
            for objeto in objetos:
                # Verifica se o objeto é do tipo café ou água
                if isinstance(objeto, Coffee):
                    # Aumenta a velocidade do jogo quando o café é coletado
                    velocidade_jogo += 2

                # Cria um novo objeto alternando entre água e café
                novo_objeto = tipos_objetos[contador_objetos]()
                contador_objetos = (contador_objetos + 1) % len(tipos_objetos)  # Atualiza o contador para alternar
                group_object.add(novo_objeto)
                all_sprites.add(novo_objeto)
                
                pontos += 20
                som_coleta_objeto.play()


        if colisoes and colidiu == False:
            som_colisao.play()
            colidiu = True

        #if tempo == 10 and pontos > 1000: #mudança de fase de jogo
            #velocidade_jogo = 20    

        if colidiu:
            game_over = exibe_mensagem('VOCÊ PERDEU :(', 40, (0,0,0)) #game over
            tela.blit(game_over, (640//2, 480//2))
            pass

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

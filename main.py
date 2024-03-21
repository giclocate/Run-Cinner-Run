import pygame
from pygame.locals import *
from sys import exit
from sprites import Aluno, Nuvens, Ground, Rock, Water, Coffee, Livro, bg, Flag, Calculo, Ground2, water_redimensionada, livro_redimensionado, coffee_redimensionado, clock, gameover
from utils import exibe_mensagem, exibe_mensagem2
from random import choice

pygame.mixer.init()
pygame.font.init()



def main():
    pygame.init()
    musica_de_fundo = pygame.mixer.music.load('assets/Background/Lemon Knife - Zombified! (Instrumental).mp3')
    pygame.mixer.music.play(-1)
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
    livro = Livro()
    flag = Flag()
    calculo = Calculo()
    all_sprites.add(aluno, nuvem, rock, water, cafe, livro, flag, calculo)

    velocidade_aluno = 10
    aumenta_uma_vez = False

    for i in range(640 * 3 // 64):
            ground = Ground(i)
            ground2 = Ground2(i)
            all_sprites.add(ground, ground2)

    group_obstacles.add(rock)
    group_object.add(water, cafe, livro)

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
    pontos = 0
    pontos_water = 0
    pontos_livro = 0
    pontos_coffee = 0

    while True:
        relogio.tick(30)
        bg()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            #Pulo do personagem    
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    if aluno.rect.y != aluno.pos_y_inicial:
                        pass
                    else:
                        aluno.pular()
            # Movimentação do personagem
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and aluno.rect.x > 0 and colidiu == False:
            aluno.rect.x -= velocidade_aluno
        if keys[pygame.K_RIGHT] and aluno.rect.x < 640 - 138 and colidiu == False:
            aluno.rect.x += velocidade_aluno     

        #Sistema de colisões
        colisoes = pygame.sprite.spritecollide(aluno, group_obstacles, False, pygame.sprite.collide_mask) 
        objetos = pygame.sprite.spritecollide(aluno, group_object, True, pygame.sprite.collide_mask) 
        all_sprites.draw(tela)
        
        tipos_objetos = [Water, Coffee, Livro]
        contador_objetos = 0
        
        if objetos:
            for objeto in objetos:
                # Verifica se o objeto é do tipo café ou água
                if isinstance(objeto, Coffee):
                    # Aumenta a velocidade do jogo quando o café é coletado
                    pontos += 5
                    pontos_coffee += 1
                    velocidade_aluno += 1
                if isinstance(objeto, Livro):
                    pontos += 20
                    pontos_livro += 1
                if isinstance(objeto, Water):
                    pontos += 10
                    pontos_water += 1   

                # Cria um novo objeto alternando entre água e café
                novo_objeto = tipos_objetos[contador_objetos]()
                contador_objetos = (contador_objetos + 1) % len(tipos_objetos)  # Atualiza o contador para alternar
                group_object.add(novo_objeto)
                all_sprites.add(novo_objeto)
                
                som_coleta_objeto.play()

        if colisoes and colidiu == False:
            som_colisao.play()
            colidiu = True

        #Teste if tempo > 10 and  tempo < 10.10:
           #rock.aumentavelocidade()
        #objetos condicionais
        if pontos == 0:
            start = exibe_mensagem2('CÁLCULO I', 40, (238,18,18)) 
            tela.blit(start, (200, 160))
            calculo.condicao()   
        #Condição pra segunda fase - Fisica I 
        if pontos >1000 and pontos <= 1050 and aumenta_uma_vez == False:
            flag.condicao() #Faz a flag aparecer uma vez
            ground2.condicao() #Era pra trocar o chão mas não tá pegando ainda
            fase2= exibe_mensagem2('FISICA I', 40, (0,0,0)) #Exibe mensagem de mudança de Fase
            tela.blit(fase2, (230, 240))
            rock.aumentavelocidade() #Aumenta a velocidade da rocha em +10
            water.aumentavelocidade() #Aumenta a velocidade da agua em +10
            cafe.aumentavelocidade() #Aumenta a velocidade da agua em +10
            aumenta_uma_vez = True

        #Condição de Game Over
        if colidiu:
            tela.blit(gameover,(120,120)) #exibe imagem de game over
            game_over = exibe_mensagem2(f'VOCÊ REPROVOU EM {int(tempo)} SEGUNDOS', 20, (0,0,0)) #game over
            tela.blit(game_over, (160, 260)) #exibe mensagem de game over
            pygame.mixer.music.stop()
            pass

        else:
            tempo += 0.05
            all_sprites.update()

        texto_tempo = exibe_mensagem(int(tempo), 40, (255, 0, 0))
        texto_pontos = exibe_mensagem(int(pontos), 40, (0, 0, 0))
        texto_water = exibe_mensagem(int(pontos_water), 40, (0, 0, 0))
        texto_coffee = exibe_mensagem(int(pontos_coffee), 40, (0, 0, 0))
        texto_livro = exibe_mensagem(int(pontos_livro), 40, (0, 0, 0))
        
        tela.blit(texto_tempo, (520, 30))
        tela.blit(texto_pontos, (300, 30))
        
        tela.blit(texto_water, (60, 30))
        tela.blit(texto_coffee,(60, 70))
        tela.blit(texto_livro,(60, 110))
        
        tela.blit(water_redimensionada, (20, 30))
        tela.blit(coffee_redimensionado, (20, 70))
        tela.blit(livro_redimensionado, (20, 110))
        tela.blit(clock, (490, 25))
    

        pygame.display.flip()

if __name__ == '__main__':
    main()
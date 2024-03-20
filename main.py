import pygame
from pygame.locals import *
from sys import exit
from sprites import Aluno, Nuvens, Ground, Rock, Water, Coffee, Livro, bg, Flag, Calculo, Ground2
from utils import exibe_mensagem
from random import choice

pygame.mixer.init()
pygame.font.init()

def exibir_texto(surf, texto, tamanho, x, y, cor):
    fonte = pygame.font.Font(None, tamanho)
    texto_surface = fonte.render(texto, True, cor)
    texto_rect = texto_surface.get_rect()
    texto_rect.center = (x, y)
    surf.blit(texto_surface, texto_rect)

def menu(tela, largura, altura):
    cor_fundo = (0, 0, 0)
    cor_titulo = (255, 255, 255)
    cor_opcoes = (255, 255, 255)
        
    relogio = pygame.time.Clock()

    while True:
        tela.fill(cor_fundo)  #cor de fundo do menu

        exibir_texto(tela, "Jogo de P1", 48, largura // 2, 100, cor_titulo)

        exibir_texto(tela, "Pressione 'S' para Iniciar", 30, largura // 2, 250, cor_opcoes)
        exibir_texto(tela, "Pressione 'Q' para Sair", 30, largura // 2, 300, cor_opcoes)

        pygame.display.update()
        relogio.tick(30)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_s:
                    return "iniciar"
                if event.key == K_q:
                    return "sair"


def main():
    tela = pygame.display.set_mode((640, 480))
    pygame.display.set_caption('Projeto P1')

    escolha = menu(tela, 640, 480)  # Chamando a função menu para exibir o menu

    if escolha == "iniciar":
        # Iniciar o jogo principal
        pygame.mixer.init()
        musica_de_fundo = pygame.mixer.music.load('assets/Background/Lemon Knife - Zombified! (Instrumental).mp3')
        pygame.mixer.music.play(-1)
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
                all_sprites.add(ground,ground2)

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
        pontos = 900

        while True:
            relogio.tick(30)
            bg()

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                #pulo do personagem    
                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        if aluno.rect.y != aluno.pos_y_inicial:
                            pass
                        else:
                            aluno.pular()
                #movimentação do personagem
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and aluno.rect.x > 0 and colidiu == False:
                aluno.rect.x -= velocidade_aluno
            if keys[pygame.K_RIGHT] and aluno.rect.x < 640 - 138 and colidiu == False:
                aluno.rect.x += velocidade_aluno     

            #sistema de colisões
            colisoes = pygame.sprite.spritecollide(aluno, group_obstacles, False, pygame.sprite.collide_mask) 
            objetos = pygame.sprite.spritecollide(aluno, group_object, True, pygame.sprite.collide_mask) 
            all_sprites.draw(tela)
            
            tipos_objetos = [Water, Coffee, Livro]
            contador_objetos = 0
            
            if objetos:
                for objeto in objetos:
                    #verifica se o objeto é do tipo café ou água
                    if isinstance(objeto, Coffee):
                        #aumenta a velocidade do jogo quando o café é coletado
                        pontos += 5
                        velocidade_aluno += 1
                    if isinstance(objeto, Livro):
                        pontos += 20
                    if isinstance(objeto, Water):
                        pontos += 10   

                    #cria um novo objeto alternando entre água e café
                    novo_objeto = tipos_objetos[contador_objetos]()
                    contador_objetos = (contador_objetos + 1) % len(tipos_objetos)  #atualiza o contador para alternar
                    group_object.add(novo_objeto)
                    all_sprites.add(novo_objeto)
                    
                    som_coleta_objeto.play()

            if colisoes and colidiu == False:
                som_colisao.play()
                colidiu = True

            #teste if tempo > 10 and  tempo < 10.10:
            #rock.aumentavelocidade()
            #objetos condicionais
            if pontos == 0:
                start = exibe_mensagem('CALCULO I', 60, (0,0,0)) 
                tela.blit(start, (640//2, 480//2))
                calculo.condicao()   
            #condição pra segunda fase - Fisica I 
            if pontos >1000 and pontos <= 1020 and aumenta_uma_vez == False:
                flag.condicao() #faz a flag aparecer uma vez
                ground2.condicao() #era pra trocar o chão mas não tá pegando ainda
                fase2= exibe_mensagem('FISICA I', 60, (0,0,0)) #Exibe mensagem de mudança de Fase
                tela.blit(fase2, (640//2, 480//2))
                rock.aumentavelocidade() #aumenta a velocidade da rocha em +10
                water.aumentavelocidade() #aumenta a velocidade da agua em +10
                cafe.aumentavelocidade() #aumenta a velocidade da agua em +10
                aumenta_uma_vez = True

            #condição de Game Over
            if colidiu:
                game_over = exibe_mensagem('VOCÊ PERDEU :(', 40, (0,0,0)) #game over
                tela.blit(game_over, (640//2, 480//2))
                pygame.mixer.music.stop()
                pass

            else:
                tempo += 0.05
                all_sprites.update()

            texto_tempo = exibe_mensagem(int(tempo), 40, (255, 0, 0))
            texto_pontos = exibe_mensagem(int(pontos), 40, (0, 0, 0))
            tela.blit(texto_tempo, (520, 30))
            tela.blit(texto_pontos, (300, 30))

            pygame.display.flip()
    elif escolha == "sair":
        pygame.quit()
        exit()

    pygame.quit()
    exit()

if __name__ == '__main__':
    main()
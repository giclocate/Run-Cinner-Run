import pygame
from pygame.locals import *
from sys import exit
from sprites import Aluno, Nuvens, Ground, Rock, Water, Coffee, Livro
from utils import exibe_mensagem
from random import choice

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
    pygame.init()

    largura = 640
    altura = 480
    tela = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption('Jogo de P1')

    pontos = 0
    contador_agua_coletada = 0
    contador_cafe_coletado = 0
    contador_livro_coletado = 0

    while True:
        opcao = menu(tela, largura, altura)

        if opcao == "iniciar":
            print("Iniciar jogo")
            break 

        elif opcao == "sair":
            pygame.quit()
            exit()

    pygame.mixer.init()
    pygame.font.init()

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

    all_sprites.add(aluno, nuvem, rock, water, cafe, livro)

    velocidade_jogo = 10

    for i in range(640 * 3 // 64):
        ground = Ground(i)
        all_sprites.add(ground)

    group_obstacles.add(rock)

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
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and aluno.rect.x > 0:
            aluno.rect.x -= 10
        if keys[pygame.K_RIGHT] and aluno.rect.x < 640 - 138:
            aluno.rect.x += 10        

        colisoes = pygame.sprite.spritecollide(aluno, group_obstacles, False, pygame.sprite.collide_mask) 
        objetos = pygame.sprite.spritecollide(aluno, group_object, True, pygame.sprite.collide_mask) 
        all_sprites.draw(tela)
        
        if objetos:
            for objeto in objetos:
                if isinstance(objeto, Water):
                    pontos += 10 
                    contador_agua_coletada += 1
                elif isinstance(objeto, Coffee):
                    pontos += 20 
                    contador_cafe_coletado += 1
                elif isinstance(objeto, Livro):
                    pontos += 30 
                    contador_livro_coletado += 1

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

        texto_contador_agua = exibe_mensagem(f'Água coletada: {contador_agua_coletada}', 30, (0, 0, 255))
        texto_contador_cafe = exibe_mensagem(f'Café coletado: {contador_cafe_coletado}', 30, (255, 0, 0))
        texto_contador_livro = exibe_mensagem(f'Livro coletado: {contador_livro_coletado}', 30, (0, 255, 0))
        tela.blit(texto_contador_agua, (20, 70))
        tela.blit(texto_contador_cafe, (20, 100))
        tela.blit(texto_contador_livro, (20, 130))

        pygame.display.flip()

if __name__ == '__main__':
    main()

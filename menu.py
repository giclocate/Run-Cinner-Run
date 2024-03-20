import pygame
from pygame.locals import *
import os

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

    #variáveis
    pontos = 0
    tempo = 0

    while True:
        opcao = menu(tela, largura, altura)

        if opcao == "iniciar":
            print("Iniciar jogo")
            break 

        elif opcao == "sair":
            pygame.quit()
            exit()

if __name__ == '__main__':
    main()
import pygame
from pygame.locals import *
from utils import exibir_texto


def menu(tela, largura, altura):
    
    pygame.display.set_caption("Menu")
    
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
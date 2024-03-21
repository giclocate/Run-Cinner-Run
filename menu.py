import pygame
from pygame.locals import *
import os
from utils import exibir_texto


def menu(tela, largura, altura):
    
    pygame.display.set_caption("Menu")
    diretorio_principal = os.path.dirname(__file__)
    diretorio_imagens = os.path.join(diretorio_principal, 'assets\imagens')
    background = pygame.image.load(os.path.join(diretorio_imagens, 'backgroundmenu.png')).convert_alpha()
    background_redimensionado = pygame.transform.scale(background, (640, 480))
    

    cor_opcoes = (0, 0, 0)

    relogio = pygame.time.Clock()

    while True:
        tela.blit(background_redimensionado, (0, 0))  #cor de fundo do menu

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
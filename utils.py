import pygame
from pygame.locals import *
from sys import exit


def exibir_texto(surf, texto, tamanho, x, y, cor):
    fonte = pygame.font.Font(None, tamanho)
    texto_surface = fonte.render(texto, True, cor)
    texto_rect = texto_surface.get_rect()
    texto_rect.center = (x, y)
    surf.blit(texto_surface, texto_rect)


def exibe_mensagem(msg, tamanho, cor):
    fonte = pygame.font.SysFont('comicsanssms', tamanho, True, False)
    mensagem = f'{msg}'
    texto_formatado = fonte.render(mensagem, True, cor)
    return texto_formatado

def exibe_mensagem2(msg, tamanho, cor):
    fonte = pygame.font.SysFont('comicsans', tamanho, True, False)
    mensagem = f'{msg}'
    texto_formatado = fonte.render(mensagem, True, cor)
    return texto_formatado
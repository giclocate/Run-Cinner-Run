import pygame
from pygame.locals import *
from sys import exit


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
import pygame
from pygame.locals import *
import sys


tela = pygame.display.set_mode((640, 480))
main_font = pygame.font.SysFont("arcade normal", 50)

star_img = pygame.image.load('buttons0.png').convert_alpha()
quit_img = pygame.image.load('buttons1.png').convert_alpha()


pygame.init()

class Button():
    def __init__(self, image, x_pos, y_pos, text_input):
        self.image = image
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_input = text_input
        self.text = main_font.render(self.text_input, True, "white")
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def update(self):
        tela.blit(self.image, self.rect)
        tela.blit(self.text, self.text_rect)
        
    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            print("Button Press!")

    def changeColor(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = main_font.render(self.text_input, True, "green")
        else:
            self.text = main_font.render(self.text_input, True, "white")
            
button_surface = pygame.image.load("buttons0.png")
button_surface = pygame.transform.scale(button_surface, (400, 150))

button = Button(button_surface, 400, 300, "Button")

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.MOUSEBUTTONDOWN:
			button.checkForInput(pygame.mouse.get_pos())

	tela.fill("white")

	button.update()
	button.changeColor(pygame.mouse.get_pos())

	pygame.display.update()
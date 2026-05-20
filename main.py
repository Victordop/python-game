import pygame

pygame.init() #inicia pygame
window = pygame.display.set_mode(size=(600,480)) #configura tela

while True: #condicional para mostrar a tela até fecha-la
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() #fecha janela
            quit() #fecha pygame
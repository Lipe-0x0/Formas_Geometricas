import numpy as np
import pygame


# Iniciando
pygame.init()

# Altura e Largura da Tela
alt = 760
lar = 760

# Superfície
screen = pygame.display.set_mode((lar, alt))

# Preenchendo superfície com a cor branca
screen.fill("white")

# Título da janela
pygame.display.set_caption("Quadrado")


# Mostrando superfície enquanto loop estiver ativo
while True:
    
    # Verificando se "Q" foi pressionado, se sim fechar janela
    for evento in pygame.event.get():
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_q:
                pygame.display.quit()

    pygame.display.update()

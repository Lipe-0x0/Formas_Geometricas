import numpy as np
import pygame


# ------------------ Forma ---------------------

# Criação dos 4 pontos no espaço 2D
pontos = np.array(
    [
        [350,350],
        [350,380],
        [380,350],
        [380,380]
     ]
        )

# Projeção dos pontos no espaço 3D




# ------------------- Canva ---------------------

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


    # Desenhando pontos
    for ponto in pontos:
        pygame.draw.circle(screen, "black", (ponto[0], ponto[1]), 5)


    pygame.display.flip()

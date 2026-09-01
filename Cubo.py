import numpy as np
import pygame


# ------------------ Formas ---------------------

# Ângulo de rotação
theta = 0.2

# Raio dos pontos
raio = 10

# Diametro dos pontos
diam = raio*2

# Criação dos 4 pontos no espaço 2D
pontos = np.array(
    [
        [350,350,0],
        [350,380+diam,0],
        [380+diam,350,0],
        [380+diam,380+diam,0]
     ]
        )

# Criação das arestas


# Projeção dos pontos no espaço 3D
Matriz_projec = np.array(
    [
        [1.10,0,0],
        [0,1.10,0]
    ]
        )

# Matrizes de rotação

rotX = np.array(
    [
        [np.cos(theta), -np.sin(theta), 0],
        [np.sin(theta), np.cos(theta), 0],
        [0,0,1]
    ]
        )
    

rotY = np.array(
    [
        [np.cos(theta), 0, -np.sin(theta)],
        [0,1,0],
        [np.sin(theta), 0, np.cos(theta)]
    ]
        )


rotZ = np.array(
    [
        [1,0,0],
        [0,np.cos(theta), -np.sin(theta)],
        [0,np.sin(theta), np.cos(theta)]
    ]
        )


# ------------------- Canva ---------------------

# Iniciando
pygame.init()

# Frames por segundo(FPS)
clock = pygame.time.Clock()

# Altura e Largura da Tela
alt = 760
lar = 760

# Centro da screen
centro = np.array([lar/2, alt/2, 0])

# Superfície
screen = pygame.display.set_mode((lar, alt))

# Título da janela
pygame.display.set_caption("Quadrado")


# Mostrando superfície enquanto loop estiver ativo
while True:

    screen.fill("white") # Preenchendo a superfície toda hora com a cor branca

    clock.tick(60) # 30 FPS 
    
    # Verificando se tecla foi pressionado para ativar alguma ação
    for evento in pygame.event.get():
        if evento.type == pygame.KEYDOWN: # Evento de saída
            if evento.key == pygame.K_q:
                pygame.display.quit()


    # Desenhando pontos
    for linha in range(np.shape(pontos)[0]):
        pygame.draw.circle(screen, "black", (pontos[linha,:][0], pontos[linha,:][1]), raio)

        # Desenhando projeção dos pontos do cubo
        projec = Matriz_projec @ pontos[linha,:]
        pygame.draw.circle(screen, "black", (projec[0], projec[1]), raio)

        # Rotacionando em relação ao X-axis da matriz de pontos 2D
        # Resolvendo problema de rotação em torno da origem
        # Explicação: pego cada ponto e envio para origem, então rotaciono ele por lá e por fim trago de volta já rotacionado para o centro novamente
        
        pontos[linha,:] = rotX @ (pontos[linha,:] - centro) + centro # Rotação x-axis dos vértices
        
        # Rotação x-axis das arestas




    pygame.display.flip()

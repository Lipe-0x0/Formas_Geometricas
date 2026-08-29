import numpy as np
import pygame


# ------------------------- Funções Complementares --------------------

def norma(vetor):
    return np.sqrt(np.sum(vetor * vetor))


# ------------------ Forma ---------------------

# Ângulo de rotação
theta = 0.5

# Criação dos 4 pontos no espaço 2D
pontos = np.array(
    [
        [350,380,0],
        [380,350,0],
        [350,350,0],
        [380,380,0]
     ]
        )

# Projeção dos pontos no espaço 3D
Matriz_projec = np.array(
    [
        [1.05,0,0],
        [0,1.05,0]
    ]
        )

# Matrizes de rotação
def rotacaoX(Matriz):
    rotX = np.array(
        [
            [np.cos(theta), -np.sin(theta), 0],
            [np.sin(theta), np.cos(theta), 0],
            [0,0,0]
        ]
            )

    return Matriz @ rotX

def rotacaoY(Matriz):
    rotY = np.array(
        [
            [np.cos(theta), 0, -np.sin(theta)],
            [0,0,0],
            [np.sin(theta), 0, np.cos(theta)]
        ]
            )

    Matriz @ rotY

def rotacaoZ(Matriz):
    rotZ = np.array(
        [
            [0,0,0],
            [0,np.cos(theta), -np.sin(theta)],
            [0,np.sin(theta), np.cos(theta)]
        ]
            )

    Matriz @ rotZ



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
    
    # Verificando se tecla foi pressionado para ativar alguma ação
    for evento in pygame.event.get():
        if evento.type == pygame.KEYDOWN: # Evento de saída
            if evento.key == pygame.K_q:
                pygame.display.quit()



    # Desenhando pontos
    for linha in range(np.shape(pontos)[0]):
        pygame.draw.circle(screen, "black", (pontos[linha,:][0], pontos[linha,:][1]), 5)

        # Desenhando projeção dos pontos do cubo
        projec = Matriz_projec @ pontos[linha,:]

        pygame.draw.circle(screen, "black", (projec[0], projec[1]), 5)

        # Rotacionando em relação ao X-axis da matriz de pontos 2D
        Matriz_projec = rotacaoX(Matriz_projec)



    pygame.display.flip()

import numpy as np
import pygame


# ------------------------- Funções Complementares --------------------

def norma(vetor):
    return np.sqrt(np.sum(vetor * vetor))


# ------------------ Forma ---------------------

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
def rotacaoX(Matriz, linha1, linha2):

    rotX = np.array(
        [
            [linha1[0]/norma(linha1), linha1[1]/norma(linha), 0],
            [linha2[0]/norma(linha2), linha2[1]/norma(linha2), 0],
            [0,0,0]
        ]
            )

    print(rotX)

    rotX @ Matriz


def rotacaoY(linha1, linha2):
    rotY = np.array(
        [
            [linha1[0]/norma(linha1), 0, linha1[2]/norma(linha1)],
            [0,0,0],
            [linha2[0]/norma(linha2), 0, linha2[2]/norma(linha2)]
        ]
            )


def rotacaoZ(linha1, linha2):
    rotZ = np.array(
        [
            [],
            []
        ]
            )



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
        if evento.type == pygame.KEYDOWN: # Evento de saída
            if evento.key == pygame.K_q:
                pygame.display.quit()


    # Desenhando pontos
    for linha in range(np.shape(pontos)[0]):
        pygame.draw.circle(screen, "black", (pontos[linha,:][0], pontos[linha,:][1]), 5)

        # Desenhando projeção dos pontos do cubo
        projec = Matriz_projec @ pontos[linha,:]

        pygame.draw.circle(screen, "black", (projec[0], projec[1]), 5)

        # Rotacionando em relação ao X-axes da matriz de projeção
        rotacaoX(Matriz_projec, Matriz_projec[0], Matriz_projec[1])



    pygame.display.flip()

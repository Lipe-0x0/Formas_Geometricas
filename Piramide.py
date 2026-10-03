from src_apoio.HelpMatriz import zeroarray, escmult, matmult
import math
import pyglet as pg
from pyglet.math import Mat4


# ----------------- Funções Complementares -------------------


# ----------------- Formas --------------------

# Ângulo de rotação
theta = 0.02

# Raio dos pontos
raio = 7

# Criação dos pontos que formam a pirâmide base triangular
pontos = [
            [-200, -200, 100],
            [200, -200, 100],
            [0, -200, -100],
            [0, 200, 0]
        ]


# Matrizes de Rotação

rotXYZ = [
            [],
            [],
            []
        ] 

rotX = [
            [1, 0, 0],
            [0, math.cos(theta), -math.sin(theta)],
            [0, math.cos(theta), math.sin(theta)]
        ]


# --------------------- Criação da Superfície -------------------

# Tamanho da tela (Largura x Altura)
lar = 720
alt = 720

# Superfície
screen = pg.window.Window(fullscreen = True)

# Redimensionando janela para que o centro seja (0,0)
@screen.event
def on_resize(width, height):
    # Projeção Ortográfica 2D
    screen.projection = Mat4.orthogonal_projection(
            left = -width/2,
            right = width/2,
            bottom = -height/2,
            top = height/2,
            z_near = -300,
            z_far = 300
            )

# Projetando e Renderizando na superfície
@screen.event
def on_draw():
    screen.clear()
    
    for ind in range(len(pontos)):
        
        # Renderizando cada ponto
        pg.shapes.Circle(x = pontos[ind][0], y = pontos[ind][1], radius = raio, color = (255,255,255)).draw()

pg.app.run()

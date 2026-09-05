import numpy as np
import pyglet as pg
from pyglet.math import Mat4

# ------------------ Formas ---------------------

# Ângulo de rotação
theta = 0.2

# Raio dos pontos
raio = 7

# Diametro dos pontos
diam = raio*2

# Criação dos 4 pontos no espaço 2D
pontos = np.array(
    [
        [-50,-50,0],
        [-50,50+diam,0],
        [50+diam,-50,0],
        [50+diam,50+diam,0]
     ]
       ,dtype = "float64" )

# Criação das arestas


# Projeção dos pontos no espaço 3D
Matriz_projec = np.array(
    [
        [2,0,0],
        [0,2,0]
    ]
       ,dtype = "float64" )

# Matrizes de rotação

rotZ = np.array(
    [
        [np.cos(theta), np.sin(theta), 0],
        [-np.sin(theta), np.cos(theta), 0],
        [0,0,1]
    ]
        ,dtype = "float64")
    

rotY = np.array(
    [
        [np.cos(theta), 0, np.sin(theta)],
        [0,1,0],
        [-np.sin(theta), 0, np.cos(theta)]
    ]
        ,dtype = "float64")


rotX = np.array(
    [
        [1,0,0],
        [0,np.cos(theta), np.sin(theta)],
        [0,-np.sin(theta), np.cos(theta)]
    ]
        ,dtype = "float64")


# ------------------- Canva ---------------------

# Frames por segundo(FPS)


# Altura e Largura da Tela
alt = 760
lar = 760

# Superfície
screen = pg.window.Window(lar, alt)


# Redimensionando superfície para que centro seja (0,0)
@screen.event
def on_resize(width, height):
    # Projeção ortográfica 2D
    screen.projection = Mat4.orthogonal_projection(
            left = -width//2,
            right = width//2,
            bottom = -height//2,
            top = height//2,
            z_near = -255,
            z_far = 255
            )



@screen.event
def on_draw():
    screen.clear()

    for ind, ponto  in enumerate(pontos):
        # Pontos 2D desenhados
        pg.shapes.Circle(x = ponto[0], y = ponto[1], radius = raio, color=(255,255,255)).draw()

        # Rotacionando em relação ao X-axis da matriz de pontos 2D
        pontos[ind,:] = rotX @ ponto

        # Pontos da projeção desenhados
        projec = Matriz_projec @ ponto
        pg.shapes.Circle(x = projec[0], y = projec[1], radius = raio, color=(255,255,255)).draw()



pg.app.run()

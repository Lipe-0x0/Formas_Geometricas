import numpy as np
import pyglet as pg
from pyglet.math import Mat4


# ----------------- Funções Complementares -----------------

def arestas(i, j, Matriz):
    a = Matriz[i, :]
    b = Matriz[j, :]

    pg.shapes.Line(x = a[0], y = a[1], x2 = b[0], y2 = b[1], color = (255,255,255)).draw()

# ------------------ Formas ---------------------

# Ângulo de rotação
theta = 0.02

# Raio dos pontos
raio = 7

# Criação dos 4 pontos no espaço 2D
pontos = np.array(
    [
        [-100,-100,50],
        [-100,100,50],
        [100,100,50],
        [100,-100,50],
        [-100,-100,-50],
        [-100,100,-50],
        [100,100,-50],
        [100,-100,-50]
     ]
       ,dtype = "float64")


# Matrizes de rotação

rotZ = np.array(
    [
        [np.cos(theta), -np.sin(theta), 0],
        [np.sin(theta), np.cos(theta), 0],
        [0,0,1]
    ]
        ,dtype = "float64")
    

rotY = np.array(
    [
        [np.cos(theta), 0, -np.sin(theta)],
        [0,1,0],
        [np.sin(theta), 0, np.cos(theta)]
    ]
        ,dtype = "float64")


rotX = np.array(
    [
        [1, 0, 0],
        [0, np.cos(theta), -np.sin(theta)],
        [0 ,np.sin(theta), np.cos(theta)]
    ]
        ,dtype = "float64")


# ------------------- Canva ---------------------

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

    for ind in range(pontos.shape[0]):
        
        # Atualizando pontos ao aplicar as 3 rotações nele
        pontos[ind, :] = rotX @ rotY @ rotZ @ pontos[ind, :]

        # Desenhando pontos na tela
        pg.shapes.Circle(x = pontos[ind, :][0], y = pontos[ind, :][1], radius = raio, color = (230,0,255)).draw()
        
        arestas(0, 1, pontos)
        arestas(1, 2, pontos)
        arestas(2, 3, pontos)
        arestas(3, 0, pontos)

        arestas(4, 5, pontos)
        arestas(5, 6, pontos)
        arestas(6, 7, pontos)
        arestas(7, 4, pontos)

        arestas(0, 4, pontos)
        arestas(1, 5, pontos)
        arestas(2, 6, pontos)
        arestas(3, 7, pontos)
    
pg.app.run()

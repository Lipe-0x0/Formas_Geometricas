from src_apoio.HelpMatriz import zeroarray, escmult, matmult
import math
import pyglet as pg
from pyglet.math import Mat4


# ----------------- Funções Complementares -----------------

def arestas(i, j, Matriz):
    a = Matriz[i]
    b = Matriz[j]

    pg.shapes.Line(x = a[0], y = a[1], x2 = b[0], y2 = b[1], color = (255,255,255)).draw()

# ------------------ Formas ---------------------

# Ângulos de rotação, cada rotação possuíra um ângulo para evitar que certos pontos fiquem fixos em torno do eixo de rotação
thetax = 0.015
thetay = 0.017
thetaz = 0.011

# Raio dos pontos
raio = 7

# Criação dos 4 pontos no espaço 2D
pontos = [
        [-100.0, -100.0, 100.0],
        [-100.0, 100.0, 100.0],
        [100.0, 100.0, 100.0],
        [100.0, -100.0, 100.0],
        [-100.0, -100.0, -100.0],
        [-100.0, 100.0, -100.0],
        [100.0, 100.0, -100.0],
        [100.0, -100.0, -100.0]
     ]

# Matriz de Perspectiva
matriz_perspec = zeroarray(8,2)


# Matrizes de rotação

#rotXYZ = [
#        [math.cos(theta)**2, -math.sin(theta)*math.cos(theta), math.sin(theta)],
#        [(math.sin(theta)**2)*math.cos(theta) + math.cos(theta)*math.sin(theta), (-math.sin(theta)**3) + (math.cos(theta)**2), -math.sin(theta)*math.cos(theta)],
#        [(-math.cos(theta)**2)*math.sin(theta) + (math.sin(theta)**2), math.cos(theta)*(math.sin(theta)**2) + math.sin(theta)*math.cos(theta), math.cos(theta)**2]
#        ]

rotZ = [
        [math.cos(thetaz), -math.sin(thetaz), 0],
        [math.sin(thetaz), math.cos(thetaz), 0],
        [0,0,1]
    ]
    

rotY = [
        [math.cos(thetay), 0, math.sin(thetay)],
        [0,1,0],
        [-math.sin(thetay), 0, math.cos(thetay)]
    ]


rotX = [
        [1, 0, 0],
        [0, math.cos(thetax), -math.sin(thetax)],
        [0 ,math.sin(thetax), math.cos(thetax)]
    ]


# ------------------- Canva ---------------------

# Altura e Largura da Tela
alt = 750
lar = 750

# Superfície
screen = pg.window.Window(fullscreen = True)


# Redimensionando superfície para que centro seja (0,0)
@screen.event
def on_resize(width, height):
    # Projeção ortográfica 2D
    screen.projection = Mat4.orthogonal_projection(
            left = -width//2,
            right = width//2,
            bottom = -height//2,
            top = height//2,
            z_near = -300,
            z_far = 300
            )



@screen.event
def on_draw():
    screen.clear()

    for ind in range(len(pontos)):

        # Atualizando pontos ao aplicar as 3 rotações nele
        pontos[ind] = matmult(rotX, pontos[ind])
        pontos[ind] = matmult(rotY, pontos[ind])
        pontos[ind] = matmult(rotZ, pontos[ind])

        # Perspectiva (Ideia geral = f / (d - z_original))
        # f = distância do view até a janela onde o objeto será projetado
        # d = distância do view até o centro do objeto
        # z_original = distância do ponto até o centro do objeto
        z = 200 / (210 - pontos[ind][2])
        
        # Atualizando x e y por meio de "z" para percepção de profundidade
        matriz_perspec[ind] = escmult(pontos[ind][0:2], z)
        
        # Desenhando pontos na tela
        pg.shapes.Circle(x = matriz_perspec[ind][0], y = matriz_perspec[ind][1], radius = raio, color = (230,0,255)).draw()

    # Desenhando arestas do Cubo
    for i in range(4):
        arestas(i, (i+1)%4, matriz_perspec)
        arestas(i+4, ((i+1)%4)+4, matriz_perspec)
        arestas(i, i+4, matriz_perspec)

pg.app.run()

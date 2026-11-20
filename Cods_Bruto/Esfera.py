import sys

# Pega o caminho do diretório atual
sys.path.insert(0, "/home/fan/Documentos/Python/PROJETOS PYTHON/Formas Geométricas")

from src_apoio.HelpMatriz import seno, cose, escmult, matmult, zeroarray
import pyglet as pg

# ----------------------- Funções Complementares ----------------------

def arestas(i, j, Matriz):
    a = Matriz[i]
    b = Matriz[j]

    pg.shapes.Line(x = a[0] + 1920/2, y = a[1] + 1080/2, x2 = b[0] + 1920/2, y2 = b[1] + 1080/2, color = (255,255,255)).draw()


# -------------------------- Formas ----------------------------------

# Ângulos de rotação, cada rotação possuíra um ângulo para evitar que certos pontos fiquem fixos em torno do eixo de rotação
thetax = 0.015
thetay = 0.015
thetaz = 0.011

# Raio dos pontos
raio = 7

# Criação dos 12 pontos no espaço 2D
pontosX = [
        [-50.0, 0, -150.0],
        [-100.0, 0, -100.0],
        [-150.0, 0, -50.0],
        [-150.0, 0, 50.0],
        [-100.0, 0, 100.0],
        [-50.0, 0, 150.0],
        [50.0, 0, 150.0],
        [100.0, 0, 100.0],
        [150.0, 0, 50.0],
        [150.0, 0, -50.0],
        [100.0, 0, -100.0],
        [50.0, 0, -150.0]
        ]

pontosY = [
        [0, -50.0, -150.0],
        [0, -100.0, -100.0],
        [0, -150.0, -50.0],
        [0, -150.0, 50.0],
        [0, -100.0, 100.0],
        [0, -50.0, 150.0],
        [0, 50.0, 150.0],
        [0, 100.0, 100.0],
        [0, 150.0, 50.0],
        [0, 150.0, -50.0],
        [0, 100.0, -100.0],
        [0, 50.0, -150.0]
        ]

# Matriz de Perspectiva
#matriz_perspecX = zeroarray(12,2)
#matriz_perspecY = zeroarray(12,2)

# Matrizes de rotação

rotXYZ = [
            [cose(thetay, 100)*cose(thetaz, 100), -cose(thetay, 100)*seno(thetaz, 100), seno(thetay, 100)],
            [seno(thetax, 100)*seno(thetay, 100)*cose(thetaz, 100) + cose(thetax, 100)*seno(thetaz, 100), -seno(thetax, 100)*seno(thetay, 100)*seno(thetaz, 100) + cose(thetax, 100)*cose(thetaz, 100), -seno(thetax, 100)*cose(thetay, 100)],
            [-cose(thetax, 100)*seno(thetay, 100)*cose(thetaz, 100) + seno(thetax, 100)*seno(thetaz, 100), cose(thetax, 100)*seno(thetay, 100)*seno(thetaz, 100) + seno(thetax, 100)*cose(thetaz, 100), cose(thetax, 100)*cose(thetay, 100)]
        ]

rotZ = [
        [cose(thetaz, 100), -seno(thetaz, 100), 0],
        [seno(thetaz, 100), cose(thetaz, 100), 0],
        [0,0,1]
    ]


rotY = [
        [cose(thetay, 100), 0, seno(thetay, 100)],
        [0,1,0],
        [-seno(thetay, 100), 0, cose(thetay, 100)]
    ]


rotX = [
        [1, 0, 0],
        [0, cose(thetax, 100), -seno(thetax, 100)],
        [0 ,seno(thetax, 100), cose(thetax, 100)]
    ]


# ----------------------------- Canva ---------------------------------

screen = pg.window.Window(fullscreen = True)


@ screen.event
def on_draw():
    screen.clear()

    for ind in range(len(pontosX)):

        pontosX[ind] = matmult(rotX, pontosX[ind])
        pontosX[ind] = matmult(rotZ, pontosX[ind])

        pontosY[ind] = matmult(rotY, pontosY[ind])
        pontosY[ind] = matmult(rotZ, pontosY[ind])

        #z1 = 200 / (200 - pontosX[ind][2])
        #z2 = 200 / (200 - pontosY[ind][2])

        #matriz_perspecX[ind] = escmult(pontosX[ind][0:2], z1)
        #matriz_perspecY[ind] = escmult(pontosY[ind][0:2], z2)

        pg.shapes.Circle(x = pontosX[ind][0] + 1920/2, y = pontosX[ind][1] + 1080/2, 
                         color = (230, 0, 255), radius = raio).draw()
        pg.shapes.Circle(x = pontosY[ind][0] + 1920/2, y = pontosY[ind][1] + 1080/2, 
                         color = (230, 0, 255), radius = raio).draw()

        #pg.shapes.Line(x = 0, y = 1080/2, x2 = 1920, y2 = 1080/2, color = (255,255,255)).draw() # Linha Horizontal
        #pg.shapes.Line(x = 1920/2, y = 0, x2 = 1920/2, y2 = 1080, color = (255,255,255)).draw() # Linha Vertical

    for i in range(len(pontosX)):
        if i != (len(pontosX)-1):
            arestas(i, i+1, pontosX)
            arestas(i, i+1, pontosY)

        arestas(0, len(pontosX)-1, pontosX)
        arestas(0, len(pontosY)-1, pontosY)

pg.app.run()

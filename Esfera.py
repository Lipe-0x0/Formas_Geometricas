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
thetay = 0.017
thetaz = 0.011

# Raio dos pontos
raio = 7

# Criação dos 4 pontos no espaço 2D
pontos = [
        [-100.0, 0, 100.0],
        [-100.0, 0, -100.0],
        [100.0, 0, 100.0],
        [100.0, 0, -100.0]
        ]

# Matriz de Perspectiva
matriz_perspec = zeroarray(4,2)


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

    for ind in range(len(pontos)):

        pontos[ind] = matmult(rotX, pontos[ind])

        z = 200 / (200 - pontos[ind][2])

        matriz_perspec[ind] = escmult(pontos[ind][0:2], z)

        pg.shapes.Circle(x = matriz_perspec[ind][0] + 1920/2, y = matriz_perspec[ind][1] + 1080/2, 
                         color = (230, 0, 255), radius = raio).draw()

    for i in range(2):
        print(i)
        arestas(i, (i+1)%2, matriz_perspec)
        arestas(i+2, ((i+1)%2)+2, matriz_perspec)
        arestas(i, i+2, matriz_perspec)

pg.app.run()

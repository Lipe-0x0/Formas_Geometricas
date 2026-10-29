from src_apoio.HelpMatriz import zeroarray, escmult, matmult, seno, cose
import pyglet as pg



# ----------------- Funções Complementares -------------------

def arestas(i, j, matriz):
    A = matriz[i]
    B = matriz[j]

    pg.shapes.Line(A[0] + 1920/2, A[1] + 1080/2, B[0] + 1920/2, B[1] + 1080/2, color = (255, 255, 255)).draw()

# ----------------- Formas --------------------

# Ângulos de rotação, um ângulo para eixo afim de evitar a fixação de pontos em torno do eixo de rotação final
thetax = 0.011
thetay = 0.015
thetaz = 0.02


# Raio dos pontos
raio = 7

# Criação dos pontos que formam a pirâmide base triangular
pontos = [
            [-200.0, -100.0, 75.0],
            [200.0, -100.0, 75.0],
            [0.0, -100.0, -125.0],
            [0.0, 300.0, -25.0]
        ]


# Matriz de Perspectiva
matriz_perspec = zeroarray(4,2)

# Matrizes de Rotação
rotXYZ = [
            [cose(thetay, 100)*cose(thetaz, 100), -cose(thetay, 100)*seno(thetaz, 100), seno(thetay, 100)],
            [seno(thetax, 100)*seno(thetay, 100)*cose(thetaz, 100) + cose(thetax, 100)*seno(thetaz, 100), -seno(thetax, 100)*seno(thetay, 100)*seno(thetaz, 100) + cose(thetax, 100)*cose(thetaz, 100), -seno(thetax, 100)*cose(thetay, 100)],
            [-cose(thetax, 100)*seno(thetay, 100)*cose(thetaz, 100) + seno(thetax, 100)*seno(thetaz, 100), cose(thetax, 100)*seno(thetay, 100)*seno(thetaz, 100) + seno(thetax, 100)*cose(thetaz, 100), cose(thetax, 100)*cose(thetay, 100)]
        ] 

rotX = [
            [1, 0, 0],
            [0, cose(thetax, 100), -seno(thetax, 100)],
            [0, seno(thetax, 100), cose(thetax, 100)]
        ]

rotY = [
            [cose(thetay, 100), 0, seno(thetay, 100)],
            [0, 1, 0],
            [-seno(thetay, 100), 0, cose(thetay, 100)]
        ]

rotZ = [
            [cose(thetaz, 100), -seno(thetaz, 100), 0],
            [seno(thetaz, 100), cose(thetaz, 100), 0],
            [0, 0, 1]
        ]

# --------------------- Criação da Superfície -------------------

# Superfície
screen = pg.window.Window(fullscreen = True)


# Projetando e Renderizando na superfície
@screen.event
def on_draw():
    screen.clear()
    
    for ind in range(len(pontos)):

        # Rotacionando
        pontos[ind] = matmult(rotXYZ, pontos[ind])

        # Projeção em perspectiva
        z = 900 / (900 - pontos[ind][2])
        
        # Atualização de x e y a partir de "z" para projeção de profundidade
        matriz_perspec[ind] = escmult(pontos[ind][0:2], z)

        # Renderizando cada ponto
        pg.shapes.Circle(x = matriz_perspec[ind][0] + 1920/2, y = matriz_perspec[ind][1] + 1080/2, radius = raio, color = (230,0,255)).draw()

    # Conectando vértices
    for i in range(3):
        arestas(i, (i+1)%3, matriz_perspec)
        arestas(i, 3, matriz_perspec)



pg.app.run()

import sys

# Pega o caminho do diretório atual
sys.path.insert(0, "/home/fan/Documentos/Python/PROJETOS PYTHON/Formas Geométricas")


from src_apoio.HelpMatriz import zeroarray, escmult, matmult, cose, seno
import pyglet as pg


# ----------------- Funções Complementares -----------------

def arestas(i, j, Matriz):
    a = Matriz[i]
    b = Matriz[j]

    pg.shapes.Line(x = a[0] + 1920/2, y = a[1] + 1080/2, x2 = b[0] + 1920/2, y2 = b[1] + 1080/2, color = (255,255,255)).draw()

# ------------------ Formas ---------------------

# Ângulos de rotação, cada rotação possuíra um ângulo para evitar que certos pontos fiquem fixos em torno do eixo de rotação
thetax = 0.015
thetay = 0.017
thetaz = 0.011

# Raio dos pontos
raio = 7

# Criação dos 8 pontos no espaço 2D
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


# ------------------- Canva ---------------------

# Superfície
screen = pg.window.Window(fullscreen = True)


@screen.event
def on_draw():
    screen.clear()

    for ind in range(len(pontos)):

        # Atualizando pontos ao aplicar as 3 rotações nele
        pontos[ind] = matmult(rotXYZ, pontos[ind])

        # Perspectiva (Ideia geral = f / (d - z_original))
        # f = distância do objeto até a janela onde ele será projetado
        # d = distância do view até o centro do objeto
        # z_original = distância do ponto até o centro do objeto

        # Critério de escolha: d > R, onde R é o maior môdulo dos vetores(vértices)  

        z = 300 / (300 - pontos[ind][2])
        
        # Atualizando x e y por meio de "z" para percepção de profundidade
        matriz_perspec[ind] = escmult(pontos[ind][0:2], z)
        
        # Desenhando pontos na tela
        pg.shapes.Circle(x = matriz_perspec[ind][0] + 1920/2, y = matriz_perspec[ind][1] + 1080/2, radius = raio, color = (230,0,255)).draw()

    # Desenhando arestas do Cubo
    for i in range(4):
        arestas(i, (i+1)%4, matriz_perspec)
        arestas(i+4, ((i+1)%4)+4, matriz_perspec)
        arestas(i, i+4, matriz_perspec)

pg.app.run()

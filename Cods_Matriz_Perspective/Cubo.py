import sys

# Pegando path do diretório atual para código saber onde pacotes e funções estão
sys.path.insert(0, "/home/fan/Documentos/Python/PROJETOS PYTHON/Formas Geométricas/")

from src_apoio.HelpMatriz import cose, seno, matmult, escmult, zeroarray
import pyglet as pg

# ---------------------- Funções Complementares  -----------------------

def arestas(i, j, matriz):
    a = matriz[i]
    b = matriz[j]

    pg.shapes.Line(x = a[0] + 1920/2, y = a[1] + 1080/2, x2 = b[0] + 1920/2, y2 = b[1] + 1080/2, 
                   color = (255,255,255)).draw()

# ---------------------- Formas ----------------------

# Ângulos de rotação, cada rotação possuíra um ângulo para evitar que certos pontos fiquem fixos em torno do eixo de rotação
thetax = 0.015
thetay = 0.017
thetaz = 0.011

# Raio dos pontos
raio = 7

# Criação dos 8 pontos no espaço 2D
pontos = [
        [-100.0, -100.0, 100.0, 1],
        [-100.0, 100.0, 100.0, 1],
        [100.0, 100.0, 100.0, 1],
        [100.0, -100.0, 100.0, 1],
        [-100.0, -100.0, -100.0, 1],
        [-100.0, 100.0, -100.0, 1],
        [100.0, 100.0, -100.0, 1],
        [100.0, -100.0, -100.0, 1]
     ]


# Matriz de Perspectiva
matriz_perspec = zeroarray(8,4)


# Matrizes de rotação

rotXYZ = [
            [cose(thetay, 100)*cose(thetaz, 100), -cose(thetay, 100)*seno(thetaz, 100), seno(thetay, 100), 0],
            [seno(thetax, 100)*seno(thetay, 100)*cose(thetaz, 100) + cose(thetax, 100)*seno(thetaz, 100), -seno(thetax, 100)*seno(thetay, 100)*seno(thetaz, 100) + cose(thetax, 100)*cose(thetaz, 100), -seno(thetax, 100)*cose(thetay, 100), 0],
            [-cose(thetax, 100)*seno(thetay, 100)*cose(thetaz, 100) + seno(thetax, 100)*seno(thetaz, 100), cose(thetax, 100)*seno(thetay, 100)*seno(thetaz, 100) + seno(thetax, 100)*cose(thetaz, 100), cose(thetax, 100)*cose(thetay, 100), 0],
            [0, 0, 0, 1]
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


# Matriz de Projeção Perspectiva
# Onde n = near(próximo), f = far(distante), d = distância do olho até o objeto
n = 300
# f = 300, como a terceira linha da multiplicação não é utilizada(até pq não estou fazendo um buffer) então achei melhor zerar
d = 250 # Critério de escolha: d > R, onde R é o maior môdulo dos vetores(vértices)

PP = [
        [n, 0, 0, 0],
        [0, n, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 1, 0]
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

        # Multiplicando matriz de projeção por cada ponto após rotação 
        matriz_perspec[ind] = matmult(PP, pontos[ind])
        # Passo final: Divisão do último índice "d - w" por todos os outros da coluna, em que "w" recebe o valor de z_objeto
        # x' = n*x/(d-z_objeto); y' = n*y/(d-z_objeto)
        matriz_perspec[ind] = escmult(matriz_perspec[ind], 1/(d - matriz_perspec[ind][3]))

        # Desenhando pontos na tela
        pg.shapes.Circle(x = matriz_perspec[ind][0] + 1920/2, y = matriz_perspec[ind][1] + 1080/2, radius = raio, color = (230,0,255)).draw()

    # Desenhando arestas do Cubo
    for i in range(4):
        arestas(i, (i+1)%4, matriz_perspec)
        arestas(i+4, ((i+1)%4)+4, matriz_perspec)
        arestas(i, i+4, matriz_perspec)

pg.app.run()


from HelpMatriz.py import seno, cose, escmult, matmult, zeroarray
import pyglet as pg

# ----------------------- Funções Complementares ----------------------
def arestas(i, j, Matriz):
	a = Matriz[i]
	b = Matriz[j]

pg.shapes.Line(a[0] + 1920/2, a[1] + 1080/2, b[0] + 1920/2, b[1] + 1080/2,
color = (255,255,255)).draw()

# -------------------------- Formas ----------------------------------


# ----------------------------- Canva ---------------------------------


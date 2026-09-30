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
            [-100, -100, 100],
            [100, -100, 100],
            [],
            []
        ]



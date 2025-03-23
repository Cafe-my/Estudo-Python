# HOW TO IMPORT MODULES?

import platform                         # importa tds as funcoes
# from platform import python_version     importa apenas uma funcao (python_version)

print(dir(platform))                    # permite consultar todas as funcoes


# IMPORTANDO MAIS DE UM MODULO
import platform, string, os


# MUDANDO A IDENTIFICACAO DA FUNCAO (USO DO 'AS')
from platform import python_version as pv   
print(pv())


# CONSULTAR MODULOS DISPONIVEIS:
# https://docs.python.org/3/py-modindex.html
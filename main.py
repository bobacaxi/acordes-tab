import numpy as np
from helpers import *

tamanho_braco = 12

resposta = 's'
while resposta in ['s']:
    acorde = Acorde()
    tab = Tablatura(tamanho_braco)
    tab.marcar(acorde, tamanho_braco)
    render = Render(tab.tab, acorde, tamanho_braco)
    resposta = input('\nDeseja continuar? [s/n] ').lower()

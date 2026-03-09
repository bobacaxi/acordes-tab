# RESUMO DO CODIGO
#
# 1 - definir dicionários de acordes, tom, cromatica e alteracoes
# 2 - regras
# 3 - perguntar acorde
# 4 - verificar se tem numero, parentesis ou barra
#
# 5 - devolver sempre tom e escala do tom com as alterações
#
# 6 - desenhar o braço
# 7 - transformar o braço em uma tabela --> 0, 1, 2, 3, 4, 5
# 8 - renderizar o braço e printar



import numpy as np
# region Dicionários

# nessa definicao da cromatica, os indices 0-11 representam as notas
# num --> notas => escala_cromatica[num] || notas --> num => escala.cromatica.index(notas)
escala_cromatica = 'C C# D D# E F F# G G# A A# B'.split(' ')

triade_maior = [0, 4, 7]
triade_menor = [0, 3, 7]

def acorde_natural(tom):
    eh_menor = True if 'm' in tom else False
    if eh_menor:
        num = escala_cromatica.index(tom.strip('m'))
        return [escala_cromatica[(i + num) % 12] for i in triade_menor]
    else:
        num = escala_cromatica.index(tom)
        return [escala_cromatica[(i + num) % 12] for i in triade_maior]

alteracoes = {
    1: '9-',
    2: '9',
    3: '9+',
    5: '4',
    6: '5-',
    8: '5+',
    9: '6',
    10: '7',
    11: '7+'
}

inv_alteracoes = {v: k for k, v in alteracoes.items()}

# endregion

#region Regras
regras_rascunho = ('\n  REGRAS\n'
    '\n    apenas sustenidos # - não tem bemol'
    '\n    pode Maior e Menor'
    '\n    a 1a alteração é idêntica às listados'
    '\n    a 2a alteração é separada por parêntesis'
    '\n    a inversão é separada por uma barra\n'
    '\n    Lista de alterações: \n'
    '\n    9-, 9, 9+, 4, 5-, 5+, 6, 7, 7+\n'
    '\n    a 5- e a 5+ não são extensões, a 5 é substituída\n')

linhas_regras = regras_rascunho.split('\n')

tamanho_linhas = [len(linhas_regras[_]) for _ in range(len(linhas_regras))]

tamanho_max_linhas = max(tamanho_linhas[:7])

espaco = 8

regras = [
    ['\n' + (tamanho_max_linhas + 9)* '='],
    [(tamanho_max_linhas//2)*' ', 'REGRAS\n'],
    [(tamanho_max_linhas + 9)* '_'],
    ['I   -  apenas sustenidos # - não tem bemol', (tamanho_max_linhas - tamanho_linhas[3] + espaco)*' ','ex. C#'],
    ['II  -  pode Maior e Menor', (tamanho_max_linhas - tamanho_linhas[4] + espaco)*' ','ex. C e Cm'],
    ['III -  a 1a alteração é idêntica às listadas', (tamanho_max_linhas - tamanho_linhas[5] + espaco)*' ', 'ex. C9-'],
    ['IV  -  a 2a alteração é separada por parêntesis', (tamanho_max_linhas - tamanho_linhas[6] + espaco)*' ', 'ex. C7(9-)'],
    ['V   -  a inversão é separada por uma barra', (tamanho_max_linhas - tamanho_linhas[7] + espaco)*' ', 'ex. C/G#', '\n'],
    ['  --> 5- e 5+ não são extensões, a 5 é substituída'],
    [(tamanho_max_linhas + 9)* '_'],
    ['  --- Lista de alterações:'],
    ['          9-, 9, 9+, 4, 5-, 5+, 6, 7, 7+'],
    [(tamanho_max_linhas + 9)* '=', '\n']]

#endregion

class Acorde:
    def __init__(self):
        for row in regras:
            print("".join(row))
        self.acorde = input('\n Escreva um acorde: \n\n --> ')
        self.tom = ''
        self.harmonico = []
        self.acorde_natural = ''
        self.alt_1 = ['', '']
        self.alt_2 = ['', '']
        self.inv = ''
        self.identificar(self.acorde)

    def identificar(self, entrada):
        self.tem_num = False
        self.tem_par = False
        self.tem_barra = False
        idx_num = []
        idx_par = []
        idx_barra = []

        for item in entrada:
            if item.isdigit():
                self.tem_num = True
                idx_num.append(entrada.index(item))

            elif item == '(':
                self.tem_par = True
                idx_par.append(entrada.index(item))

            elif item == '/':
                self.tem_barra = True
                print(item)
                idx_barra.append(entrada.index(item))

        # region CASO A CASO
        if self.tem_num == False and self.tem_barra == False:
            self.acorde_natural = entrada
            self.tom = acorde_natural(entrada)[0]
            self.harmonico = acorde_natural(self.acorde_natural)

        elif self.tem_num == False and self.tem_barra == True:

            self.acorde_natural = "".join(entrada[:idx_barra[0]])
            self.tom = acorde_natural(self.acorde_natural)[0]

            self.inv = "".join(entrada[(idx_barra[0] + 1):])

            self.harmonico = acorde_natural(self.acorde_natural)
            self.harmonico.append(self.inv)

        elif self.tem_num == True and self.tem_par == False and self.tem_barra == False:

            self.acorde_natural = "".join(entrada[:idx_num[0]])
            self.tom = acorde_natural(self.acorde_natural)[0]

            self.alt_1[0] = "".join(entrada[idx_num[0]:])
            alt_1_id = inv_alteracoes[self.alt_1[0]]
            self.alt_1[1] = escala_cromatica[ (alt_1_id + escala_cromatica.index(self.tom)) % 12 ]

            self.harmonico = acorde_natural(self.acorde_natural)
            self.harmonico.append(self.alt_1[1])

        elif self.tem_num == True and self.tem_par == True and self.tem_barra == False:

            self.acorde_natural = "".join(entrada[:idx_num[0]])
            self.tom = acorde_natural(self.acorde_natural)[0]

            self.alt_1[0] = "".join(entrada[idx_num[0]:idx_par[0]])
            alt_1_id = inv_alteracoes[self.alt_1[0]]
            self.alt_1[1] = escala_cromatica[ (alt_1_id + escala_cromatica.index(self.tom)) % 12 ]

            self.alt_2[0] = "".join(entrada[(1+idx_par[0]):-1])
            alt_2_id = inv_alteracoes[self.alt_2[0]]
            self.alt_2[1] = escala_cromatica[ (alt_2_id + escala_cromatica.index(self.tom)) % 12 ]

            self.harmonico = acorde_natural(self.acorde_natural)
            self.harmonico.append(self.alt_1[1])
            self.harmonico.append(self.alt_2[1])

        elif self.tem_num == True and self.tem_par == False and self.tem_barra == True:

            self.acorde_natural = "".join(entrada[:idx_num[0]])
            self.tom = acorde_natural(self.acorde_natural)[0]

            self.alt_1[0] = "".join(entrada[idx_num[0]:idx_barra[0]])
            alt_1_id = inv_alteracoes[self.alt_1[0]]
            self.alt_1[1] = escala_cromatica[ (alt_1_id + escala_cromatica.index(self.tom)) % 12 ]

            self.inv = "".join(entrada[(idx_barra[0] + 1):])

            self.harmonico = acorde_natural(self.acorde_natural)
            self.harmonico.append(self.alt_1[1])
            if self.inv not in acorde_natural(self.acorde_natural):
                self.harmonico.append(self.inv)

        elif self.tem_num == True and self.tem_par == True and self.tem_barra == True:

            self.acorde_natural = "".join(entrada[:idx_num[0]])
            self.tom = acorde_natural(self.acorde_natural)[0]

            self.alt_1[0] = "".join(entrada[idx_num[0]:idx_par[0]])
            alt_1_id = inv_alteracoes[self.alt_1[0]]
            self.alt_1[1] = escala_cromatica[ (alt_1_id + escala_cromatica.index(self.tom)) % 12 ]

            self.alt_2[0] = "".join(entrada[(1+idx_par[0]):idx_barra[0]-1])
            alt_2_id = inv_alteracoes[self.alt_2[0]]
            self.alt_2[1] = escala_cromatica[ (alt_2_id + escala_cromatica.index(self.tom)) % 12 ]

            self.inv = "".join(entrada[(idx_barra[0] + 1):])

            self.harmonico = acorde_natural(self.acorde_natural)
            self.harmonico.append(self.alt_1[1])
            self.harmonico.append(self.alt_2[1])
            if self.inv not in self.harmonico:
             self.harmonico.append(self.inv)

        if self.alt_1[0] in ['5-', '5+'] or self.alt_2[0] in ['5-', '5+']:
            self.harmonico.pop(2)

        # endregion

class Tablatura:
    def __init__(self, tamanho_braco=12):
        cordas = [3, 10, 6, 1, 8, 3]
        self.braco = [self.corda_num(x, tamanho_braco) for x in cordas]
        self.tab = np.zeros((6, tamanho_braco+2), int)

    def corda_num(self, x, tamanho_braco=12):
        return [escala_cromatica[(i + x) % 12] for i in range(tamanho_braco+2)]

    def marcar(self, acorde, tamanho_braco=12):
        for i in range(6):
            for j in range(tamanho_braco +2):
                if self.braco[i][j] == acorde.tom:
                    self.tab[i][j] = 2
                elif acorde.alt_1[1] != '' and self.braco[i][j] == acorde.alt_1[1]:
                    self.tab[i][j] = 3
                elif acorde.alt_2[1] != '' and self.braco[i][j] == acorde.alt_2[1]:
                    self.tab[i][j] = 4
                elif acorde.inv != '' and self.braco[i][j] == acorde.inv:
                    self.tab[i][j] = 5
                elif self.braco[i][j] in acorde.harmonico:
                    self.tab[i][j] = 1
                else:
                    self.tab[i][j] = 0

        return self.tab

class Render:

    def __init__(self, tab, acorde, tamanho_braco=12):
        simbolos = {0: "—", 1: "○", 2: "◉", 3: "▲", 4: "■", 5: "i"}
        self.tab_proj = np.vectorize(simbolos.get)(tab)
        self.tab = np.empty((6, 2 * tamanho_braco + 4), dtype=str)

        self.tab_rep(acorde, tamanho_braco)

        print("\nCampo Harmônico: ", " ".join(acorde.harmonico))

    def contagem_casas(self, tamanho_braco=12):
        # adicionar contagem de casas
        contagem = [None] * (2 * tamanho_braco + 4)

        for i in range((2 * tamanho_braco + 4) // 2):
            contagem[2 * i] = i
            if 2 * i + 1 < 2 * tamanho_braco + 4:
                contagem[2 * i + 1] = " "

            # mostrar apenas casas 0, 3, 5, 7, 9, 12, 15, 17
        for i in range((2 * tamanho_braco + 4) // 2):
            if contagem[2 * i] not in [3, 5, 7, 9, 12, 15, 17, 19]:
                contagem[2 * i] = " "

            # ajusta espaços da contagem / alinhar com tab
        contagem[0] = '   '

        contagem_render = '   '

        for _ in contagem:
            contagem_render += str(_)
            if _ == " ":
                contagem_render += " "
            elif isinstance(_, int) and _ < 10:
                contagem_render += " "

        print(contagem_render)

    def linhas(self, cima, tamanho_braco=12):
        simb = '\uFE47' if cima else '\uFE48'

        # adicionar linha
        linha = [' '] * (2 * tamanho_braco + 4)

        for i in range((2 * tamanho_braco + 4) // 2):
            linha[2 * i] = simb
            if 2 * i + 1 < 2 * tamanho_braco + 4:
                linha[2 * i + 1] = " "

        #ajeitar espaços
        linha[0] = '   '

        linha_render = '   '

        for _ in linha:
            linha_render += str(_)
            if _ == " ":
                linha_render += " "

        print(linha_render)

    def tab_rep(self, acorde, tamanho_braco=12):
        # espaços e cordas
        for i in range(6):
            self.tab[i, ::2] = self.tab_proj[i, :]

        self.tab[:6, 0] = ' '
        self.tab[:6, 1::2] = "|"
        self.tab[:6, 1] = ["e", "B", "G", "D", "A", "E"]

        for i in range(6):
            if self.tab[i][2] == "\u2014":
                self.tab[i][2] = '\u271D'

        # print
        print("")
        if acorde.tem_num == True and acorde.tem_par == True and acorde.tem_barra == True:
            print('Legenda:', f"\u25B2 =  {acorde.alt_1[0]} ({acorde.alt_1[1]})", "/", f"\u25A0 = {acorde.alt_2[0]} ({acorde.alt_2[1]})", "/", f"i = inversão ({acorde.inv})")
        if acorde.tem_num == True and acorde.tem_par == True and acorde.tem_barra == False:
            print('Legenda:', f"\u25B2 =  {acorde.alt_1[0]} ({acorde.alt_1[1]})", "/", f"\u25A0 = {acorde.alt_2[0]} ({acorde.alt_2[1]})")
        if acorde.tem_num == True and acorde.tem_par == False and acorde.tem_barra == True:
            print('Legenda:', f"\u25B2 =  {acorde.alt_1[0]} ({acorde.alt_1[1]})", "/", f"i = inversão ({acorde.inv})")
        if acorde.tem_num == False and acorde.tem_par == False and acorde.tem_barra == True:
            print('Legenda:', f"i = inversão ({acorde.inv})")
        if acorde.tem_num == True and acorde.tem_par == False and acorde.tem_barra == False:
            print('Legenda:', f"\u25B2 = {acorde.alt_1[0]} ({acorde.alt_1[1]})")
        print("")

        self.contagem_casas(tamanho_braco)
        self.linhas(True, tamanho_braco)

        for row in self.tab[:6]:
            print(" ".join(row))

        self.linhas(False, tamanho_braco)
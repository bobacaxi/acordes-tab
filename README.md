# acordes-tab
Um código python que recebe um acorde no formato "Cm7(9)" como input e
devolve uma tablatura marcando o campo harmônico do acorde no braço do violão. Utiliza apenas
um pouco de NumPy, um dia vai ser adaptado apenas com pacotes built-in.

# Como usar

Para usar basta rodar o arquivo main.py em uma IDE ou terminal, que aparecerá uma série de regras 
de formatação para o acorde ser inserido:<br/>
<br/>

REGRAS
_____________________________________________________
I   -  apenas sustenidos # - não tem bemol             ex. C#<br/>
II  -  pode Maior e Menor                              ex. C e Cm<br/>
III -  a 1a alteração é idêntica às listadas           ex. C9-<br/>
IV  -  a 2a alteração é separada por parêntesis        ex. C7(9-)<br/>
V   -  a inversão é separada por uma barra             ex. C/G#<br/>

  --> 5- e 5+ não são extensões, a 5 é substituída
_____________________________________________________
  --- Lista de alterações:
          9-, 9, 9+, 4, 5-, 5+, 6, 7, 7+
_____________________________________________________
<br/>
Assim, basta escrever um acorde e o resultado será uma tablatura com as marcações adequadas.
É possível também alterar o tamanho do braço do violão mostrado, que está no padrão tamanho_braco = 12.


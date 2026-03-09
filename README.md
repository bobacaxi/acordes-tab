# acordes-tab
Um código python que recebe um acorde no formato "Cm7(9)" como input e
devolve uma tablatura marcando o campo harmônico do acorde no braço do violão. Utiliza apenas
um pouco de NumPy, um dia vai ser adaptado apenas com pacotes built-in.

# Como usar

Para usar, primeiro é necessário baixar os arquivos "main.py" e "helpers.py", dentro de uma mesma pasta. Se você não tem
NumPy, é muito fácil de instalar, basta abrir um console python 3 digitar "pip install numpy". 
Finalmente, basta rodar o arquivo main.py em uma IDE ou terminal, que aparecerão uma série de regras 
de formatação para o acorde:<br/>
<br/>

REGRAS
_____________________________________________________
1. apenas sustenidos # - não tem bemol             [ex. C#] <br/>
2. pode Maior e Menor                              [ex. C e Cm] <br/>
3. a 1a alteração é idêntica às listadas           [ex. C9-]<br/>
4. a 2a alteração é separada por parêntesis        [ex. C7(9-)]<br/>
5. a inversão é separada por uma barra             [ex. C/G#]<br/>

  --> 5- e 5+ não são extensões, a 5 é substituída
_____________________________________________________
  --- Lista de alterações:
          9-, 9, 9+, 4, 5-, 5+, 6, 7, 7+
_____________________________________________________
<br/>
Assim, basta escrever um acorde e o resultado será uma tablatura com as marcações adequadas.
É possível também alterar o tamanho do braço do violão mostrado, que está no padrão tamanho_braco = 12.

# Helpers

O arquivo main.py executa todas as operações, no entanto é o arquivo helpers.py que define os objetos.
Há 5 seções no arquivo:<br/>

1. Dicionários (cromática, tríades e alterações)
2. Regras (formatação dos acordes)
3. classe Acorde (identifica o tom e o campo harmônico do acorde)
4. classe Tablatura (cria uma tabela do braço e marca o campo harmônico em números)
5. classe Render (representa e alinha a tabela, adiciona contagem e legenda)

Ainda é praticamente tudo feito manualmente, isso é, não há muito automatização do código
para eficiência, foi feito pela tentativa e erro --- mas funciona! Fique à vontade para conferir e
melhorar o código.
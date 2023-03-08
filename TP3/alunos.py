from lark import Lark
from lark.tree import pydot__tree_to_png
from lark import Transformer
from lark import Discard



## Primeiro precisamos da GIC
grammar = '''
start: Turma+
Turma: TURMA LETRA NEWLINE (Aluno NEWLINE)* AlunoFinal
Aluno: NOME PE NOTA (VIR NOTA)* PF PV NEWLINE
AlunoFinal: NOME PE NOTA (VIR NOTA)* PF PF NEWLINE
TURMA: "TURMA"
LETRA: "A".."Z"
NEWLINE: "\n"
NOME: /\w+/
PE: "("
PF: ")"
NOTA: /\d+/
PV: ";"

%import common.WS
%ignore WS
'''


class MyTransformer(Transformer):

    def start(self, start):
        print(start)

    def Turma(self, turma):
        print(turma)
    
    def Aluno(self, aluno):
        print(aluno)

    def TURMA(self, turma):
        print(turma)
    
    def LETRA(self, letra):
        print(letra)

    def NEWLINE(self, nl):
        print(nl)

    def NOME(self, nome):
        print(nome)

    def PE(self, pe):
        print(pe)

    def PF(self,pf):
        print(pf)
        return Discard

    def NOTA(self, numero):
        print(numero)

    def PV(self, pv):
        print(pv)

    def PF(self, pf):
        print(pf)

    pass


frase = open("exemplo.txt", "r").read()
print(frase)
p = Lark(grammar)

parse_tree = p.parse(frase)
print(parse_tree.pretty())

data = MyTransformer().transform(parse_tree)
print(data)
from lark import Lark
from lark.tree import pydot__tree_to_png
from lark import Transformer
from lark import Discard
from html import gen_html



# Primeiro precisamos da GIC
grammar = r'''
start : turma+
turma : TURMA ESPACO LETRA EOL aluno+ alunof
aluno : NOME ESPACO PE NOTA (VIR ESPACO? NOTA)* PF PV EOL
alunof : NOME ESPACO PE NOTA (VIR ESPACO? NOTA)* PF PFINAL EOL
TURMA : "TURMA"
LETRA : "A".."Z"
VIR : ","
NOME : /\w+/
PE : "("
PF : ")"
PFINAL : "."
NOTA : /\d+/
PV : ";"
EOL : /\n/
ESPACO : " "
'''



class MyTransformer(Transformer):
    alunos = {}
    notas = {}
    biggest_notas = 0

    def pop_notas(self, aluno):
        nome = aluno[0]
        notas = aluno[1:]
        for nota in notas:
            if nota in self.notas:
                nomes = self.notas[nota]
                nomes.add(nome)
                self.notas[nota] = nomes
            else:
                self.notas[nota] = {nome}

    def start(self, start):   
        #print(self.alunos)    
        #print(self.notas) 
        print(start)
        gen_html(list(start), self.biggest_notas)
        return start

    def turma(self, turma):
        #print(turma)
        return turma

    def aluno(self, aluno):
        #print(aluno)
        notas = aluno[1:]
        media = sum(notas)/len(notas)
        if len(notas) > self.biggest_notas:
            self.biggest_notas = len(notas)
        self.alunos[aluno[0]] = media
        self.pop_notas(aluno)
        return aluno

    def alunof(self, aluno): 
        notas = aluno[1:]
        media = sum(notas)/len(notas)
        if len(notas) > self.biggest_notas:
            self.biggest_notas = len(notas)
        self.alunos[aluno[0]] = media
        self.pop_notas(aluno)
        return aluno

    def TURMA(self, turma):
        return Discard
    
    def LETRA(self, letra):
        return Discard

    def NEWLINE(self, nl):
        return Discard

    def NOME(self, nome):
        #print(nome)
        return str(nome)

    def VIR(self, vir):
        return Discard

    def PE(self, pe):
        return Discard

    def PF(self,pf):
        return Discard

    def NOTA(self, numero):
        #print(numero)
        return int(numero)

    def PV(self, pv):
        return Discard

    def PF(self, pf):
        return Discard

    def ESPACO(self, espaco):
        return Discard

    def EOL(self, eol):
        return Discard

    def PFINAL(self, pfinal):
        return Discard

    pass


frase = open("teste.txt", "r").read()
#print(frase)
p = Lark(grammar)


parse_tree = p.parse(frase)
#print(parse_tree.pretty())

data = MyTransformer().transform(parse_tree)
#print(data)
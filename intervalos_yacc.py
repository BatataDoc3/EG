# ------------------------------------------------------------
# TPC1 : Intervalos (definição sintática)
#  + [100,200][3,12]
#  + [-4,-2][1,2][3,5][7,10][12,14][15,19]
#  - [19,15][12,6][-1,-3]
#  - [1000,200][30,12]
# ------------------------------------------------------------
import sys
import ply.yacc as yacc
from intervalos_lex import tokens

lis = []


def verify_intervals_asc(intervals):
    lowest = intervals[0][0] - 1
    for interval in intervals:
        if interval[1] < interval[0]:
            parser.success = False
            return
        if interval[0] <= lowest:
            parser.success = False
            return
        lowest = interval[1]

def verify_intervals_desc(intervals):
    highest = intervals[0][0] + 1
    for interval in intervals:
        if interval[1] > interval[0]:
            parser.success = False
            return
        if interval[0] >= highest:
            parser.success = False
            return
        highest = interval[1]

def biggest_interval(intervals, signal):
    biggest = 0
    for interval in intervals:
        if signal == 1:
            if interval[1]-interval[0] > biggest:
                biggest = interval[1]-interval[0]
        else: 
            if interval[0]-interval[1] > biggest:
                biggest = interval[0]-interval[1]
    return biggest

# The set of syntatic rules
def p_sequencia(p):
    "sequencia : sentido intervalos"
    signal = 1
    if p[1] == "+":
        verify_intervals_asc(p[2])
    else:
        signal = -1
        verify_intervals_desc(p[2])
    if parser.success == False:
        print("Frase inválida")
    else:
        print(p[2])
        print("Número de intervalos :" + str(len(p[2])))
        for i, interval in enumerate(p[2]):
            print("\tcomprimento do intervalo " + str(i + 1) + ": " + str((interval[1]-interval[0]) * signal))
        print("comprimento do maior intervalo: " + str(biggest_interval(p[2], signal)))
        print("Amplitude da sequência: " + str((p[2][-1][1] - p[2][0][0]) * signal))

    global lis
    lis = []

def p_sentidoA(p):
    "sentido : '+'"
    p[0] = p[1]

def p_sentidoD(p):
    "sentido : '-'"
    p[0] = p[1]

def p_intervalos_intervalo(p):
    "intervalos : intervalo"
    global lis
    lis.append(p[1])
    p[0] = lis

def p_intervalos_intervalos(p):
    "intervalos : intervalos intervalo"
    #print(p[1])
    #print(p[2])
    p[1].append(p[2])
    p[0] = p[1]
    #print(p[0])

def p_intervalo(p):
    "intervalo : '[' NUM ',' NUM ']'"
    p[0] = [p[2], p[4]]

# Syntatic Error handling rule
def p_error(p):
    print('Syntax error: ', p)
    parser.success = False

# Build the parser
parser = yacc.yacc()

# Start parsing the input text
for line in sys.stdin:
    parser.success = True
    parser.flag = True
    parser.last = 0
    parser.parse(line)

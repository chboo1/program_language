from sys import stdin, stdout
from rply.errors import LexingError
from lexer import Lexer
from ast import *
from parser import Parser

lexer = Lexer().get_lexer()
pg = Parser()
pg.parse()
parser = pg.get_parser()

while True:
    stdout.write('> ')
    stdout.flush()
    line = stdin.readline()
    if not line: break
    try:
        tokens = lexer.lex(line)
        arbre = parser.parse(tokens)
        resultat = arbre.eval()
        if resultat:
            print (resultat)

    except LexingError as e:
        idx = e.source_pos.idx
        stdout.write(' ' * (idx+2))
        stdout.write('^\n')
        print('Erreur:', e)

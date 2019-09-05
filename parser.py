from rply import ParserGenerator
from ast import *
d={}
class Parser():
	def __init__(self):
		self.pg = ParserGenerator(
		# A list of all token names accepted by the parser.
		['NOMBRE', 'MON', 'PARENTESE1', 'PARENTESE2',
		'POINT_VERG', 'PLUS', 'MOINS', 'FOIS', 'DIVI', 'TERM', 'EGAL', 'QUOTE']
		)
	def parse(self):
		@self.pg.production('language : string')
		@self.pg.production('language : variable')
		@self.pg.production('language : print')
		@self.pg.production('language : expression')
		def lanexp(p):
			hmm=p[0]
			return hmm
		@self.pg.production('string : TERM')
		def string(p):
			val=p[0].value
			return val
		@self.pg.production('variable : string EGAL string')
		@self.pg.production('variable : string EGAL expression')
		def variable(p):
				lhs=p[0]
				rhs=p[2]
				d[lhs]=rhs
				return NoOp()
		@self.pg.production('expression : NOMBRE')
		def number(p):
			return Number(p[0].value)
		@self.pg.production('expression : expression PLUS expression')
		def plus(p):
			left=p[0]
			right=p[2]
			return Sum(left, right)
		@self.pg.production('expression : expression MOINS expression')
		def moins(p):
			left=p[0]
			right=p[2]
			return Sub(left, right)
		@self.pg.production('expression : PARENTESE1 expression PARENTESE2')
		def parentese(p):
			ex=p[1]
			return ex
		@self.pg.production('expression : expression FOIS expression')
		def fois(p):
			left=p[0]
			right=p[2]
			return Times(left, right)
		@self.pg.production('expression : expression DIVI expression')
		def diviser(p):
			left=p[0]
			right=p[2]
			return Divide(left, right)
		@self.pg.production('print : MON PARENTESE1 QUOTE string QUOTE PARENTESE2')
		def montrer(p):
			write=p[3]
			return Montrer(write)
		@self.pg.production('print : MON PARENTESE1 string PARENTESE2')
		def print2(p):
				wie=p[2]
				write2=d.get(wie)
				return Montrer(write2)
	def get_parser(self):
		return self.pg.build()

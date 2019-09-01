from rply import ParserGenerator
from ast import *
class Parser():
	def __init__(self):
		self.pg = ParserGenerator(
		# A list of all token names accepted by the parser.
		['NOMBRE', 'MON', 'PARENTESE1', 'PARENTESE2',
		'POINT_VERG', 'PLUS', 'MOINS', 'FOIS', 'DIVI', 'TERM']
		)
	def parse(self):
		@self.pg.production('language : print')
		@self.pg.production('language : expression')
		def lanexp(p):
			hmm=p[0]
			return hmm
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
		@self.pg.production('print : MON TERM POINT_VERG')
		def montrer(p):
			write=p[1].value
			return Montrer(write)
	def get_parser(self):
		return self.pg.build()
 

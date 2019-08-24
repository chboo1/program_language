from rply import ParserGenerator
from ast import *
class Parser():
	def __init__(self):
		self.pg = ParserGenerator(
		# A list of all token names accepted by the parser.
		['NOMBRE', 'MON', 'PARENTESE1', 'PARENTESE2',
		'POINT_VERG', 'PLUS', 'MOINS']
		)
	def parse(self):
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

	def get_parser(self):
		return self.pg.build()

from rply import ParserGenerator
from ast import *
d={}
class Parser():
	def __init__(self):
		self.pg = ParserGenerator(
		# A list of all token names accepted by the parser.
		['NOMBRE', 'MON', 'PARENTESE1', 'PARENTESE2',
		'POINT_VERG', 'PLUS', 'MOINS', 'FOIS', 'DIVI', 'TERM', 'EGAL', 'QUOTE', 'VERGULE', 'DOLLAR']
		)
	def parse(self):
		@self.pg.production('language : string')
		@self.pg.production('language : variable')
		@self.pg.production('language : print')
		@self.pg.production('language : expression')
		@self.pg.production('language : ac')
		def lanexp(p):
			hmm=p[0]
			return hmm
		@self.pg.production('string : TERM')
		def string(p):
			val=p[0].value
			return val
		@self.pg.production('ac : string VERGULE string')
		@self.pg.production('ac : expression VERGULE expression')
		@self.pg.production('ac : string VERGULE expression')
		@self.pg.production('ac : expression VERGULE string')
		@self.pg.production('ac : ac VERGULE expression')
		@self.pg.production('ac : ac VERGULE string')
		@self.pg.production('ac : string VERGULE ac')
		@self.pg.production('ac : expression VERGULE ac')
		@self.pg.production('ac : ac VERGULE ac')
		def ac(p):
			lhss=p[0]
			rhss=p[2]
			return AC(lhss,rhss)
		@self.pg.production('ac : DOLLAR string VERGULE DOLLAR string')
		def ac2(p):
			lhsss=d.get(p[1])
			rhsss=d.get(p[4])
			return AC(lhsss, rhsss)
		@self.pg.production('ac : DOLLAR string VERGULE expression')
		@self.pg.production('ac : DOLLAR string VERGULE string')
		def ac3(p):
			rhssss=p[3]
			lhssss=d.get(p[1])
			return AC(lhssss, rhssss)
		@self.pg.production('ac : string VERGULE DOLLAR string')
		@self.pg.production('ac : expression VERGULE DOLLAR string')
		def ac4(p):
			lhsssss=p[0]
			rhsssss=d.get(p[3])
			return AC(lhsssss, rhssssss)
		@self.pg.production('variable : string EGAL string')
		@self.pg.production('variable : string EGAL expression')
		def variable(p):
			lhs=p[0]
			rhs=p[2]
			d[lhs]=rhs
			return NoOp()
		@self.pg.production('variable : string EGAL ac')
		def variable2(p):
			lhs=p[0]
			rhs=p[2].eval
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
		@self.pg.production('print : MON PARENTESE1 DOLLAR string PARENTESE2')
		def print2(p):
				wie=p[3]
				write2=d.get(wie)
				return Montrer(write2)
		@self.pg.production('print : MON PARENTESE1 ac PARENTESE2')
		def print3(p):
			thing=p[2]
			return thing
	def get_parser(self):
		return self.pg.build()

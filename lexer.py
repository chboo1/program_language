from rply import LexerGenerator

class Lexer():
    def __init__(self):
        self.lexer = LexerGenerator()

    def _add_tokens(self):
        # Print
        self.lexer.add('MON', r'montrer')
        # Parenthesis
        self.lexer.add('PARENTESE1', r'\(')
        self.lexer.add('PARENTESE2', r'\)')
        # Semi Colon
        self.lexer.add('POINT_VERG', r'\;')
        # Operators
        self.lexer.add('PLUS', r'\+')
        self.lexer.add('MOINS', r'\-')
        # Number
        self.lexer.add('NOMBRE', r'\d+')
        # Ignore spaces
        self.lexer.ignore('\s+')
        self.lexer.add('FOIS', r'\*')
        self.lexer.add('DIVI', r'\/')
        self.lexer.add('TERM', r'[a-zA-Z0-9]+')
        self.lexer.add('EGAL', r'\=+')
        self.lexer.add('QUOTE', r'\'')
        self.lexer.add('VERGULE', r',')
        self.lexer.add('DOLLAR', r'\$')
    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()

import re

r"""lexer.py: Lexical Analyzer Module.

A typical use might be this:
   for category, lexeme in lexer.readTokens (sys.stdin):
       # Process token with given category and lexeme.      
"""

# Syntactic categories.  For best performance, compare against these using
# the 'is' operator, not '='

GTEQ = ">="; LTEQ = "<="; GT = ">";      LT = "<";    ARROW = "-->"; 
PLUS = "+";  MINUS = "-"; STAR = "*";    SLASH = "/"; ASSIGN = "="
LPAR = "(";  RPAR = ")";  SEMI = ";";    COMMA = ","
IF = "if";   DEF = "def"; ELSE = "else"; FI = "fi";   WHILE = "while";
IDENT = "IDENT"; NUMERAL = "NUMERAL"; ERROR = "ERROR"

_tokenMap = { 
        GTEQ: GTEQ, LTEQ: LTEQ, ARROW: ARROW, GT: GT, LT: LT, 
        PLUS: PLUS, MINUS: MINUS, STAR: STAR, SLASH: SLASH, ASSIGN: ASSIGN,
        LPAR: LPAR, RPAR: RPAR, SEMI: SEMI, COMMA: COMMA,
        IF: IF, DEF: DEF, ELSE: ELSE, FI: FI, WHILE: WHILE }

def readTokens(file):
    """A generator that returns pairs (C, L) consisting of the lexemes
    in FILE (L) and their syntactic categories (C)."""
    for token in re.finditer (r"(\s+|#.*)" 
                              r"|>=|<=|-->|if|def|else|fi|while" 
                              r"|([a-zA-Z][a-zA-Z0-9]*)|(\d+)"
                              r"|.",
                              file.read ()):
        L = token.group(0)
        i = token.lastindex
        if i == 1:
            pass
        elif i == 2:
            yield IDENT, L
        elif i == 3:
            yield NUMERAL, L
        else:
            yield _tokenMap.get(L, ERROR), L
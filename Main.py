import re
import ply.lex as lex

# Define tokens
tokens = [
    'COMMENT', 'INLINE_COMMENT', 'OPEN_MULTI_COMMENT', 'CLOSE_MULTI_COMMENT',
    'KEYWORD', 'IDENTIFIER', 'OPEN_PAREN', 'CLOSE_PAREN', 'OPEN_BRACKET',
    'CLOSE_BRACKET', 'ASSIGNMENT', 'INTEGER', 'FLOAT', 'BOOLEAN', 'CHAR',
    'IF', 'ELSE', 'WHILE', 'OP_EQUAL', 'OP_NOTEQ', 'OP_LESSTHAN', 'OP_LESSEQUAL', 'OP_GREATER',
    'OP_GREATEREQ', 'OP_PLUS', 'OP_MINUS', 'OP_MULT', 'OP_DIV', 'OP_MOD', 'OP_AND',
    'OP_OR', 'OP_NOT', 'SEMICOLON'
]

# Define regex patterns for tokens
t_COMMENT = r'\/\*.*?\*\/'
t_INLINE_COMMENT = r'\/\/.*'
t_OPEN_MULTI_COMMENT = r'\/\*\n'
t_CLOSE_MULTI_COMMENT = r'\*\/\n'
t_KEYWORD = r'int\s|bool\s|float\s|char\s|if\s|else\s|while\s'
t_IDENTIFIER = r'[a-zA-Z][a-zA-Z0-9]*'
t_OPEN_PAREN = r'\('
t_CLOSE_PAREN = r'\)'
t_OPEN_BRACKET = r'\{'
t_CLOSE_BRACKET = r'\}'
t_ASSIGNMENT = r'='
t_INTEGER = r'\d+'
t_FLOAT = r'\d+\.\d+'
t_BOOLEAN = r'true|false'
t_CHAR = r'\'.\''
t_IF = r'if'
t_ELSE = r'else'
t_WHILE = r'while'
t_OP_EQUAL = r'=='
t_OP_NOTEQ = r'!='
t_OP_LESSTHAN = r'<'
t_OP_LESSEQUAL = r'<='
t_OP_GREATER = r'>'
t_OP_GREATEREQ = r'>='
t_OP_PLUS = r'\+'
t_OP_MINUS = r'-'
t_OP_MULT = r'\*'
t_OP_DIV = r'/'
t_OP_MOD = r'%'
t_OP_AND = r'&&'
t_OP_OR = r'\|\|'
t_OP_NOT = r'!'
t_SEMICOLON = r';'

# Define ignored characters (spaces and tabs)
t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Error handling
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Sample code
code = """
// /* not a multiline comment */
/*
 * Comment // not an inline comment
 * 1
 */
int main()
{
  int int0 = 6;
  int int1 = 42;
  float flt0 = 5.3;

  if ( int0 <= int1)
  {
    // inline comment 2
    flt0 = flt0 + int1; // inline comment 3 == not comparison
    }
}
/******* COMMENT4 ********/
"""

# Pass the code through the lexer
lexer.input(code)
inside_multiline_comment = False

for tok in lexer:
    if tok.type == 'OPEN_MULTI_COMMENT':
        inside_multiline_comment = True

    if not inside_multiline_comment:
        print(tok.type + ':\t\t' + tok.value.strip())

    if tok.type == 'OPEN_MULTI_COMMENT':
        inside_multiline_comment = True
        print(tok.type)
    elif tok.type == 'CLOSE_MULTI_COMMENT':
        inside_multiline_comment = False
        print(tok.type)


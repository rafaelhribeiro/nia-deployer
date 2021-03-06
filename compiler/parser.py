import ply.lex as lex
import ply.yacc as yacc
import config

tokens = [
    'ID',
    'LPAREN', 
    'RPAREN',
    'APOS',
    'COLON',
    'COMMA',
]

keywords =  config.NILE_OPERATIONS + ['middlebox', 'endpoint','define', 'intent']

tokens += keywords

t_ignore = ' \t\n'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_APOS = r'\''
t_COLON = r':'
t_COMMA = r','

def t_NEWLINE(t):
    r'\n'
    t.lexer.lineno += 1
    return t

def t_ID(t):
    r'[a-zA-Z][a-zA-Z0-9_]*'
    if t.value in keywords:
        t.type = t.value
    return t

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lex.lex()

endpoints = []
middleboxes = []

def p_statement(p):
    'statement : define intent ID COLON commands'
    intent_name = p[3]

def p_commands(p):
    '''commands : command 
                | commands command'''

def p_command(p):
    '''command  : locations
                | _middlebox'''

def p_middlebox_command(p):
    '''_middlebox : add middleboxes'''

def p_middleboxes_name(p):
    '''middleboxes : _mboxname
                   | middleboxes COMMA _mboxname'''

def p_middlebox_name(p):
    '''_mboxname : middlebox LPAREN APOS ID APOS RPAREN'''
    middlebox_name = p[4]
    if not middlebox_name in middleboxes:
        middleboxes.append(middlebox_name)

def p_command_locations(p):
    '''locations : from _endpoint to _endpoint'''

def p_command_endpoint(p):
    '''_endpoint : endpoint LPAREN APOS ID APOS RPAREN'''
    endpoint_name = p[4]
    if not endpoint_name in endpoints:
        endpoints.append(endpoint_name)

def p_error(p):
    if p:
        print("Syntax error at '%s'" % p.value)
    else:
        print("Syntax error at EOF")

yacc.yacc()

def yacc_compile(intent):
    yacc.parse(intent)

""" This will parse the data from the unix command echo "Header1 is this~Header2 and that~~Data 1.0~Data 2.0" | tr "~" "\n"
which is:
Header1 is this
Header2 and that

Data 1.0
Data 2.0
"""

tokens = ('LINUX', 'CPU', 'ALL', 'AMPM', 'INTEGER','DATE')
literals = ['.', ':', '/'  ]

# Tokens
t_LINUX  = r'^Linux.*$'
t_CPU    = r'CPU.*$'
t_ALL    = r'all.*$'
t_AMPM   = r'[AP]M'
t_DATE   = r'Dates.*$'

def t_INTEGER(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

# Ignored characters
t_ignore = " \r"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
import ply.lex as lex   # ply.lex comes from the ply folder in the PLY download.
lexer = lex.lex()

# Parsing rules

global time_step
time_step = 0

def p_start(t):
    '''start : LINUX
             | cpu
             | all
             | empty
             | data
             | date
             | DATE
    '''
    #print "Saw: ", t[1]

def p_time(t):
    'time : INTEGER ":" INTEGER'
    t[0] = str(t[1]) + str(t[2]) + str(t[3]) + str(t[4]) + str(t[5])

def p_date(t):
    'date : INTEGER "/" INTEGER "/" INTEGER time'
    t[0] = str(t[1]) + str(t[2]) + str(t[3]) + str(t[4]) + str(t[5]) + str(t[6])


def p_cpu(t):
    'cpu : time CPU'
    t[0] = str(t[1]) + str(t[2])

def p_all(t):
    'all : time ALL'
    t[0] = str(t[1]) + str(t[2])

def p_data(t):
    'data : time INTEGER float float float float float float float float float'
    print "Saw a Data Line With : " + str(t[2]) + ", " + str(t[10]) + ", " + str(t[11])

def p_float(t):
    'float : INTEGER "." INTEGER'
    t[0] = str(t[1]) + str(t[2]) + str(t[3])

def p_empty(t):
    'empty : '
    pass

def p_error(t):
    if t == None:
        print("Syntax error at '%s'" % t)
    else:
        print("Syntax error at '%s'" % t.value)

import ply.yacc as yacc   # ply.yacc comes from the ply folder in the PLY download.
parser = yacc.yacc()

while True:
    try:
        s = raw_input('')
    except EOFError:
        break
    parser.parse(s)

# To run the parser do the following in a terminal window: echo "Header1 is this~Header2 and that~~Data 1.0~Data 2.0" | tr "~" "\n" | grep -v '^\s*$' | python PLYstarter.py | sed "s/_~_/ which is a float./"

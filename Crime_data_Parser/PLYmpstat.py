"""
##### To run the parser do the following in a terminal window: cat crime.out | python PlyMpstat.py #####

This program will run through data collected from San Fransisco's crime registry from Wednesday, 5-13-15 and
print out the time and type of offense

Brandon Bartos, Caty Nava, Tristan Miranda##

"""

tokens = ('HEADER1', 'INTEGER', 'DATE', 'STRING')
literals = ['.', ':','-']

# Tokens
t_HEADER1  = r'^Header1[ -~]+$'
t_DATE   = r'Dates.*$'

def t_INTEGER(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

def t_STRING(t):
    r'\w+'
    try:
        t.value = str(t.value)
    except ValueError:
        print("String problem %s", t.value)
        t.value = ""
    return t


# Ignored characters
t_ignore = " \r" + " \t"

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
    '''start : HEADER1
             | empty
             | data
             | date
             | DATE
             | offense
             | day

    '''

def p_date(t):
    'date : INTEGER "-" INTEGER "-" INTEGER'
    t[0] = str(t[1]) + str(t[2]) + str(t[3]) + str(t[4]) + str(t[5])

def p_time(t):
    'time : INTEGER ":" INTEGER'
    t[0] = str(t[1]) + str(t[2]) + str(t[3])


def p_offense(t):
    'offense : STRING "-" STRING'
    t[0] = str(t[1]) + str(t[2]) + str(t[3])

def p_day(t):
    'day : STRING'
    t[0] = str(t[1])


def p_data(t):
    'data : date time offense day'
    print "Time/Offense Type: " + str(t[2]) + '/' +str(t[3])


def p_empty(t):
    'empty :    '
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

##### To run the parser do the following in a terminal window: cat crime.out | python PlyMpstat.py #####

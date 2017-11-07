import ox
import pprint
from data import Data

raw_lexer = ox.make_lexer([
    ('SECTION_TITLE', r'\[[^\]]+\]\n*'),
    ('SUBSECTION_TITLE', r'\[\[[^\]]+\]\]\n*'),
    ('DATA', r'\{[^\}]+\}\n*'),
    ('COMMENT', r'\#[^\n]+\n*'),
    ('STRING', r'[^=^#^\n^\[^\]^\}^\{]+\n*'),
    ('EQUAL', r'='),
])

tokens_list = ['SECTION_TITLE',
               'SUBSECTION_TITLE',
               'DATA',
               'COMMENT',
               'STRING',
               'EQUAL']


def lexer(source):
    return [tk for tk in raw_lexer(source) if tk.type != 'COMMENT']


def comment(comment):
    return ('comment', comment)


def section(section, body):
    return (('section', section), body)


def section_all(section, subsection):
    return (section, subsection)


def subsection(subsection, body):
    return (('subsection', subsection), body)


def attribute_data(string_attr, equal, string_variable):
    return (('attr', string_attr), equal, ('variable', string_variable))


def body(body, attribute):
    return (body, attribute)


def document(document, section):
    return (document, section)


def check_digits(string):
    # for ch in string:
    #     if ch.isdigit():
    #         print(ch)
    var = string.split()
    # pprint.pprint(var)
    # pprint.pprint(" ")
    # pprint.pprint(var[2:10])
    teste = var[2:10]
    pprint.pprint(teste)


parser = ox.make_parser([
    ('document : document section', section_all),
    ('document : section', lambda x: x),
    ('section : section subsection', section_all),
    ('section : SECTION_TITLE subsection', section),
    ('section : SECTION_TITLE body', section),
    ('subsection : SUBSECTION_TITLE body', subsection),
    ('body : body attribute', body),
    ('body : attribute', lambda x: x),
    ('attribute : COMMENT', comment),
    ('attribute : STRING EQUAL DATA', attribute_data),
    ('attribute : STRING EQUAL STRING', attribute_data),
], tokens_list)

data = Data()
expr = data.return_data()
tokens = lexer(expr)
ast = parser(tokens)

teste = str(ast)
print("-------------------------------------")
# pprint.pprint(teste)
print("=================================================================================================")
# pprint.pprint(teste.split('subsection'))
var = teste.split('SampleData')
for l in var:
    k = l.split('B')
    # pprint.pprint(k)
    for n in k:
        check_digits(n)
        pprint.pprint("....")
    pprint.pprint("***************************************")

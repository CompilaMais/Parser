import ox
import pprint
from data import Data

lexer = ox.make_lexer([
    ('SECTION_TITLE', r'\[[^\]]+\]\n*'),
    ('SUBSECTION_TITLE', r'\[\[[^\]]+\]\]\n*'),
    ('DATA', r'\{[^\}]+\}\n*'),
    ('ignore_COMMENT', r'\#[^\n]+\n*'),
    ('STRING', r'[^=^#^\n^\[^\]^\}^\{]+\n*'),
    ('EQUAL', r'='),
])

tokens_list = ['SECTION_TITLE',
               'SUBSECTION_TITLE',
               'DATA',
               'STRING',
               'EQUAL']


def section(section, body):
    return (('section', section), body)


def section_all(section, subsection):
    return (section, subsection)


def subsection(subsection, body):
    return ((('subsection', subsection),) + body)


def attribute_data(string_attr, equal, string_variable):
    return (('attr', string_attr), ('variable', string_variable))


def body(attribute, body):
    return ((attribute,) + body)


def section_body(body_section, subsection):
    return (body_section, subsection)


parser = ox.make_parser([
    ('document : document section', section_all),
    ('document : section', lambda x: x),
    ('section : SECTION_TITLE body_section', section),
    ('body_section : body_section subsection', section_body),
    ('body_section : subsection', lambda x: x),
    ('body_section : body', lambda x: x),
    ('subsection : SUBSECTION_TITLE body', subsection),
    ('body : attribute body', body),
    ('body : attribute', lambda x: x),
    ('attribute : STRING EQUAL DATA', attribute_data),
    ('attribute : STRING EQUAL STRING', attribute_data),
], tokens_list)


data = Data()
expr = data.return_data()
tokens = lexer(expr)
ast = parser(tokens)

test = []

for tupla in ast[0]:
    y = tupla
    for line in y:
        test.append(line)
        # print(line)

for lista in test:
    for final_list in lista:
        print(final_list)

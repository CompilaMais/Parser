import ox
import pprint
from data import Data
import collections

# This dictionary remembers the order in which its data are added
dictionary = collections.OrderedDict()

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
    return ((section,) + subsection)


def subsection(subsection, body):
    return ((('subsection', subsection),) + body)


def attribute_data(string_attr, equal, string_variable):
    return (((('attr', string_attr),) + (('variable', string_variable),)),)


def body(attribute, body):
    return ((attribute,) + body)


def document(document, section):
    return (document, section)


dictionary = ox.make_parser([
    ('document : document section', section_all),
    ('document : section', lambda x: x),
    ('section : section subsection', section_all),
    ('section : SECTION_TITLE subsection', section),
    ('section : SECTION_TITLE body', section),
    ('subsection : SUBSECTION_TITLE body', subsection),
    ('body : attribute body', body),
    ('body : attribute', lambda x: x),
    ('attribute : STRING EQUAL DATA', attribute_data),
    ('attribute : STRING EQUAL STRING', attribute_data),
], tokens_list)


# def extract_section(ast):
#     head, *tail = ast
#     if head == 'section':
#         print (tail[0])
#     elif head == 'subsection':
#         print (tail[0])
#     elif head == 'attr':
#         print (tail[0])
#     else:
#         print("==")
#         if tail:
#             x, *y = tail
#             # print(y)
#             extract_section(x)
#             # extract_section(y)
#

data = Data()
expr = data.return_data()
tokens = lexer(expr)
ast = dictionary(tokens)
pprint.pprint(ast[0])

pprint.pprint(ast[1])

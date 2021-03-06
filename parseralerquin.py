from sys import argv
import ox
from models import (Document, Section, Subsection)


file_name, file_in = argv


def create_lexer():
    lexer = ox.make_lexer([
        ('SECTION_TITLE', r'\[[^\]]+\]\n*'),
        ('SUBSECTION_TITLE', r'\[\[[^\]]+\]\]\n*'),
        ('DATA', r'\{[^\}]+\}\n*'),
        ('ignore_COMMENT', r'\#[^\n]+\n*'),
        ('STRING', r'[^=^#^\n^\[^\]^\}^\{]+\n*'),
        ('EQUAL', r'='),
    ])
    return lexer


def create_tokens():
    tokens_list = ['SECTION_TITLE',
                   'SUBSECTION_TITLE',
                   'DATA',
                   'STRING',
                   'EQUAL']
    return tokens_list


def section(section, body):
    return (('section', section), body)


def section_all(section, subsection):
    return (section, subsection)


def subsection(subsection, body):
    return ((('subsection', subsection),) + body)


def attribute_data(string_attr, equal, string_variable):
    return (('attr', string_attr), ('variable', string_variable))


def body(attribute, body):
    return ((attribute, ) + body)


def section_body(body_section, subsection):
    return (body_section, subsection)


#  Defining tokens that will be used in the parser
tokens_list = create_tokens()

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


def eval(ast, document, last_create=None):
    head, *tail = ast

    if head[0] == 'section':
        section = Section(head[1].rstrip())
        document.sections.append(section)
        if tail:
            eval(tail, document, 'section')
    elif head[0] == 'subsection':
        subsection = Subsection(head[1].rstrip())
        document.sections[-1].subsections.append(subsection)
        if tail:
            eval(tail, document, 'subsection')
    elif head[0] == 'attr':
        value = tail[0][1].replace('{', "")
        value = value.replace('}', "")
        value = value.replace('\t', "")
        attr = ({head[1]: (value).rstrip()})
        if last_create == 'section':
            document.sections[-1].attrs.append(attr)
        else:
            document.sections[-1].subsections[-1].attrs.append(attr)
    else:
        eval(head, document, last_create)
        if tail:
            eval(tail, document, last_create)


def get_variable(ast):
    head, *tail = ast
    return head[1]


def open_file(file_in: str):
    file_data = open(file_in, 'r')
    data = file_data.read()
    file_data.close()
    return data


#  Open file user input in comand line
data = open_file(file_in)

#  Defining lexer ast
lexer = create_lexer()
tokens = lexer(data)
ast = parser(tokens)
document = Document()
eval(ast, document)
document.extract_document()
document.print_document()

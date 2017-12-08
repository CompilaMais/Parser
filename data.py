import os
import re


class Data():

    def return_data(self):
        arq = open('lista.txt', 'r')
        data = arq.read()
        # print(data)
        arq.close()

        return data


class Document:
    def __init__(self):
        self.sections = []

    def print_document(self):
        for section in self.sections:
            section.print_section()

    def extract_document(self):
        for section in self.sections:
            section.extract_section()


class Section:
    def __init__(self, name):
        self.name = name
        self.subsections = []
        self.attrs = []

    def print_section(self):
        print(self.name)
        for attr in self.attrs:
            print(attr)

        for subsection in self.subsections:
            subsection.print_subsection()

    def extract_section(self):
        for subsection in self.subsections:
            subsection.extract_subsection()


class Subsection:
    def __init__(self, name):
        self.name = name
        self.attrs = []

    def print_subsection(self):
        print(self.name)
        for attr in self.attrs:
            print(attr)

    def extract_subsection(self):
        extract_lista = []
        for attr in self.attrs:
            if 'SampleData' in attr:
                varAux = extract_subsection_data(attr['SampleData'])
                extract_lista.append(varAux)

        print(extract_lista)


def extract_subsection_data(string):
    '''
    This function receives an subsection string with the data.
    '''

    # Here the spaces are removed from list.
    string_splited = string.split(" ")
    filter_string = []

    # Here the null fields are removed from list.
    for field in string_splited:
        if field != '':
            filter_string.append(field)

    final_list = []
    '''
    All the lists starts with '\n' character in start.So we start to manipulate
    then in position 1 of the list.
    '''
    x = 1
    while x < len(filter_string):
        varAux = []
        varAux.append(filter_string[x])
        varAux.append(filter_string[x+1])
        varAux.append(filter_string[x+2])
        varAux.append(filter_string[x+3])
        varAux.append(filter_string[x+4])
        varAux.append(filter_string[x+5])
        varAux.append(filter_string[x+6])
        varAux.append(filter_string[x+7])
        varAux.append(filter_string[x+8])
        varAux.append(filter_string[x+9])

        final_list.append(varAux)

        '''
        In each subsection with have sub_data to be extracted in this format:
          BT0BA1E1  17  184 116 258 280 184 116 258 280
        So we scroll list in 10 positions each time, so this conditional makes it
        happens in correct way.
        '''
        if(x+11 >= len(filter_string)):
            break
        else:
            x = x + 10

    return final_list

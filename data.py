import pandas as pd
import pprint

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

    number_of_new_lines = string.count('\n')

    # Here the null fields are removed from list.
    for field in string_splited:
        if field != '' and field != '\n':
            filter_string.append(field)

    final_list = []
    '''
    All the lists starts with '\n' character in start.So we start to manipulate
    then in position 1 of the list.
    '''

    number_of_loci = int((len(filter_string)/(number_of_new_lines/2)) - 2)

    x = 0
    for count in range(int(number_of_new_lines/2)):
        varAux = []

        number = filter_string[x] + filter_string[x+1]
        print(number_of_loci)
        for count2 in range(int(number_of_loci/2)):
            varAux.append('(' + filter_string[x+2].replace("\n", "") + ',' +
                          filter_string[x+2+int(number_of_loci/2)].replace("\n", "") + ')')
            x = x + 1

        x = x + 2 + int(number_of_loci/2)
        final_list.append((number, varAux))

    pprint.pprint(final_list)

    columns = []

    for count in range(1, int(number_of_loci/2) + 1):
        column = 'loci_' + str(count)
        columns.append(column)

    print(columns)
    a = pd.DataFrame.from_items(final_list, orient='index', columns=columns)
    print(a)

    return final_list

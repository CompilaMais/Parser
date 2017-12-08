import pandas as pd


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
        self.data_frames = []

    def print_subsection(self):
        print(self.name)
        for attr in self.attrs:
            print(attr)

    def extract_subsection(self):
        for attr in self.attrs:
            if 'SampleData' in attr:
                attr['SampleData'] = self.extract_subsection_data(attr['SampleData'])

    def extract_subsection_data(self, string):
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

            feature = filter_string[x]
            varAux.append(filter_string[x+1])
            for count2 in range(int(number_of_loci/2)):
                varAux.append('(' + filter_string[x+2].replace("\n", "") + ',' +
                              filter_string[x+2+int(number_of_loci/2)].replace("\n", "") + ')')
                x = x + 1

            x = x + 2 + int(number_of_loci/2)
            final_list.append((feature, varAux))

        columns = ['number']

        for count in range(1, int(number_of_loci/2) + 1):
            column = 'loci_' + str(count)
            columns.append(column)

        data_frame = pd.DataFrame.from_items(final_list, orient='index', columns=columns)
        self.data_frames.append(data_frame)
        data_frame.to_csv('DataFrame_out.csv', sep='\t', index=False)

        return data_frame

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


class Subsection:
    def __init__(self, name):
        self.name = name
        self.attrs = []

    def print_subsection(self):
        print(self.name)
        for attr in self.attrs:
            print(attr)

        self.extract_attr()

    def extract_attr(self):
        for attr in self.attrs:
            if 'SampleData' in attr:
                print(attr['SampleData'])

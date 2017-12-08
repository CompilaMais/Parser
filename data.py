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
        # print(self.name)
        # for attr in self.attrs:
        #     print(attr)

        for subsection in self.subsections:
            subsection.print_subsection()


class Subsection:
    def __init__(self, name):
        self.name = name
        self.attrs = []

    def print_subsection(self):
        # print(self.name)
        # for attr in self.attrs:
        #     print(attr)

        self.extract_attr()

    def extract_attr(self):
        x = []
        for attr in self.attrs:
            if 'SampleData' in attr:
                funcao(attr['SampleData'])
                print("==============")
        #         x.append(attr['SampleData'])
        #
        # for y in x:
        #     print("=========")
        #     print(x)
        #     print("=========")


def funcao(string):
    teste = string.split(" ")
    lista = []

    print(teste)
    for letter in teste:
        if letter != '':
            lista.append(letter)

    lista_final = []
    print(lista)

    print("Tamanho lista: %s",len(lista))
    x = 1
    while x < len(lista):
        var = []
        var.append(lista[x])
        var.append(lista[x+1])
        var.append(lista[x+2])
        var.append(lista[x+3])
        var.append(lista[x+4])
        var.append(lista[x+5])
        var.append(lista[x+6])
        var.append(lista[x+7])
        var.append(lista[x+8])
        var.append(lista[x+9])

        lista_final.append(var)

        print("==========")
        print(var)
        print("==========")

        if(x+11 >= len(lista)):
            break
        else:
            x = x + 10

    print(lista_final)

============
Arlequin parser?
============

What is arlequin parser?
===============
In computer technology, a parser is a program, usually part of a compiler, that receives input in the form of sequential source program instructions, interactive online commands, markup tags, or some other defined interface and breaks them up into parts (for example, the nouns (objects), verbs (methods), and their attributes or options) that can then be managed by other programming (for example, other components in a compiler). A parser may also check to see that all input has been provided that is necessary.

Our parser is responsible for extracting information from the subsections of a document in the format Arlequin.py used in Kpop. The information obtained is placed in a DataFrame of the Pandas, facilitating the later manipulation of the same for other purposes.


How to use?
===============

Requirements
------------------

To use the parser, some dependencies must be installed beforehand.The requirements are listed in requirements.txt file.

To install them, run the following command:

    pip  install -r requirements.txt

PS: Consider to run it inside a virtual enviromment.

How to run the parser
------------------

On the command line run parserarlequin.py by passing the file name containing the data to be extracted as a parameter.

For example, consider that the file that contains the data is named arlequin.arp. To extract his data use the following command:

    python3 parserarlequin.py arlequin.arp

How's the output?
------------------
The output format will be a Dataframe from Pandas.For example, will be a structure similiar to the following one:




Contact
===============

from antlr4 import *
from util.OurLangLexer import OurLangLexer
# from util.OurLangListener import OurLangListener
from util.OurLangParser import OurLangParser
from our.OurVisitor import OurVisitor
import sys


def main():

    visitor = OurVisitor()

    while True:
        input_text = input("enter text: ")
        input_stream = InputStream(input_text)

        lexer = OurLangLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = OurLangParser(stream)

        tree = parser.program()

        visitor.visit(tree)


if __name__ == '__main__':
    main()

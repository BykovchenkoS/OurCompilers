from antlr4 import *
from util.OurLangLexer import OurLangLexer
# from util.OurLangListener import OurLangListener
from util.OurLangParser import OurLangParser
from our.OurVisitor import OurVisitor
import sys


def main():
    print("Hello, this is our lab work! Enter text (type 'exit' to quit):")
    visitor = OurVisitor()

    while True:
        input_text = input("> ")

        if input_text.strip().lower() == "exit":
            print("Exiting compiler.")
            break

        input_stream = InputStream(input_text)
        lexer = OurLangLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = OurLangParser(stream)

        try:
            tree = parser.program()
            visitor.visit(tree)
        except Exception as e:
            print(f"Error: {e}")

if __name__ == '__main__':
    main()

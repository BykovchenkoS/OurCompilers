from antlr4 import *
from util.OurLangLexer import OurLangLexer
from util.OurLangParser import OurLangParser
from our.OurVisitor import OurVisitor
import sys


def main():
    try:
        visitor = OurVisitor()

        if len(sys.argv) > 1:
            with open(sys.argv[1], 'r') as file:
                input_text = file.read()

            input_stream = InputStream(input_text)
            lexer = OurLangLexer(input_stream)
            stream = CommonTokenStream(lexer)
            parser = OurLangParser(stream)

            try:
                tree = parser.program()
                visitor.visit(tree)
            except Exception as e:
                print(f"Error: {e}")

        else:
            print("Hello, this is our lab work! Enter text (type 'exit' to quit):")

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

    except Exception:
        print("Compiler job ended forcibly.")


if __name__ == '__main__':
    main()

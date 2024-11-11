from antlr4 import *
from util.OurLangLexer import OurLangLexer
from util.OurLangListener import OurLangListener
from util.OurLangParser import OurLangParser
import sys

class OurLangPrintListener(OurLangListener):
    def exitPrintStatement(self, ctx):
        number = ctx.NUMBER().getText()
        print(number)

def main():
    input_stream = StdinStream()
    lexer = OurLangLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = OurLangParser(stream)

    tree = parser.program()

    listener = OurLangPrintListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

if __name__ == '__main__':
    main()

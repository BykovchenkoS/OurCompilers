from antlr4 import *
from util.OurLangLexer import OurLangLexer
from util.OurLangListener import OurLangListener
from util.OurLangParser import OurLangParser
import sys

class OurLangPrintListener(OurLangListener):
    def enterHello(self, ctx):
        print("Hello: %s" % ctx.ID())

def main():
    lexer = OurLangLexer(StdinStream())
    stream = CommonTokenStream(lexer)
    parser = OurLangParser(stream)
    tree = parser.hello()
    printer = OurLangPrintListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)

if __name__ == '__main__':
    main()
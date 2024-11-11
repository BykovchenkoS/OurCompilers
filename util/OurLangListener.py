# Generated from OurLang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .OurLangParser import OurLangParser
else:
    from OurLangParser import OurLangParser

# This class defines a complete listener for a parse tree produced by OurLangParser.
class OurLangListener(ParseTreeListener):

    # Enter a parse tree produced by OurLangParser#program.
    def enterProgram(self, ctx:OurLangParser.ProgramContext):
        pass

    # Exit a parse tree produced by OurLangParser#program.
    def exitProgram(self, ctx:OurLangParser.ProgramContext):
        pass


    # Enter a parse tree produced by OurLangParser#statement.
    def enterStatement(self, ctx:OurLangParser.StatementContext):
        pass

    # Exit a parse tree produced by OurLangParser#statement.
    def exitStatement(self, ctx:OurLangParser.StatementContext):
        pass


    # Enter a parse tree produced by OurLangParser#printStatement.
    def enterPrintStatement(self, ctx:OurLangParser.PrintStatementContext):
        pass

    # Exit a parse tree produced by OurLangParser#printStatement.
    def exitPrintStatement(self, ctx:OurLangParser.PrintStatementContext):
        pass



del OurLangParser
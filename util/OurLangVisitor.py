# Generated from OurLang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .OurLangParser import OurLangParser
else:
    from OurLangParser import OurLangParser

# This class defines a complete generic visitor for a parse tree produced by OurLangParser.

class OurLangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by OurLangParser#program.
    def visitProgram(self, ctx:OurLangParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OurLangParser#statement.
    def visitStatement(self, ctx:OurLangParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OurLangParser#printStatement.
    def visitPrintStatement(self, ctx:OurLangParser.PrintStatementContext):
        return self.visitChildren(ctx)



del OurLangParser
from util.OurLangParser import OurLangParser
from util.OurLangVisitor import OurLangVisitor


class OurVisitor(OurLangVisitor):
    def __init__(self):
        self.variables = {}

    # Visit a parse tree produced by OurLangParser#program.
    def visitProgram(self, ctx:OurLangParser.ProgramContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by OurLangParser#statement.
    def visitStatement(self, ctx:OurLangParser.StatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by OurLangParser#printStatement.
    def visitPrintStatement(self, ctx:OurLangParser.PrintStatementContext):
        print(ctx.NUMBER().getText())

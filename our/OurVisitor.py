from util.OurLangParser import OurLangParser
from util.OurLangVisitor import OurLangVisitor

variables = {}


class OurVisitor(OurLangVisitor):
    def __init__(self):
        self.variables = {}

    def visitProgram(self, ctx:OurLangParser.ProgramContext):
        return self.visitChildren(ctx)

    def visitStatement(self, ctx:OurLangParser.StatementContext):
        return self.visitChildren(ctx)

    def visitPrintStatement(self, ctx:OurLangParser.PrintStatementContext):
        print(self.visit(ctx.expression()))

    def visitAssignmentStatement(self, ctx:OurLangParser.AssignmentStatementContext):
        var_name = ctx.IDENTIFIER().getText()
        value = self.visit(ctx.expression())
        variables[var_name] = value
        print(f"var {var_name} = {value}")


    def visitNumberExpr(self, ctx:OurLangParser.NumberExprContext):
        return ctx.NUMBER().getText()

# TODO can we even return strings?
    def visitIdExpr(self, ctx:OurLangParser.IdExprContext):
        return variables.get(ctx.IDENTIFIER().getText(), 0)

    def visitAddSubExpr(self, ctx:OurLangParser.AddSubExprContext):
        left = int(self.visit(ctx.expression(0)))
        right = int(self.visit(ctx.expression(1)))
        return left + right if ctx.op.type == OurLangParser.PLUS else left - right

    def visitMulDivExpr(self, ctx:OurLangParser.MulDivExprContext):
        left = int(self.visit(ctx.expression(0)))
        right = int(self.visit(ctx.expression(1)))
        return left * right if ctx.op.type == OurLangParser.MUL else left // right

    def visitLogicalExpr(self, ctx:OurLangParser.LogicalExprContext):
        left = int(self.visit(ctx.expression(0)))
        right = int(self.visit(ctx.expression(1)))
        return int(left and right) if ctx.op.type == OurLangParser.AND else int(left or right)

    def visitNotExpr(self, ctx:OurLangParser.NotExprContext):
        return int(not self.visit(ctx.expression()))

    def visitParenExpr(self, ctx:OurLangParser.ParenExprContext):
        return self.visit(ctx.expression())

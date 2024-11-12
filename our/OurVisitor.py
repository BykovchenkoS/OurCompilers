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

    def visitIfStatement(self, ctx: OurLangParser.IfStatementContext):
        print(f"Visiting if-statement with condition: {ctx.expression()}")
        condition = self.visit(ctx.expression())
        print(f"Condition result: {condition}")

        if condition:
            print("Executing if block")
            for statement in ctx.statement():
                self.visit(statement)

        if ctx.elseStatement():
            print("Executing else block")
            for statement in ctx.elseStatement().statement():
                self.visit(statement)
        else:
            print("No else block found, skipping")

    def visitNumberExpr(self, ctx: OurLangParser.NumberExprContext):
        return int(ctx.NUMBER().getText())

    def visitStringExpr(self, ctx: OurLangParser.StringExprContext):
        return ctx.STRING().getText()[1:-1]

    def visitIdExpr(self, ctx: OurLangParser.IdExprContext):
        var_name = ctx.IDENTIFIER().getText()
        value = variables.get(var_name, None)
        if value is None:
            print(f"Warning: Variable '{var_name}' is not defined.")
            return 0
        return value

    def visitAddSubExpr(self, ctx: OurLangParser.AddSubExprContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))

        if isinstance(left, str) or isinstance(right, str):
            if ctx.op.type == OurLangParser.PLUS:
                return str(left) + str(right)
            elif ctx.op.type == OurLangParser.MINUS:
                raise ValueError("Cannot subtract strings.")
        else:
            left = int(left)
            right = int(right)
            return left + right if ctx.op.type == OurLangParser.PLUS else left - right

    def visitMulDivExpr(self, ctx:OurLangParser.MulDivExprContext):
        left = int(self.visit(ctx.expression(0)))
        right = int(self.visit(ctx.expression(1)))
        return left * right if ctx.op.type == OurLangParser.MUL else left // right

    def visitComparisonExpr(self, ctx: OurLangParser.ComparisonExprContext):
        left = int(self.visit(ctx.expression(0)))
        right = int(self.visit(ctx.expression(1)))

        op_map = {
            OurLangParser.GT: left > right,
            OurLangParser.LT: left < right,
            OurLangParser.GE: left >= right,
            OurLangParser.LE: left <= right,
            OurLangParser.EQ: left == right,
            OurLangParser.NEQ: left != right
        }

        if ctx.op.type in op_map:
            return op_map[ctx.op.type]
        else:
            raise ValueError(f"Unknown comparison operator: {ctx.op.type}")

    def visitLogicalExpr(self, ctx:OurLangParser.LogicalExprContext):
        left = int(self.visit(ctx.expression(0)))
        right = int(self.visit(ctx.expression(1)))
        return int(left and right) if ctx.op.type == OurLangParser.AND else int(left or right)

    def visitNotExpr(self, ctx:OurLangParser.NotExprContext):
        return int(not self.visit(ctx.expression()))

    def visitParenExpr(self, ctx:OurLangParser.ParenExprContext):
        return self.visit(ctx.expression())
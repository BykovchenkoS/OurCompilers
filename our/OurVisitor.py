from util.OurLangParser import OurLangParser
from util.OurLangVisitor import OurLangVisitor

variables = {}


class OurVisitor(OurLangVisitor):

    def visitProgram(self, ctx: OurLangParser.ProgramContext):
        return self.visitChildren(ctx)

    def visitStatement(self, ctx: OurLangParser.StatementContext):
        return self.visitChildren(ctx)

    def visitPrintStatement(self, ctx: OurLangParser.PrintStatementContext):
        print(self.visit(ctx.expression()))

    def visitAssignmentStatement(self, ctx: OurLangParser.AssignmentStatementContext):
        var_name = ctx.IDENTIFIER().getText()
        value = self.visit(ctx.expression())
        variables[var_name] = value

    def visitIfStatement(self, ctx: OurLangParser.IfStatementContext):
        condition = bool(self.visit(ctx.expression()))
        if condition:
            for statement in ctx.statement():
                self.visit(statement)
            return

        if ctx.elifStatement():
            for elif_statement in ctx.elifStatement():
                elif_condition = bool(self.visit(elif_statement.expression()))
                if elif_condition:
                    for statement in elif_statement.statement():
                        self.visit(statement)
                    return

        if ctx.elseStatement():
            for statement in ctx.elseStatement().statement():
                self.visit(statement)
            return

    def visitNumberExpr(self, ctx: OurLangParser.NumberExprContext):
        return int(ctx.NUMBER().getText())

    def visitStringExpr(self, ctx: OurLangParser.StringExprContext):
        return ctx.STRING().getText()[1:-1]

    def visitIdExpr(self, ctx: OurLangParser.IdExprContext):
        var_name = ctx.IDENTIFIER().getText()

        # Обработка булевых значений
        if var_name == "true":
            return True
        elif var_name == "false":
            return False

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

    def visitMulDivExpr(self, ctx: OurLangParser.MulDivExprContext):
        left = int(self.visit(ctx.expression(0)))
        right = int(self.visit(ctx.expression(1)))

        op_map = {
            OurLangParser.MUL: left * right,
            OurLangParser.DIV: left // right,
            OurLangParser.POW: pow(left, right),
            OurLangParser.MOD: left % right
        }

        if ctx.op.type in op_map:
            return op_map[ctx.op.type]
        else:
            raise ValueError(f"Unknown comparison operator: {ctx.op.type}")

    def visitComparisonExpr(self, ctx: OurLangParser.ComparisonExprContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))

        # Приведение значений к булевому типу, если это необходимо
        if not isinstance(left, (int, bool)):
            left = bool(left)
        if not isinstance(right, (int, bool)):
            right = bool(right)

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

    def visitLogicalExpr(self, ctx: OurLangParser.LogicalExprContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))

        if not isinstance(left, bool):
            left = bool(left)
        if not isinstance(right, bool):
            right = bool(right)

        return left and right if ctx.op.type == OurLangParser.AND else left or right

    def visitNotExpr(self, ctx: OurLangParser.NotExprContext):
        value = self.visit(ctx.expression())
        if not isinstance(value, bool):
            value = bool(value)
        return not value

    def visitParenExpr(self, ctx: OurLangParser.ParenExprContext):
        return self.visit(ctx.expression())

    def visitForStatement(self, ctx: OurLangParser.ForStatementContext):
        self.visit(ctx.declaration)
        while bool(self.visit(ctx.expression())):
            for statement in ctx.statement():
                self.visit(statement)
            self.visit(ctx.assignment)

    def visitWhileStatement(self, ctx: OurLangParser.WhileStatementContext):
        while bool(self.visit(ctx.expression())):
            for statement in ctx.statement():
                self.visit(statement)

from util.OurLangParser import OurLangParser
from util.OurLangVisitor import OurLangVisitor

variables = {}
labels, t_var_num = 1, 1
lines = []


def get_args(left, right):
    if isinstance(left, tuple):
        left_val, left_tmp = int(left[0]), str(left[1])
    else:
        left_val, left_tmp = int(left), int(left)

    if isinstance(right, tuple):
        right_val, right_tmp = int(right[0]), str(right[1])
    else:
        right_val, right_tmp = int(right), int(right)
    return left_val, left_tmp, right_val, right_tmp

def get_var_num():
    global t_var_num
    t_var_num += 1
    return f"t{t_var_num - 1}"


def fill_file():
    with open('file.txt', 'w') as f:
        for line in lines:
            f.write(line)



class OurVisitor(OurLangVisitor):

    def visitProgram(self, ctx: OurLangParser.ProgramContext):
        self.visitChildren(ctx)
        fill_file()
        return

    def visitStatement(self, ctx: OurLangParser.StatementContext):
        return self.visitChildren(ctx)

    def visitPrintStatement(self, ctx: OurLangParser.PrintStatementContext):
        value = self.visit(ctx.expression())
        if isinstance(value, tuple):
            value_val, value_tmp = value[0], value[1]
        else:
            value_val, value_tmp = value
        lines.append(f"print {value_tmp}\n")
        print(value_val)

    def visitAssignmentStatement(self, ctx: OurLangParser.AssignmentStatementContext):
        var_name = ctx.IDENTIFIER().getText()
        value, t_value = self.visit(ctx.expression())
        variables[var_name] = value
        lines.append(f"{var_name} = {t_value}\n")

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
            print(f"Warning: Variable '{var_name}' is not defined.\n")
            return 0
        return value

    def visitAddSubExpr(self, ctx: OurLangParser.AddSubExprContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        t = get_var_num()

        # Сложение строк
        if isinstance(left, str) or isinstance(right, str):

            if isinstance(left, tuple):
                left_val, left_tmp = str(left[0]), str(left[1])
            else:
                left_val, left_tmp = str(left), str(left)

            if isinstance(right, tuple):
                right_val, right_tmp = str(right[0]), str(right[1])
            else:
                right_val, right_tmp = str(right), str(right)

            if ctx.op.type == OurLangParser.PLUS:
                lines.append(f"{t} = {left_tmp} + {right_tmp}\n")
                return str(left_val) + str(right_val)
            elif ctx.op.type == OurLangParser.MINUS:
                raise ValueError("Cannot subtract strings.\n")

        # Сложение чисел
        else:

            vals = get_args(left, right)
            left_val, left_tmp, right_val, right_tmp = vals[0], vals[1], vals[2], vals[3]

            if ctx.op.type == OurLangParser.PLUS:
                lines.append(f"{t} = {left_tmp} + {right_tmp}\n")
                return left_val + right_val, t
            else:
                lines.append(f"{t} = {left_tmp} - {right_tmp}\n")
                return left_val - right_val, t

    def visitMulDivExpr(self, ctx: OurLangParser.MulDivExprContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        t = get_var_num()

        vals = get_args(left, right)
        left_val, left_tmp, right_val, right_tmp = vals[0], vals[1], vals[2], vals[3]

        op_map = {
            OurLangParser.MUL: left_val * right_val,
            OurLangParser.DIV: left_val // right_val,
            OurLangParser.POW: pow(left_val, right_val),
            OurLangParser.MOD: left_val % right_val
        }

        if ctx.op.type in op_map:
            operator = OurLangParser.literalNames[ctx.op.type].strip("\'")
            lines.append(f"{t} = {left_tmp} {operator} {right_tmp}\n")
            return op_map[ctx.op.type], t
        else:
            raise ValueError(f"Unknown comparison operator: {ctx.op.type}\n")

    def visitComparisonExpr(self, ctx: OurLangParser.ComparisonExprContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        t = get_var_num()

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
            lines.append(f"{t} = {left} {ctx.op.type} {right}\n")
            return op_map[ctx.op.type], t
        else:
            raise ValueError(f"Unknown comparison operator: {ctx.op.type}")

    def visitLogicalExpr(self, ctx: OurLangParser.LogicalExprContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        t = get_var_num()

        if not isinstance(left, bool):
            left = bool(left)
        if not isinstance(right, bool):
            right = bool(right)

        if ctx.op.type == OurLangParser.AND:
            lines.append(f"{t} = {left} && {right}\n")
            return left and right, t
        else:
            lines.append(f"{t} = {left} || {right}\n")
            return left or right, t

    def visitNotExpr(self, ctx: OurLangParser.NotExprContext):
        value = self.visit(ctx.expression())
        t = get_var_num()
        if not isinstance(value, bool):
            value = bool(value)
        lines.append(f"{t} = !{value}\n")
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

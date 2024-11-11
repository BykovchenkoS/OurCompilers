from antlr4 import *
from util.OurLangLexer import OurLangLexer
from util.OurLangListener import OurLangListener
from util.OurLangParser import OurLangParser
import sys

variables = {}

class OurLangPrintListener(OurLangListener):
    def exitPrintStatement(self, ctx):
        # Обрабатываем выражение в операторе print
        value = self.evaluate_expression(ctx.expression())
        print(value)

    def exitAssignmentStatement(self, ctx):
        # Обрабатываем присваивание переменной
        var_name = ctx.IDENTIFIER().getText()
        value = self.evaluate_expression(ctx.expression())
        variables[var_name] = value

    def evaluate_expression(self, ctx):
        if isinstance(ctx, OurLangParser.NumberExprContext):
            return int(ctx.NUMBER().getText())
        elif isinstance(ctx, OurLangParser.IdExprContext):
            var_name = ctx.IDENTIFIER().getText()
            return variables.get(var_name, 0)
        elif isinstance(ctx, OurLangParser.AddSubExprContext):
            left = self.evaluate_expression(ctx.expression(0))
            right = self.evaluate_expression(ctx.expression(1))
            return left + right if ctx.op.type == OurLangParser.PLUS else left - right
        elif isinstance(ctx, OurLangParser.MulDivExprContext):
            left = self.evaluate_expression(ctx.expression(0))
            right = self.evaluate_expression(ctx.expression(1))
            return left * right if ctx.op.type == OurLangParser.MUL else left // right
        elif isinstance(ctx, OurLangParser.LogicalExprContext):
            left = self.evaluate_expression(ctx.expression(0))
            right = self.evaluate_expression(ctx.expression(1))
            return int(left and right) if ctx.op.type == OurLangParser.AND else int(left or right)
        elif isinstance(ctx, OurLangParser.NotExprContext):
            return int(not self.evaluate_expression(ctx.expression()))
        elif isinstance(ctx, OurLangParser.ParenExprContext):
            return self.evaluate_expression(ctx.expression())
        else:
            raise ValueError("Unknown expression type")

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

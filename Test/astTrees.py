import ast
from ast import *


tree = Module(
  body=[
    Expr(
      value=BinOp(
        left=IfExp(
          test=Compare(
            left=Name(id='x', ctx=Load()),
            ops=[
              GtE()],
            comparators=[
              Constant(value=5)]),
          body=Name(id='x', ctx=Load()),
          orelse=Name(id='y', ctx=Load())),
        op=Add(),
        right=IfExp(
          test=Compare(
            left=Name(id='x', ctx=Load()),
            ops=[
              Lt()],
            comparators=[
              Constant(value=3)]),
          body=BinOp(
            left=Name(id='y', ctx=Load()),
            op=Mod(),
            right=Constant(value=3)),
          orelse=Constant(value=5))))],
  type_ignores=[])

x, y = 3, 1
print(ast.unparse(tree))
print((x if x >= 5 else y) + (y % 3 if x < 3 else 5))

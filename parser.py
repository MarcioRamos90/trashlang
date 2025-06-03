import lexer
from errors import ComparisonError


class BinOp:
  def __eq__(self, obj):
    if not isinstance(obj, BinOp):
      raise ComparisonError(self, obj)
    return self.left == obj.left and self.op == obj.op and self.right == obj.right

  def __init__(self, left, op, right):
    self.left = left
    self.op = op
    self.right = right

  def __repr__(self):
    return f"<{self.__class__.__name__}:{self.left}{self.op}{self.right}>"
  

def precedence(op):
  match op:
    case ['+', '-']:
      return [9]
    case ['*', '/']:
      return [10]


class Parser:
  def __init__(self, tokens):
    self.tokens = tokens
    self.index = 0

  def parse(self):
    exp = self.expression()
    return exp
  
  def expression(self):
    left = self.current()
    while self.next():
      op = self.current()
      right = self.next()
      if self.has_next():
        right = self.expression()
    return BinOp(left, op, right)

  def current(self, offset=0):
    return self.tokens[self.index + offset]
  
  def has_next(self):
    return not isinstance(self.current(1), lexer.Eof)

  def next(self):
    if self.has_next():
      self.index += 1
      return self.current()

import lexer
from errors import ComparisonError


class BinOp:
  def __eq__(self, obj):
    if not isinstance(obj, BinOp):
      print(self, obj)
      raise ComparisonError(self, obj)
    return self.left == obj.left and self.op == obj.op and self.right == obj.right

  def __init__(self, left, op, right):
    self.left = left
    self.op = op
    self.right = right

  def __repr__(self):
    return f"<{self.__class__.__name__}:{self.left}{self.op}{self.right}>"
  

def precedence(op: lexer.Token):
  v = op.value
  if v in ['+', '-']:
      return 9
  elif v in ['*', '/']:
      return 10
  return 0


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
      current_precedence = precedence(op)
      
      right = self.next()
      if self.has_next() and current_precedence > self.next_precedence():
        left = BinOp(left, op, right)  
      elif self.has_next() and current_precedence < self.next_precedence():
        right = self.expression()
    return BinOp(left, op, right)

  def next_precedence(self):
    return precedence(self.read_next())
  
  def read_next(self):
    return self.current(1)
    
  def current(self, offset=0):
    return self.tokens[self.index + offset]
  
  def has_next(self):
    return not isinstance(self.current(1), lexer.Eof)

  def next(self):
    if self.has_next():
      self.index += 1
      return self.current()

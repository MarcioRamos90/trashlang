class Token():
  def __init__(self, value):
    self.value = value

  def __eq__(self, obj):
    if not isinstance(obj, Token):
      return False
    return self.value == obj.value

  def __repr__(self):
    return f"<{self.__class__.__name__}:{self.value}>"

class ParentesesOpen(Token):
  pass

class ParentesesClose(Token):
  pass

class Number(Token):  
  pass

class Op(Token):
  pass

class Eof(Token):
  def __init__(self):
    self.value = 'Eof'


class Lexer():
  def __init__(self, code):
    self.code = code
    self.index = 0
    self.current = code[self.index]
    self.tokens = []
  
  def next(self):
    if self.index < len(self.code) - 1:
      self.index += 1
      self.current = self.code[self.index]
      return True
    self.current = None
    return False

  def get_tokens(self):
    while self.current:
      if self.is_number():
        num = self.get_number() 
        self.tokens.append(Number(num))
        continue
      elif self.is_op():
        op = self.get_op() 
        self.tokens.append(Op(op))
      elif self.is_open_parenteses():
        paren = self.get_op() 
        self.tokens.append(ParentesesOpen(paren))
      elif self.is_close_parenteses():
        paren = self.get_op() 
        self.tokens.append(ParentesesClose(paren))
      if not self.next():
        break
    self.tokens.append(Eof())
    return self.tokens

  def is_open_parenteses(self):
    return self.current == '('

  def is_close_parenteses(self):
    return self.current == ')'
  
  def get_parenteses(self):
    return self.current
    
  def is_op(self):
    return self.current and self.current in ('+', '-', '/', '*')
  
  def get_op(self):
    return self.current

  def is_number(self):
    return self.current and self.current.isdigit()
  
  def get_number(self):
    num_str = ''
    while self.is_number():
      num_str += self.current
      self.next()
    return num_str

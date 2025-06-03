from lexer import *

def test_tokens_creation():
  expect = [Number('1'), Op("+"), Number('2'), Eof()]
  tokens = Lexer("1+2").get_tokens()
  assert tokens == expect, "Error on comparing"


def test_tokens_creation():
  expect = [ 
            Number('1'), 
            Op("+"),
            Number('2'),
            Op("*"),
            Number('3'),
            Eof()]
  tokens = Lexer("1+2*3").get_tokens()
  assert tokens == expect, "Error on comparing"


def test_tokens_creation_with_parenteses():
  expect = [Parenteses('('), 
            Number('1'), 
            Op("+"),
            Number('2'),
            Parenteses(')'),
            Op("*"),
            Number('8'),
            Eof()]
  tokens = Lexer("(1+2)*8").get_tokens()
  assert tokens == expect, "Error on comparing"

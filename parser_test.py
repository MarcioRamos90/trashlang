from lexer import *
from parser import *

def test_gen_simple_parsed_structure():
  tokens = Lexer("1 + 2").get_tokens()
  result = Parser(tokens).parse()

  assert result == BinOp(Number('1'), Op('+'), Number('2'))

def test_gen_not_so_simple_parsed_structure():
  tokens = Lexer("1 + 2 * 3").get_tokens()
  result = Parser(tokens).parse()

  assert result == BinOp(Number('1'), Op('+'),
                          BinOp(Number('2'), Op('*'), Number('3')))


def test_gen_not_so_simple_parsed_structure_with_reversed_precedence():
  tokens = Lexer("1 * 2 + 3").get_tokens()
  result = Parser(tokens).parse()

  assert result == \
    BinOp(
      BinOp(Number('1'), Op('*'), Number('2')),
      Op('+'), 
      Number('3'))


def test_parsing_with_parenteses():
    tokens = Lexer("(1+2)*3").get_tokens()
    result = Parser(tokens).parse()

    assert result == \
      BinOp(
        BinOp(Number('1'), Op('+'), Number('2')),
        Op('*'), 
        Number('3'))
  
# def test_parsing_with_parenteses():
#     tokens = Lexer("((1+2)+2)*3").get_tokens()
#     result = Parser(tokens).parse()

#     assert result == \
#       BinOp(
#         BinOp(Number('1'), Op('+'), Number('2')),
#         Op('*'), 
#         Number('3'))
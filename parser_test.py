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
  

def test_gen_complex_parsed_structure():
  tokens = Lexer("1 + 2 * 3 - 4").get_tokens()
  result = Parser(tokens).parse()

  assert result == \
    BinOp(
      Number('1'), Op('+'),
      BinOp(
          BinOp(Number('2'), Op('*'), Number('3')),
          Op('-'), 
          Number('4')),
    )


def test_gen_not_so_simple_parsed_structure_with_reversed_precedence():
  tokens = Lexer("1 * 2 + 3").get_tokens()
  result = Parser(tokens).parse()

  assert result == \
    BinOp(
      BinOp(Number('1'), Op('*'), Number('2')),
      Op('+'), 
      Number('3'))


def test_parsing_with_parenteses_in_left():
    tokens = Lexer("(1+2)*3").get_tokens()
    result = Parser(tokens).parse()

    assert result == \
      BinOp(
        BinOp(Number('1'), Op('+'), Number('2')),
        Op('*'), 
        Number('3'))


def test_parsing_with_parenteses_in_right():
    tokens = Lexer("3*(1+2)").get_tokens()
    result = Parser(tokens).parse()

    assert result == \
      BinOp(
        Number('3'),
        Op('*'), 
        BinOp(Number('1'), Op('+'), Number('2')),
      )
  

def test_parsing_with_parenteses_2():
    tokens = Lexer("((1+2)+2)*3").get_tokens()
    result = Parser(tokens).parse()

    assert result == \
      BinOp(
        BinOp(
          BinOp(Number('1'), Op('+'), Number('2')), 
          Op('+'),
          Number('2')),
        Op('*'), 
        Number('3'))


def test_parsing_with_parenteses_3():
    tokens = Lexer("((1+2)+(1-2))*3").get_tokens()
    result = Parser(tokens).parse()

    assert result == \
      BinOp(
        BinOp(
          BinOp(Number('1'), Op('+'), Number('2')), 
          Op('+'),
          BinOp(Number('1'), Op('-'), Number('2')),
        ),
        Op('*'), 
        Number('3')
      )


def test_error_parsing_1(): # TODO: Fix this test!!!
  tokens = Lexer("4+4+5").get_tokens()
  result = Parser(tokens).parse()

  assert result == BinOp(BinOp(Number('4'), Op('+'), Number('4')), Op('+'), Number('5'))

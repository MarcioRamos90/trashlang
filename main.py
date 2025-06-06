from lexer import *
from parser import *

def main():
  tokens = Lexer("1 * 2 + 3").get_tokens()
  result = Parser(tokens).parse()
  print(result)

main()
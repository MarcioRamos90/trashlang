from lexer import *
from parser import *

def main():
  while True:
    code = input("> ")
    if code == "q":
      return
    tokens = Lexer(code).get_tokens()
    result = Parser(tokens).parse()
    print(result)

main()
from lexer import *

def main():
  expect = [Number(1), Op("+"), Number(22), Eof()]
  tokens = Lexer("2025 + 200 * 9 + 0").get_tokens()
  print(tokens)
  # assert tokens == expect, "Error on comparing"


main()
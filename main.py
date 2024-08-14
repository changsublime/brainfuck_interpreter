import sys

from interpreter import Interpreter

if __name__ == "__main__":
    program = sys.stdin.readline().rstrip()
    arg = sys.stdin.readline().rstrip()
    interpreter = Interpreter()
    output = interpreter.interpret(program, arg)
    print(output)
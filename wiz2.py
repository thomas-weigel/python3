#!/usr/bin/env python3
import sys

def main():
    try:
        while True:
            task = input("> ")
            if task == "quit":
                bye()
            print(f'''I performed: {task}.''')
    except (KeyboardInterrupt, EOFError):
        bye()

def bye():
   # print(EOFError)
    sys.exit(EOFError)

if __name__ == "__main__":
    main()
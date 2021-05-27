from converters import *
import sys

if __name__ == "__main__":
    try:
        if sys.argv[1] == "-ds":
            ascii_convert(sys.argv[3], int(sys.argv[2]))
        else:
            ascii_convert(sys.argv[1])
    except:
        print("Invalid argument(s)!")
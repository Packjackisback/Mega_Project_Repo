import sys
def method(string:str):
    return len(string.split())

if len(sys.argv)>1:
    print(method(" ".join(sys.argv[1:])))
else:
    print(method(input("> ")))


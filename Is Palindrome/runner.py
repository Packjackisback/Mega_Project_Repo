import sys
def method(string:str):
    return string[:int(len(string)/2)] == string[:int(len(string)/2):-1]

if len(sys.argv)>1:
    print(method(" ".join(sys.argv[1:])))
else:
    print(method(input("> ")))


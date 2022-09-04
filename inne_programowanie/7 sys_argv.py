from sys import argv
#argv są to argumenty z lini poleceń z wywoływaniem skryptu

def add(x, y):
    return x + y

def main(args):
    print(add(int(args[1]), int(args[2])))

if __name__ == "__main__":
    main(argv)
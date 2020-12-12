addnum =  lambda *args : sum(args)

def prodnum(*args):
    res = 1
    for arg in args:
        res *=arg
    return res

if __name__ == "__main__":
    print(addnum(4,5,7))
    print(prodnum(2,5,2.5))
def BooWho(Check):
    if type(Check) == bool:
        print("true")
    else:
        print("false")
BooWho(True)
BooWho(False)
BooWho([1 , 2 , 3])
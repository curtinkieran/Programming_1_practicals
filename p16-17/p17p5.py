'''alter program according to instructions in notes'''

def checkpal(x):
    print("Checkpal function called with argument", x)
    def lower(x):
        x = x.lower()
        letstring=""
        for char in x:
            if char in "abcdefghijklmnopqrstuvwxyz":
                letstring += char
        return letstring
    def palind(x):
        if len(x) <= 1:
            print("About to return True from function 'palind' from the base case")
            return True
        else:
            result = x[0] == x[-1] and palind(x[1:-1])
            print("About to return", result, "from function 'palind' with argument", x)
            return x[0] == x[-1] and palind(x[1:-1])
    return palind(lower(x))
    

checkpal("wwwnwww")


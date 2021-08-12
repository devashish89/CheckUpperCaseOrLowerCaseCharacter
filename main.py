# Check Case of Character
# ord("A") = ASCII value of A
# chr(65) = "A"
# String are compared based upon ASCII no.

def checkCase(c):
    if "A" <= c <= "Z":
        return "UpperCase"
    elif "a" <= c <= "z":
        return "LowerCase"
    else:
        return "Indifferent"


if __name__ == '__main__':
    print(ord("A"))
    print(chr(65))

    print(checkCase("H"))
    print(checkCase("d"))
    print(checkCase("1"))

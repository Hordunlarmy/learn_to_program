def comp_str(argone, argtwo):
    argone_rev = list(argone[::-1])
    argtwo_rev = list(argtwo[::-1])

    for char in argone_rev:
        if argtwo_rev and char == argtwo_rev[0]:
            argtwo_rev.pop(0)
        else:
            break

    if argtwo_rev:
        print(False)
    else:
        print(True)


comp_str("deobaba", "baba")
comp_str("deobaba", "bbaa")

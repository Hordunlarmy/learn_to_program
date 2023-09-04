def comp_str(argone, argtwo):
    argone_rev = argone[::-1]
    argtwo_rev = argtwo[::-1]
    if (argone_rev.find(argtwo_rev) != -1):
        print("True")
    else:
        print("False")


comp_str("deobaba", "deo")
comp_str("deobaba", "bbaa")

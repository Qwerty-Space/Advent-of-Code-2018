with open("input.txt") as f:
    contents = f.read().split()
    print(eval("".join(contents)))
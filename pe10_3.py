def nameFormat (first, last, middle=None):
    if middle:
        print(last.capitalize(), first.capitalize(), middle.capitalize()[0],  sep=", ")
    else:
        print(last, first, sep=", ")

def main():
    nameFormat(first="james", last="bond")
    nameFormat("henry","jones", "indianna")

main()
def nameFormat(first, middle, last):
    print(first.capitalize(), middle.capitalize()[0], last.capitalize())

def main():
    nameFormat("john", "stu", "smith")
    nameFormat(last = "kennedy", first="john", middle="fitzgerald")

main()


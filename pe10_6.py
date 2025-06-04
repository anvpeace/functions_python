import random

def average(*grades):
    return sum(grades) / len(grades)

def main():

    print(f"Average of 95,87,83,74: ", average(95,87,83,74))

    x = random.randint(-100, 0)
    y = random.randint(0, 100)

    print(f"Average of two random numbers: ", average(x,y))
main()

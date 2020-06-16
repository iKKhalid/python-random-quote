import random


def main():
    print("Keep it logically awesome.")

    f = open('quotes.txt', 'a')
    f.write('Hello\n')
    f.close()

    f = open("quotes.txt")
    quotes = f.readlines()
    f.close()

    last01 = 13
    last02 = 13
    rnd01 = random.randint(0, last01)
    rnd02 = random.randint(0, last02)

    print(quotes[rnd01].rstrip())
    print(quotes[rnd02])


if __name__ == "__main__":
    main()

from color import Color


def main():
    red = Color(red=1, green=0, blue=0)
    green = Color(red=0, green=1, blue=0)
    blue = Color(red=0, green=0, blue=1)
    print(red)
    print(red+green)


if __name__ == "__main__":
    main()
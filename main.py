from image import Image
from color import Color


def main():
    WIDTH = 3
    HEIGHT = 8
    red = Color(red=1, green=0, blue=0)
    green = Color(red=0, green=1, blue=0)
    blue = Color(red=0, green=0, blue=1)

    im = Image(WIDTH, HEIGHT)
    pixel_matrix = [
        [red+green, red+blue+green, red*0.001 ],
        [red,       green,          blue      ],

        # mixing
        [red,       red+green,      red+blue  ],
        [green,     green+red,      green+blue],
        [blue,      blue+red,       blue+green],
        
        # darker shaddow:
        [red,       red*0.8,        red*0.3  ],
        [green,     green*0.8,      green*0.3],
        [blue,      blue*0.8,       blue*0.3 ],
    ]
    im.set_pixel_matrix(pixel_matrix)

    im.generate_png(file_name="test")


if __name__ == "__main__":
    main()
from ppm_to_png import convert_to_jpg

class Image:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self._create_pixels_matrix()

    def _create_pixels_matrix(self):
        self.pixels = []
        for _ in range(self.height):
            row = []
            for __ in range(self.width):
                row.append(None)
            self.pixels.append(row)
    
    def set_pixel_matrix(self, pixel_matrix, width=None, height=None):
        if width == None:
            width = self.width
        if height == None:
            height = self.height
        assert  len(pixel_matrix) == height, "Pixel matrix does not obey height size"
        for row in pixel_matrix:
            assert  len(row) == width, "Pixel matrix does not obey width size"
        self.pixels = pixel_matrix
        self.height = height
        self.width = width

    def set_pixel_color(self, x, y, color):
        self.pixels[y][x] = color
    
    def write_picture_pixel_map(self, image_file):
        image_file.write("P3\n{} {}\n255\n".format(self.width, self.height))
        for row in self.pixels:
            for color in row:
                image_file.write(color.to_byte_map())
            image_file.write("\n")

    def create_ppm_file(self, file_name="test"):
        with open(f"{file_name}.ppm", "w") as img:
            self.write_picture_pixel_map(img)
    
    def generate_png(self, file_name="test"):
        self.create_ppm_file(file_name=file_name)
        convert_to_jpg(file_name=file_name)

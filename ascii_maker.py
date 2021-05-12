import PIL.Image

CHARS = ["@", "#", "S", "%", "?", "o", ";", ":", ",", "."]


def imgsize(image, new_width=100):
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio)
    resized = image.resize( (new_width, new_height) )
    return resized

def greyscale(image):
    return image.convert('L')

def ascii_convert(image):
    pixels = image.getdata()
    characters = "".join([CHARS[pixels//25] for pixel in pixels])
    return characters
    
from PIL import Image

BRAILLE = ['⠀','⠮','⠐','⠼','⠫','⠩','⠯','⠄','⠷','⠾','⠡','⠬','⠠','⠤','⠨','⠌','⠴','⠂','⠆','⠒','⠲','⠢',
        '⠖','⠶','⠦','⠔','⠱','⠰','⠣','⠿','⠜','⠹','⠈','⠁','⠃','⠉','⠙','⠑','⠋','⠛','⠓','⠊','⠚','⠅',
        '⠇','⠍','⠝','⠕','⠏','⠟','⠗','⠎','⠞','⠥','⠧','⠺','⠭','⠽','⠵','⠪','⠳','⠻','⠘','⠸']

def convert_to_greyscale(img):
    return img.convert("L")

def resize_image(img):
    width = img.size[0] // 10
    height = img.size[1] // 10
    return img.resize((width, int(height/1.65))), width

def pixels_to_braille()

def braille_convert():
    final = []

    path = input("Enter a valid pathname:\n")

    image = Image.open(path)

    print(resize_image(image))

braille_convert()
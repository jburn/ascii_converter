from PIL import Image

ASCII = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

BINARY = [32,16,8,4,2,1]

BRAILLE = {
    0: '⠀',
    1: '⠠',
    2: '⠄',
    3: '⠤',
    4: '⠐',
    5: '⠰',
    6: '⠔',
    7: '⠴',
    8: '⠂ ',
    9: '⠢',
    10: '⠆',
    11: '⠦',
    12: '⠒',
    13: '⠲',
    14: '⠖',
    15: '⠶',
    16: '⠈',
    17: '⠨',
    18: '⠌',
    19: '⠬',
    20: '⠘',
    21: '⠸',
    22: '⠜',
    23: '⠼',
    24: '⠊',
    25: '⠪',
    26: '⠎',
    27: '⠮',
    28: '⠚',
    29: '⠺',
    30: '⠞',
    31: '⠾',
    32: '⠁',
    33: '⠡',
    34: '⠅',
    35: '⠥',
    36: '⠑',
    37: '⠱',
    38: '⠕',
    39: '⠵',
    40: '⠃',
    41: '⠣',
    42: '⠇',
    43: '⠧',
    44: '⠓',
    45: '⠳',
    46: '⠗',
    47: '⠷',
    48: '⠉',
    49: '⠩',
    50: '⠍',
    51: '⠭',
    52: '⠙',
    53: '⠹',
    54: '⠝',
    55: '⠽',
    56: '⠋',
    57: '⠫',
    58: '⠏',
    59: '⠯',
    60: '⠛',
    61: '⠻',
    62: '⠟',
    63: '⠿'}


def convert_to_greyscale(img):
    return img.convert("L")

def resize_image(img):
    width = img.size[0] // 10
    height = img.size[1] // 10 
    return img.resize((width, int(height/1.65))), width

def pixels_to_ascii(img):
    ascii_list = []
    pixels = img.getdata()
    for pixel in pixels:
        ascii_list.append("".join(ASCII[pixel//25]))
    return ascii_list

def ascii_convert():
    final = []

    path = input("Enter a valid pathname:\n")

    image = Image.open(path)

    resized, width = resize_image(image)

    
    ascii_data = pixels_to_ascii(convert_to_greyscale(resized))

    datalen = len(ascii_data)

    for i in range(0, datalen, width):
        final.append("".join(ascii_data[i:i+width]))
    
    final = "\n".join(final)
    print(final)

def braille_convert():

    shitlist = []
    path = input("Enter a valid pathname:\n")

    image = Image.open(path)

    resized, width = resize_image(image)

    data = list(resized.getdata(0))
    datalen = len(data)

    print("datalen ", datalen)
    
    newlist = []

    n = 0
    for i in range(0, datalen-(width*2+1)):
        shitlist.append([])
        shitlist[n].extend([data[i], data[i+1], data[i+width], data[i+width+1], data[i+width*2], data[i+width*2+1]])
        n += 1

    print(len(shitlist))
    for n, sixlist in enumerate(shitlist):
        newlist.append(0)
        for i, item in enumerate(sixlist):
            if item < 120:
                shitlist[n][i] = 0
            else:
                shitlist[n][i] = 1
                newlist[n] += BINARY[i]

    newlen = len(newlist)
    print(newlen)

    braille_image = []
    for n in newlist:
        braille_image.append(BRAILLE[n])

    final = []
    for i in range(0, newlen, width):
        final.append("".join(braille_image[i:i+width]))

    final = "\n".join(final)
    print(final)



    #print(shitlist)
    #print(newlist)



braille_convert()
#ascii_convert()
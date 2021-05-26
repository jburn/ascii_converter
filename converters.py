from PIL import Image
from values import *
import os
import inspect
print ()


def convert_to_greyscale(img):
    return img.convert("L")


def resize_image(img, divider):
    width = img.size[0] // divider
    height = img.size[1] // divider
    return img.resize((width, int(height/1.65)))


def pixels_to_ascii(img):
    ascii_list = []
    pixels = img.getdata()
    for pixel in pixels:
        ascii_list.append("".join(ASCII[pixel//25]))
    return ascii_list


def onedim2twodim(list1d, width):
    list2d = []
    datalen = len(list1d)
    for j in range(0, datalen, width):
        list2d.append(list1d[j:j+width])
    return list2d


def split_to_braille_chunks(list2d):
    n = 0
    height = len(list2d)
    width = len(list2d[0])
    chunklist = []

    for j in range(0, height-2, 3):
        for i in range(0, width-1, 2):
            chunklist.append([])
            chunklist[n].extend([list2d[j][i], list2d[j][i+1]])
            if j+1 < height-1:
                chunklist[n].extend([list2d[j+1][i], list2d[j+1][i+1]])
            if j+2 < height-1:
                chunklist[n].extend([list2d[j+2][i], list2d[j+2][i+1]])
            n += 1

    return chunklist


def chunks_to_braille(list_of_chunks):
    dict_values = []
    braillelist = []

    for n, chunk in enumerate(list_of_chunks):
        dict_values.append(0)
        for i, item in enumerate(chunk):
            if item < 128:
                pass
            else:
                dict_values[n] += BINARY[i]
        
    for n in dict_values:
        braillelist.append(BRAILLE[n])

    return braillelist


def ascii_convert(path, divid):
    print(divid)
    result = []

    #path = input("Enter a valid pathname:\n")
    
    try:
        image = Image.open(path)
    except:
        print("Invalid file or path!")
        exit(1)

    """
    while True:
        divid = int(input("Enter resize divider: "))
        if divid < 1:
            print("Invalid value!")
        else:
            break
    """
    
    resized = resize_image(image, divid)
    width = resized.size[0]
    ascii_data = pixels_to_ascii(convert_to_greyscale(resized))
    datalen = len(ascii_data)

    for i in range(0, datalen, width):
        result.append("".join(ascii_data[i:i+width]))
    
    result = "\n".join(result)
    print(result)
    with open("{}/output.txt".format(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))), 'w') as fileout:
        fileout.write(result)
    return result


def braille_convert(path, divid):
    worklist1 = []
    worklist2 = []
    result = ""
    #path = input("Enter a valid pathname:\n")

    try:
        image = Image.open(path)
    except:
        print("Invalid file or path!")
        exit(1)

    """
    while True:
        divid = int(input("Enter resize divider: "))
        if divid < 1:
            print("Invalid value!")
        else:
            break
    """

    resized = resize_image(image, divid)
    width, height = resized.size
    data = list(resized.getdata(0))
    
    worklist2 = onedim2twodim(data, width)
    worklist1 = split_to_braille_chunks(worklist2)

    del worklist2[:]

    worklist2 = chunks_to_braille(worklist1)

    del worklist1[:]

    for n in range(0, len(worklist2), width//2):
        worklist1.append(worklist2[n:n+width//2])

    for n in worklist1:
        result += "".join(n)
        result += "\n"
    
    print(result)
    with open("output.txt", 'w') as fileout:
        fileout.write(result)
    #return result


if __name__ == "__main__":
    #braille_convert()
    ascii_convert()
import logging
import os
import numpy as np
from PIL import Image

logging.basicConfig(filename='logs.log', level=logging.DEBUG)

gscale1 = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'  "


# gray scale level values from:
# http://paulbourke.net/dataformats/asciiart/

# 70 levels of gray

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def getAverageL(image):
    """
    Given PIL Image, return average value of grayscale value
    """
    # get image as numpy array
    im = np.array(image)

    # get shape
    w, h = im.shape

    # get average
    return np.average(im.reshape(w*h))


def covertImageToAscii(fileName, rows):
    """
    Given Image and dims (rows, cols) returns an m*n list of Images
    """
    # declare globals
    global gscale1

    # open image and convert to grayscale
    image = Image.open(fileName).convert('L')

    # store dimensions
    W, H = image.size[0], image.size[1]

    # compute width of tile
    h = H/rows

    # compute tile height based on aspect ratio and scale
    w = W*h/H

    # compute number of rows
    cols = int(W/w)

    # check if image size is too small
    if cols > W or rows > H:
        print("Image too small for specified cols!")
        exit(0)

    # ascii image is a list of character strings
    aimg = []
    # generate list of dimensions
    for j in range(rows):
        y1 = int(j*h)
        y2 = int((j+1)*h)

        # correct last tile
        if j == rows-1:
            y2 = H

        # append an empty string
        aimg.append("")

        for i in range(2*cols):

            # crop image to tile
            x1 = int(i*w*0.5)
            x2 = int((0.5*i+1)*w)

            # correct last tile
            if 0.5*i == cols-1:
                x2 = W

            # crop image to extract tile
            img = image.crop((x1, y1, x2, y2))

            # get average luminance
            avg = int(getAverageL(img))

            aimg[j] += gscale1[int((avg*69)/255)]

    return aimg


def main():

    root_path = os.path.join(os.path.dirname(__file__), "Frames")

    cols = os.get_terminal_size()[1]
    frame = 0

    while(os.path.exists(root_path+f"Frame_{frame}.jpg")):

        img_path = root_path+f"Frame_{frame}.jpg"
        aimg = covertImageToAscii(img_path, cols)

        cls()

        # printing the ascii
        for row in aimg:
            print(row)

        frame = frame + 1
        logging.info(frame)


if __name__ == '__main__':
    main()

import numpy as np
import math
import cv2


def imgsplice(img):
    dir = 'C:\\Users\\invke\\Desktop\\Project\\Python\\Passive Learning Youtube\\Letter\\'
    i, j = 0, 0
    off = [1, -4, -3, -2, 1, 4, 6, 6, 10, 12]
    btmoffcord = {10: 12, 11: 13, 15: 13, 16: 12, 27: 2, 41: 13}
    keys = list(btmoffcord.keys())
    vals = list(btmoffcord.values())
    btmoff = [vals[keys.index(i)] if i in btmoffcord else 0 for i in range(50)]
    amtx = 30
    amty = 42

    while i < 10:
        i = i + 1
        while j < 5:
            j = j + 1
            xtmp = 140+(i-1)*150+off[i-1]
            Letter = crop(img, 22+(j-1)*268, 22+j*268, xtmp, xtmp+146)
            index = (i-1)*5+(j-1)
            if(btmoff[index] != 0):
                letroff = imgmov(Letter, btmoff[index], [150, 230], 146, 268)
                croped = crop(letroff, amty+8, 268-amty-83, amtx, 146-amtx)
                saveimg(croped, dir, str(i) + ',' + str(j))
            else:
                croped = crop(Letter, amty+8, 268-amty-83, amtx, 146-amtx)
                saveimg(croped, dir, str(i) + ',' + str(j))
        j = 0


def showimg(img):
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def saveimg(img, dir, name):
    cv2.imwrite(dir + name + '.jpg', img)


def crop(img, x1, x2, y1, y2):
    n1 = np.arange(x1, x2)
    n2 = np.arange(y1, y2)
    return img[n1[:, None], n2[None, :]]


def initialize():
    directory = 'C:\\Users\\invke\\Desktop\\Project\\Python\\Passive Learning Youtube\\'

    img = cv2.imread(directory + 'Free Japanese Letter Vector-01.jpg', 0)

    imgsplice(img)
    # showimg(imgmov(img, 50, [500, 800], 1800, 1400))


def imgmov(img, off, strip, length, width):
    i, j = 0, 0
    x, y = img.shape
    imgtmp = np.zeros((x, y), dtype=np.uint8)
    # imgtmp = [[0 for i in range(length)] for j in range(width)]
    while j < width:
        while i < length:
            if j > strip[0] and j < strip[1]:
                if i+off > length-1:
                    imgtmp[j][i+off-length] = img[j][i]
                else:
                    imgtmp[j][i+off] = img[j][i]
            else:
                imgtmp[j][i] = img[j][i]
            i = i+1
        j = j+1
        i = 0
    return imgtmp


# img = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# img = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17, 18, 19, 20], [21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
#        [31, 32, 33, 34, 35, 36, 37, 38, 39, 40], [41, 42, 43, 44, 45, 46, 47, 48, 49, 50], [51, 52, 53, 54, 55, 56, 57, 58, 59, 60]]

# imgmov(img, 2)
initialize()

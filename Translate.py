from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import numpy as np
import cv2
import time


def startup(driver):
    language = driver.find_element_by_xpath(
        '//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[1]/c-wiz/div[5]/button')
    language.click()

    japanese = driver.find_element_by_xpath(
        '//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[3]/c-wiz/div[2]/div/div[3]/div/div[2]/div[47]')
    japanese.click()


def driversetup():
    PATH = "C:\Program Files (x86)\Chrome Driver for Selenium\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.get("https://translate.google.com/")

    startup(driver)

    translate(driver, 'hello')

    driver.close()


def translate(driver, input):
    translate = driver.find_element_by_class_name("er8xn")
    translate.send_keys(input)

    time.sleep(5)

    translateden = driver.find_element_by_xpath(
        '//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[2]/div[5]/div/div[2]/div[1]')
    translatedjp = driver.find_element_by_xpath(
        '//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[2]/div[5]/div/div[1]/span[1]/span/span')

    print(translateden.text)
    print(translatedjp.text)

    time.sleep(5)

    return [translateden.text, translatedjp.text]


def showimg(img):
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def getdat(loc):
    dir = 'C:\\Users\\invke\\Desktop\\Project\\Python\\Passive Learning Youtube\\' + loc
    return [cv2.imread(dir + str(i) + '.jpg', 0) for i in range(50)]
# driversetup()


def txt2imgjp(text, data):
    img = [[]]
    key = [0, 1, 2, 3, 4, 5, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
           26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 42, 44, 45, 46, 47, 48, 49]
    value = [12354, 12356, 12358, 12360, 12362, 12431, 12363, 12365, 12367, 12369, 12371, 12373, 12375, 12377, 12379, 12381, 12383, 12385, 12388, 12390, 12392,
             12394, 12395, 12396, 12397, 12398, 12399, 12402, 12405, 12408, 12411, 12414, 12415, 12416, 12417, 12418, 12420, 12422, 12424, 12425, 12426, 12427, 12428, 12429]
    indexlist = [key[value.index(ord(i))] for i in text]
    for ind, i in enumerate(indexlist, start=0):
        if ind == 0:
            img = data[i]
        else:
            img = np.hstack((img, data[i]))
    showimg(img)


def txt2imgen(text, data):
    img = [[]]
    key = [0, 1, 2, 3, 4, 5, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
           26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 44, 45, 46, 47, 48, 49]
    value = ['a', 'i', 'u', 'e', 'o', 'wa', 'ka', 'ki', 'ku', 'ke', 'ko', 'sa', 'shi', 'su', 'se', 'so', 'ta', 'chi', 'tsu', 'te', 'to', 'na',
             'ni', 'nu', 'ne', 'no', 'ha', 'hi', 'fu', 'he', 'ho', 'ma', 'mi', 'mu', 'me', 'mo', 'ya', ' ', 'yu', 'yo', 'ra', 'ri', 'ru', 're', 'ro']
    txtsplat = txtsplit(text)
    indexlist = [key[value.index(i)] for i in txtsplat]
    for ind, i in enumerate(indexlist, start=0):
        if ind == 0:
            img = data[i]
        else:
            img = np.hstack((img, data[i]))
    showimg(img)


# txt2imgjp('こにちは', getdat('jap x eng\\'))


def txtsplit(text):
    arr = []
    dat = [['a', 'chi', 'e', 'fu', 'i', 'o', 'u', 'wa', ' '], ['h', 'k', 'm', 'n', 'r', 's', 't', 'y'], ['ha', 'he', 'hi', 'ho'], ['ka', 'ke', 'ki', 'ko', 'ku'], [
        'ma', 'me', 'mi', 'mo', 'mu'], ['na', 'ne', 'ni', 'no', 'nu'], ['ra', 're', 'ri', 'ro', 'ru'], ['sa', 'se', 'shi', 'so', 'su'], ['ta', 'te', 'to', 'tsu'], ['ya', 'yo', 'yu']]
    i = 0
    while(i < len(text)):
        for j in dat[0]:
            if j[0] == text[i]:
                arr.append(j)
                i = i+len(j)-1
                break
        for ind, j in enumerate(dat[1], start=0):
            if j[0] == text[i]:
                for k in dat[2+ind]:
                    if k[1] == text[i+1]:
                        arr.append(k)
                        i = i+len(k)-1
                        break
                break
        i = i+1
    return arr


# txt2imgen("kon'nichiwa", getdat('jap x eng\\'))
txt2imgen("kon'nichiwa arigato", getdat('Letter\\'))
# print(txtsplit('konichiwa'))
# letter = 'あいうえおわかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろ'
# print([i if i < 6 else i + 4 for i in range(len(letter))])
# print(letter)
# print([ord(letter[i]) for i in range(len(letter))])

# decorate.py
import csv
import re
import numpy as np
import cv2

def getValuesFromCSV(csvFile):
    with open(csvFile, newline=None) as info:
        reader = csv.reader(info, delimiter=';')
        values = []
        for row in reader:
            corner_info = (row[0], row[8])
            # print(corner_info)
            values.append(corner_info)
        # for row in s
        return values

def adornImage(imagePath, cornerInfo):
    rawCorners = re.compile('(\d*,\d*)')
    corners = rawCorners.findall(cornerInfo)

    img = cv2.imread(imagePath, 0)
    print(imagePath)

    if img is None:
        return
    print(imagePath)
    for corner in corners:
        x, y = corner.split(',')
        point = int(x), int(y)
        cv2.circle(img, point, 1, (255, 255, 0), 10)
    
    return img


if __name__ == "__main__":
    img_dir = 'C:\\Data\\Image\\ANY_Passports\\'
    image_names = getValuesFromCSV("C:\Work\XVrs\ANY_Passports_20171214.txt")
    for image in image_names:
        img = adornImage(img_dir + image[0], image[1])



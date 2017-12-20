import cv2
import numpy as np
from matplotlib import pyplot as plt

if __name__ == "__main__":
    imgSrc = r"C:\Users\Donghan.Lee\sandbox\python\p.png"

    img = cv2.imread(imgSrc)

    angle = -16.975805476189414

    

    plt.subplot(121),plt.imshow(img),plt.title('Original')
    plt.show()

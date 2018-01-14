import argparse
import glob
import os
import cv2
import numpy as np
from matplotlib import pyplot as plt


def get_img_fft(imagedir):
    imgs_path = imagedir;
    #glob.glob(os.path.join(imagedir, '*.jpg'))
    for img_path in imgs_path:
        img = cv2.imread(img_path, 0)
        fft = np.fft.fft2(img)
        fft_shift = np.fft.fftshift(fft)
        s2 = np.log(np.abs(fft_shift))
        y, x = img.shape
        polar = cv2.logPolar(s2, (y//2, x//2), 40, cv2.INTER_LINEAR+cv2.WARP_FILL_OUTLIERS+cv2.WARP_INVERSE_MAP)
        plt.subplot(131), plt.imshow(img, 'gray'), plt.title('original')
        plt.subplot(132), plt.imshow(s2, 'gray'), plt.title('center')
        plt.subplot(133), plt.imshow(polar, 'gray'), plt.title('polar')
        plt.show()


def main():
    #parser = argparse.ArgumentParser()
    #parser.add_argument('--imagedir', help='image path')
    #args = parser.parse_args()
    get_img_fft("G:\\pic\\a1b.jpg")


if __name__ == '__main__':
    main()
import numpy as np
import math
import cv2

def PSNR(img1, img2):
    h, w, c = img1.shape
    PIXEL_MAX = 255.0
    mse = np.sum((img1-img2)**2)/(h*w*c)
    print("MSE:",mse)

    if mse == 0:
        return 100
    else:
        return 10*math.log10(math.pow(PIXEL_MAX,2)/mse)
    

original = cv2.imread("./0.png")                        # label image
contrast = cv2.imread("./depth_comb-WLS.png")           # our output image


result = PSNR(original, contrast)
print("PSNR result :",result)

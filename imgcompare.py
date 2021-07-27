from PIL import Image
import math
import operator
from functools import reduce


def image_contrast(img1, img2):

    image1 = img1
    image2 = img2

    h1 = image1.histogram()
    h2 = image2.histogram()

    image1.close()
    image2.close()
    
    result = math.sqrt(reduce(operator.add,  list(map(lambda a,b: (a-b)**2, h1, h2)))/len(h1) )
    return result

if __name__ == '__main__':
    img1 = "./1.png"
    img2 = "./2.png"
    result = image_contrast(img1,img2)
    print(result)
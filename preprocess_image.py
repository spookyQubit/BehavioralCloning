import numpy as np
import cv2
from sklearn.utils import shuffle

g_top_rows_to_crop = 65
g_bottom_rows_to_crop = 20

def get_cropped_image(img, up=g_top_rows_to_crop, down=g_bottom_rows_to_crop):
    """
    Crop image from top and bottom.
    Assumes that the shape of the image is in the form (height, width, color channels)
    """
    return img[up:img.shape[0] - down, ]


def grayscale(img):
    """Applies the Grayscale transform
    This will return an image with only one color channel
    but NOTE: to see the returned image as grayscale
    (assuming your grayscaled image is called 'gray')
    you should call plt.imshow(gray, cmap='gray')"""
    return cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    # Or use BGR2GRAY if you read an image with cv2.imread()
    #return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


def gaussian_blur(img, kernel_size):
    """Applies a Gaussian Noise kernel"""
    return cv2.GaussianBlur(img, (kernel_size, kernel_size), 0)


def histogram_equal(img):
    """
    Improves the contrast of the image
    """
    return cv2.equalizeHist(img)


def process_image(img):
    # Make a copy of the image
    image = np.copy(img)

    # Cropped image
    image = get_cropped_image(image)

    # Convert the copy_image to grayscale
    image = grayscale(image)

    # gausian filtering
    #kernal_size = 5
    #image = gaussian_blur(image, kernal_size)

    # Hist equalization
    image = histogram_equal(image)

    # Normalize
    image = (image - image.mean()) * 1. / image.std()

    return image
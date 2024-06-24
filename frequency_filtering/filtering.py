# For this part of the assignment, You can use inbuilt functions to compute the fourier transform
# You are welcome to use fft that are available in numpy and opencv

import numpy as np


class Filtering:

    def __init__(self, image):
        """initializes the variables for frequency filtering on an input image
        takes as input:
        image: the input image
        """
        self.image = image
        self.mask = self.get_mask

    def get_mask(self, shape):
        """Computes a user-defined mask
        takes as input:
        shape: the shape of the mask to be generated
        rtype: a 2d numpy array with size of shape
        """
        box=15
        xcorner1 = 226
        xcorner2 = 291
        xcorner3 = 207
        xcorner4 = 271
        mask = np.ones(shape)
        mask[xcorner1+6:xcorner1+box+6, xcorner1:xcorner1+box] = 0
        mask[xcorner2-65:xcorner2+box-65, xcorner2:xcorner2+box] = 0
        mask[xcorner3+67:xcorner3+box+67, xcorner3:xcorner3+box] = 0
        mask[xcorner4-10:xcorner4+box-10, xcorner4:xcorner4+box] = 0

        return mask

    def post_process_image(self, image):
        """Post processing to display DFTs and IDFTs
        takes as input:
        image: the image obtained from the inverse fourier transform, forward fourier transform, or filtered fourier transform 
        return an image with full contrast stretch
        -----------------------------------------------------
        You can perform post processing as needed. For example,
        1. You can perfrom log compression
        2. You can perfrom a full contrast stretch (fsimage)
        3. You can take negative (255 - fsimage)
        4. etc.
        """

        return image

    def filter(self):
        """Performs frequency filtering on an input image
        returns a filtered image, magnitude of frequency_filtering, magnitude of filtered frequency_filtering
        ----------------------------------------------------------
        You are allowed to use inbuilt functions to compute fft
        There are packages available in numpy as well as in opencv
        Steps:
        1. Compute the fft of the image
        2. shift the fft to center the low frequencies
        3. get the mask (write your code in functions provided above) the functions can be called by self.filter(shape)
        4. filter the image frequency based on the mask (Convolution theorem)
        5. compute the inverse shift
        6. compute the inverse fourier transform
        7. compute the magnitude
        8. You will need to do post processing on the magnitude and depending on the algorithm (use post_process_image to write this code)
        Note: You do not have to do zero padding as discussed in class, the inbuilt functions takes care of that
        filtered image, magnitude of frequency_filtering, magnitude of filtered frequency_filtering: Make sure all images being returned have grey scale full contrast stretch and dtype=uint8
        """
        f = np.fft.fft2(self.image)
        f1shift = np.fft.fftshift(f)
        mag_spectrum1 = 10*np.log(1+np.abs(f1shift))
        
        mask = self.get_mask(mag_spectrum1.shape)
        
        f2 = f1shift*(mask)
        mag_spectrum2 = 10*np.log(1+np.abs(f2))
        img1 = np.abs(np.fft.ifft2(f2))
        
        
        return [img1, mag_spectrum1, mag_spectrum2]

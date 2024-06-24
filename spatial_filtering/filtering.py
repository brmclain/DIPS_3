import numpy as np
import math

class Filtering:

    def __init__(self, image):
        self.image = image

    def get_gaussian_filter(self):
        """Initialzes/Computes and returns a 5X5 Gaussian filter"""
        mask = np.zeros((5, 5))
        sigma = 1
        total = 0
        for i in range(5):
            for j in range(5):
                temp = (1/(2*math.pi*sigma**2))*math.exp(-1*(((i**2)+(j**2))/(2*sigma**2)))
                total += temp
                mask[i][j] = temp
        for i in range(5):
            for j in range(5):
                temp = mask[i][j]
                mask[i][j] = temp/total
        return mask
    def get_laplacian_filter(self):
        """Initialzes and returns a 3X3 Laplacian filter"""
        mask = [[0, 1, 0],
                [1,-4, 1],
                [0, 1, 0]]
        
        return mask

    def filter(self, filter_name):
        """Perform filtering on the image using the specified filter, and returns a filtered image
            takes as input:
            filter_name: a string, specifying the type of filter to use ["gaussian", laplacian"]
            return type: a 2d numpy array
                """
        if filter_name == "gaussian":
            img1 = np.zeros((len(self.image)+4, len(self.image[0])+4))
            img2 = np.zeros((len(self.image), len(self.image[0])))
            for i in range(len(self.image)):
                for j in range(len(self.image[0])):
                    img1[i+2][j+2] = self.image[i][j]
            
            mask = self.get_gaussian_filter()
            for i in range(2, len(img1)-2):
                for j in range(2, len(img1[0])-2):
                    total = 0
                    total = (mask[0][0]*img1[i-2][j-2] + mask[0][1]*img1[i-2][j-1] + mask[0][2]*img1[i-2][j-0] + mask[0][3]*img1[i-2][j+1] + mask[0][4]*img1[i-2][j+2] + 
                             mask[1][0]*img1[i-1][j-2] + mask[1][1]*img1[i-1][j-1] + mask[1][2]*img1[i-1][j-0] + mask[1][3]*img1[i-1][j+1] + mask[1][4]*img1[i-1][j+2] + 
                             mask[2][0]*img1[i-0][j-2] + mask[2][1]*img1[i-0][j-1] + mask[2][2]*img1[i-0][j-0] + mask[2][3]*img1[i-0][j+1] + mask[2][4]*img1[i-0][j+2] + 
                             mask[3][0]*img1[i+1][j-2] + mask[3][1]*img1[i+1][j-1] + mask[3][2]*img1[i+1][j-0] + mask[3][3]*img1[i+1][j+1] + mask[3][4]*img1[i+1][j+2] + 
                             mask[4][0]*img1[i+2][j-2] + mask[4][1]*img1[i+2][j-1] + mask[4][2]*img1[i+2][j-0] + mask[4][3]*img1[i+2][j+1] + mask[4][4]*img1[i+2][j+2] )
                    img2[i-2][j-2] = total
                    
        elif filter_name == "laplacian":
            img1 = np.zeros((len(self.image)+2, len(self.image[0])+2))
            img2 = np.zeros((len(self.image), len(self.image[0])))
            for i in range(len(self.image)):
                for j in range(len(self.image[0])):
                    img1[i+1][j+1] = self.image[i][j]
            mask = self.get_laplacian_filter()
            for i in range(1, len(img1)-1):
                for j in range(1, len(img1[0])-1):
                    total = 0
                    total = (mask[0][0]*img1[i-1][j-1] + mask[0][1]*img1[i-1][j-0] + mask[0][2]*img1[i-1][j+1] + 
                             mask[1][0]*img1[i-0][j-1] + mask[1][1]*img1[i-0][j-0] + mask[1][2]*img1[i-0][j+1] + 
                             mask[2][0]*img1[i+0][j-1] + mask[2][1]*img1[i+1][j-0] + mask[2][2]*img1[i+1][j+1] )
                    img2[i-1][j-1] = total
                    
        else:
            img2 = self.image
         
        return img2


# For this part of the assignment, please implement your own code for all computations,
# Do not use inbuilt functions like fft from either numpy, opencv or other libraries
import math
import numpy as np

class Dft:
    def __init__(self):
        pass

    def forward_transform(self, matrix):
        """Computes the forward Fourier transform of the input matrix
        takes as input:
        matrix: a 2d matrix
        returns a complex matrix representing fourier transform"""

        n = len(matrix)
        m = len(matrix[0])
        frwd_trans = np.zeros((n,m), dtype=np.complex_)
        for row in range(n-1):
            for col in range(m-1):
                temp = 0
                inside = 0
                for i in range(n-1):
                    for j in range(m-1):
                        inside = (-2*math.pi*row*i)/n + (-2*math.pi*col*j)/m
                        temp += math.cos(inside) + 1j*math.sin(inside)
                frwd_trans[row][col] = temp
        return frwd_trans

    def inverse_transform(self, matrix):
        """Computes the inverse Fourier transform of the input matrix
        You can implement the inverse transform formula with or without the normalizing factor.
        Both formulas are accepted.
        takes as input:
        matrix: a 2d matrix (DFT) usually complex
        returns a complex matrix representing the inverse fourier transform"""
        
        n = len(matrix)
        m = len(matrix[0])
        invr_trans = np.zeros((n,m), dtype=np.complex_)
        for row in range(n-1):
            for col in range(m-1):
                temp = 0
                inside = 0
                for i in range(n-1):
                    for j in range(m-1):
                        inside = (2*math.pi*row*i)/n + (2*math.pi*col*j)/m
                        temp += math.cos(inside) + 1j*math.sin(inside)
                invr_trans[row][col] = temp
        return invr_trans

    def magnitude(self, matrix):
        """Computes the magnitude of the input matrix (iDFT)
        takes as input:
        matrix: a 2d matrix
        returns a matrix representing magnitude of the complex matrix"""
        invr_matrix = self.inverse_transform(matrix)
        mag_matrix = np.zeros((len(invr_matrix), len(invr_matrix[0])))
        for i in range(len(invr_matrix)):
            for j in range(len(invr_matrix[0])):
                mag_matrix[i][j] = abs(math.sqrt(((invr_matrix[i][j].real)**2)+((invr_matrix[i][j].imag)**2)))
        return mag_matrix
import nibabel as nb 
import numpy as np 
import sys
import matplotlib.pyplot as plt

def plot_func(img,slice_n):
    #plt.title(f"K-space of the {slice_n}th slice")
    plt.figure()
    plt.imshow(img[slice_n],cmap='gray')
    plt.show()

if __name__ == '__main__':
    image = np.array(nb.load(sys.argv[1]).get_fdata()) # input data 
    option = sys.argv[2] # do inverse fft?
    
    k = np.fft.fftn(image) # fft to kspace
    k = np.fft.fftshift(k) # shift the 0-freq to center of image

    slice_n = 180 # example slice for visualization

    print(k.shape) # the k space data still has same shape as img
    plot_func(np.log(abs(k)), slice_n) # plot its log-scale for better visualization

    if option:
        rev = np.fft.ifftn(k)
        plot_func(abs(rev),slice_n)
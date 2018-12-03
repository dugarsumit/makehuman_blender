#from scipy.misc import imread
import numpy as np
from cv2 import imread
from scipy import misc

file = '/home/sumit/Desktop/poseSamples/render_data/human_0_rgb_3.png'
file1 = '/home/sumit/Desktop/img.exr'
file2 = '/home/sumit/Desktop/poseSamples/render_data/human_1_rgbd_20001.exr'
file3 = '/home/sumit/Desktop/save.png'



img = misc.imread(file)
img = np.array(img)
print(img.dtype)
print(np.max(img))
print(np.min(img))
print(img.shape)
print(np.unique(img))
#print(img[:,:,0])
print(img)
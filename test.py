import os
import matplotlib.pyplot as plt
import pathlib
import numpy as np
from skimage import io


#Set the path where images are stored
img_dir = pathlib.Path(__file__).parent.resolve()

images_lst = [file for file in os.listdir(img_dir)
            if file.endswith(".tif")]

data_path = os.path.join(img_dir,images_lst[1])
im = io.imread(data_path)

plt.imshow(im[1,1,:,:])
plt.show()

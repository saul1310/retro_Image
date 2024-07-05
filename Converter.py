from PIL import Image
import numpy as np
import os

# Get the current directory of the script
script_dir = os.path.dirname(__file__)
# Define the relative path to the image
image_path = os.path.join(script_dir, 'Example.jpg')




def image_to_array(image_path):
  
    with Image.open(image_path) as img:
      
        img_array = np.array(img)
    return img_array

def array_to_image(array):
    # Convert a numpy array back to an image
    return Image.fromarray(array)

def main():
 
    img_array = image_to_array(image_path)
    copied_array = img_array.copy()
    # at this point we have a copy of the array, we now need to reduce its size to a quarter before its converted back to an image
    
    
    # this functionality will iterate through every cell in the 2d matrix
    for i in range(len(copied_array)):
        for j in range(len(copied_array[0])):

    
    
    
    
    new_image = array_to_image(copied_array)
    new_image.show()

  

if __name__ == '__main__':
     main()


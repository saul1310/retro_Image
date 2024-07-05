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
    new_image = array_to_image(copied_array)
    new_image.show()

  

if __name__ == '__main__':
     main()


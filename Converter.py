from PIL import Image
import numpy as np
import os

# Get the current directory of the script
script_dir = os.path.dirname(__file__)
# Define the relative path to the image
image_path = os.path.join(script_dir, 'Example.jpg')
new_array_len = 0




def image_to_array(image_path):
  
    with Image.open(image_path) as img:
      
        img_array = np.array(img)
        global new_array_len
        new_array_len = len(img_array) //2
    # return img_array
    print(len(img_array))


def create_new_array():
     #we now need to create a new array that is half as big before its converted back to an image
     global new_array_len
     new_array = [[]]
     for i in range(new_array_len):
         new_array.append([0])
     print(new_array_len)


def array_to_image(array):
    # Convert a numpy array back to an image
    return Image.fromarray(array)
def main():
    image_to_array(image_path)
    create_new_array()

    
    
    
    
    # new_image = array_to_image(copied_array)
    # new_image.show()

  

if __name__ == '__main__':
     main()

